## This is an autoGrader developed for the Centre CSC170 class by Calvin Mar and Adam Ibrahim
##
## The autoGrader requires two other files to run. There must exist a json file of the form lab_xx_testFile.json.
## The json file contains the necessary information to run all tests.
## The autoGrader also requires the student submission of the format lab_xx_student_submission.py
## If these files do not exist, the autoGrader will not function as expected.
##
## This document contains many functions and classes. The following are the most important to understand its function.
## - class Worker and function wrapper: These are necessary for running a function in a thread, receving output from it, and catching errors
## - class thread_with_trace: This class is necessary to allow threads to be killed after a set time, which prevents lag
## - function autoGrader: This function runs all tests on the student submission and returns the results.
##                        It also handles interpreting the information from the json file
## - class MainWindow: This class initializes the window to display the results to the student.
##                     It runs most other functions and contains several methods that are used for testing.
##                     The init also handles loading the json file data
##                     The window has two phases, the loading screen and the the display of results.
##                     The two phases are handled in __init__ and updateWindow respectively
## - method syntax_checker: This is a method of MainWindow. It handles checking for banned syntax and global infinite loops
##                          It also checks for potentially malicious student code such as "import os" or "eval"
## - function displayWindow: This function simply sets up and runs the MainWindow
## - main: This function handles finding the necessary student submission and json file, as source code or as an executable
##         It also runs displayWindow.
##
## Limitations of the json file autoGrader and future work
## - When comparing the results using a seperate function. The function must a) accept the student result as the first paramter and b) return True or False
## - The json file must be strictly formatted to work properly. See template.json for more information.
## - Does not currently handle global input statements for global variables
## - It would be relatively easy to create GUI to create JSON files for the autograder. (Check out ast.literal_eval(str))
                     

# Python imports
import sys
import ast
import astor
import re
import datetime
import random
import threading
import trace
import os
import json
from multiprocessing import shared_memory as shm
import multiprocessing
import importlib.util
import traceback
from PIL import Image, ImageSequence

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt, QRect, pyqtSlot, QThreadPool, QObject, QThread, pyqtSignal, QTimer, QRectF, QPointF
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication, QGraphicsProxyWidget, QGraphicsScene, QGraphicsView
import PyQt6.QtWidgets
from PyQt6.QtGui import QFont, QMovie
from PyQt6.QtGui import QColor, QPalette, QPainter

class thread_with_trace(threading.Thread):
  """
  This code provides a version of threading that allows for the threads to be killed.
  It attaches a trace to the thread which monitors a variable in order to kill a function.
  """
  def __init__(self, *args, **keywords):
    threading.Thread.__init__(self, *args, **keywords)
    self.killed = False

  def start(self):
    self.__run_backup = self.run
    self.run = self.__run      
    threading.Thread.start(self)

  def __run(self):
    sys.settrace(self.globaltrace)
    self.__run_backup()
    self.run = self.__run_backup

  def globaltrace(self, frame, event, arg):
    if event == 'call':
      return self.localtrace
    else:
      return None

  def localtrace(self, frame, event, arg):
    if self.killed:
      if event == 'line':
        raise SystemExit()
    return self.localtrace

  def kill(self):
    self.killed = True
    
# Input: Function to run (student functions), paramaters for function, var result to return result
# Outputs: result (error or output if passes)
def wrapper(function, parameter_list, result):
    try:
        result[0] = function(*parameter_list)
    except Exception as e:
        try:
            if(e.message == "InputException"):
                result[0] = "Input"
            else:
                result[0] = "Error"
        except:
            result[0]


#Copied from layout_colorwidget
class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
#endCopy
    
# Worker Thread to run Autograder
# Sends finished, resultReadySig, errorOccured, updateWindowSig pyqtSignal(s)

class Worker(QObject):
    '''
    This Worker takes a string filename, a dictionary testInfo, and an object window
    The pyqtSignals are initialized within the Worker to sent when the target is run
    This also has some expection catching for syntax errors in the student submission
    '''
    end = pyqtSignal(object)
    errorOccurredSig = pyqtSignal(object)

    def __init__(self, filename, testInfo, window):
        super().__init__()
        self.filename = filename
        self.window = window
        self.testInfo = testInfo
    
    def run(self):
        try:
            result = autoGrader(self.filename, self.testInfo, self.window)
            self.end.emit(result)
        except Exception as exc:
            exception_info = traceback.format_exc()
            result = [[False], ["<font color=red size = 5>" + "<br><br>line".join(str(exception_info).split(", line")) + "</font>"]]
            self.end.emit(result)

def autoGrader(student_submission, testInfo, window):
    '''
    inputs:
     - student_submission = String of the name of the student_submission file
     - testInfo = dictionary containg all of the data held in the json file
     - window = instance of MainWindow that is active, to call certain methods from

     outputs:
     - passes = a boolean list where passes[i] corresponds to whether test i was passed (True) or not (False)
     - error_msgs = a list of strings, with length equal the quantity of False in passes.
                    Each string corresponds to the message to display to the student


    This function loops through each test from testInfo running each function from the student submission with the necessary parameters and returns the aggregation of results.
    '''
    #sys.stdout = open(os.devnull, 'w')
    passes = []
    error_msgs = []
    
    print("Autograder starting...")

    if getattr(sys, "frozen", False):
        dir_path = os.path.dirname(sys.executable)
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))


    ## This section loads each necessary additional testing file that the autograder needs
    ## Consider for example math.isclose(), the autograder requires math to loaded and saved so that is may later run the .isclose() method
    moduleNames = testInfo["modules"]
    modules = {}

    for module in moduleNames:
      if((module + ".py") in os.listdir()):
            loaded_module = importlib.util.spec_from_file_location(module, os.path.join(dir_path, (module + ".py")))
            function_file = importlib.util.module_from_spec(loaded_module)
            loaded_module.loader.exec_module(function_file)
            modules[module] = function_file
      else:
            m = __import__(module)
            modules[module] = m

    ## Double check that the ShareableList doesn't exist
    try:
        l_data = shm.ShareableList(sequence=None, name="l_data")
        l_data.shm.close()
        l_data.shm.unlink()
    except:
        pass


    # Load the student_submission
    name = student_submission[:-3]
    specific_student = importlib.util.spec_from_file_location(name, os.path.join(dir_path, student_submission))
    sm = importlib.util.module_from_spec(specific_student)

    # Run the syntax_checker
    b_proceed, s_error_msg = window.syntax_checker(os.path.join(dir_path, student_submission))

    # If the syntax checker finds a problem, do not run the tests
    if b_proceed == False:
        passes.append(False)
        if(s_error_msg != ""):
            error_msgs.append(s_error_msg)
        else:
            error_msgs.append("There is a problem with your file")
    else:
        specific_student.loader.exec_module(sm)

        ## Run for each test
        for i in range(len(testInfo)-2):
            testIndex = str(i)
            isFunction = ("functionName" in testInfo[testIndex].keys())

            ## Determine how the function should be tested
            if("special" in testInfo[testIndex].keys()):
                specialTest = getattr(modules[testInfo[testIndex]["special"]["functionLocation"]], testInfo[testIndex]["special"]["functionName"])

            ## If it is a function, process the data as such, with potential inputs, and parameters
            if(isFunction):
              ## Prepare the information for the function and inputs/parameters
              function = getattr(sm, testInfo[testIndex]["functionName"])
              if("inputs" in testInfo[testIndex].keys()):
                inputs = testInfo[testIndex]["inputs"]
              else:
                inputs = []
              if("parameters" in testInfo[testIndex].keys()):
                parameters = tuple(testInfo[testIndex]["parameters"])
              else:
                parameters = ""

              ## Special catch for the Shareable List to ensure it does not exist
              try:
                l_data = shm.ShareableList(sequence=None, name="l_data")
                l_data.shm.close()
                l_data.shm.unlink()
              except:
                pass

              ## Initialize Shareable List for inputs
              l_data = shm.ShareableList(inputs, name = "l_data")

              ## This try/except catches high level errors in the function, such as the function not being defined
              try:

                ## Test function with or without parmaeters
                if(parameters != ""):
                  results = window.testFunction(function, parameters)
                else:
                  results = window.testFunction(function)

                ## This displays other errors that testFunction may catch
                if(results[1]):
                    if(len(inputs) > 0):
                      results[0] = results[0] + " The inputs were " + str(inputs)
                    if(len(parameters) > 0):
                      results[0] = results[0] + " The paramters were " + str(parameters)

                    error_msgs.append(results[0])
                    passes.append(False)
                ## Handles the result displays if no errors occur
                else:
                    ## Pass if testing against a value
                    if("output" in testInfo[testIndex].keys() and results[0] == testInfo[testIndex]["output"]):
                        passes.append(True)
                    ## Pass if testing with a function
                    elif("special" in testInfo[testIndex].keys() and specialTest(results[0], *testInfo[testIndex]["special"]["parameters"])):
                        passes.append(True)
                    ## Display incorrect result
                    else:
                        passes.append(False)
                        if("output" in testInfo[testIndex].keys()):
                          msg = " Failed: "+str(testInfo[testIndex]["functionName"])+"() should return "+str(testInfo[testIndex]["output"])
                        else:
                          msg = " Failed: "+str(testInfo[testIndex]["functionName"])+"() returns the incorrect result"
                          
                        if(len(inputs) > 0):
                          msg = msg + " when the inputs are " + str(inputs).replace("[","").replace("]","")
                        if(len(inputs) > 0 and len(parameters) > 0):
                          msg = msg + " and "
                        if(len(parameters) > 0):
                          msg = msg + " when the parameters are "+ str(parameters).replace("(","").replace(")","")

                        if("output" in testInfo[testIndex].keys()):
                          msg = msg + " but"
                        msg = msg + " it returns " + str(window.show_spaces(results[0])) + ".</font>"
                        error_msgs.append(msg)
                          
              except Exception as exc:
                passes.append(False)
                error_msgs.append(" Failed: Function "+str(testInfo[testIndex]["functionName"])+"() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
              l_data.shm.close()
              l_data.shm.unlink()
              
            ## Handles the testing if the it is against a global variable
            else:
              if("expectedValue" in testInfo[testIndex].keys() and getattr(sm, testInfo[testIndex]["globalVariable"]) == testInfo[testIndex]["expectedValue"]):
                passes.append(True)
              elif("special" in testInfo[testIndex].keys() and specialTest(getattr(sm, testInfo[testIndex]["globalVariable"]), *testInfo[testIndex]["special"]["parameters"])):
                passes.append(True)
              else:
                passes.append(False)
                if("expectedValue" in testInfo[testIndex].keys()):
                  error_msgs.append(" Failed: "+str(testInfo[testIndex]["globalVariable"])+" should be "+str(testInfo[testIndex]["expectedValue"])+" but it is " + str(window.show_spaces(getattr(sm, testInfo[testIndex]["globalVariable"]))) + ".</font>")
                else:
                  error_msgs.append(" Failed: "+str(testInfo[testIndex]["globalVariable"])+" is not the correct value but it is " + str(window.show_spaces(getattr(sm, testInfo[testIndex]["globalVariable"]))) + ". It is being compared against " + str(window.show_spaces(testInfo[testIndex]["special"]["parameters"])) + ".</font>")

            
    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")
    
    return passes, error_msgs
 


class problem(Exception):
    def __init__(self, exception_info):
        super().__init__(exception_info)
        
# Autograder GUI
# Inputs window, list of passes/fails, error messages to display, testSets (how many test in each task)
class MainWindow(QMainWindow):
    progress = pyqtSignal(int)
    def __init__(self, filename,testFile):
        super().__init__()
        
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle('Autograder')
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)

        ## Load tests
        with open(testFile, 'r') as file:
            self.testInfo = json.load(file)
        self.testSets = self.testInfo["testSets"]            
        
        ## Loading Screen

        widget = QWidget()
        layout = QVBoxLayout()
        message = QLabel("<b>Autograder is running...<br> Please be patient.</b>")
        font = widget.font()
        font.setPointSize(30)
        message.setFont(font)
        message.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.progressBar = PyQt6.QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(200, 400, 400, 30)
        self.progressBar.setMaximum(sum(self.testSets))
        self.progress.connect(self.updateProgress)
        layout.addWidget(message)
        layout.addWidget(self.progressBar)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.passes = []
        self.error_msgs = []
        
        self.flag = True

        if(len(self.testSets) == 1):
            self.testSets = []
        
        self.show()
        self.startAutoGrader(filename, self.testInfo, self)

    # Tests for infinite loops, errors
    # Inputs: function to test, paramater list to pass, input list for input statements
    # Outputs: result or error message
    def testFunction(self, function, parameter_list=(), input_list=[]):
        # Return either Infinite, Error, or All Good
        global l_data
        l_data = input_list
        result =["Error"]
        #print(l_data)
        p = thread_with_trace(target=wrapper, args=(function,parameter_list, result), daemon=True)
        p.start()
        p.join(4)
        output = []
        if p.is_alive():
            p.kill()
            output.append(" Failed: Function " + str(function.__name__) + "() caused an error. The function might contain an infinite loop or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!")
            output.append(True)
        elif result[0] == "Error":
            output.append(" Failed: Function " + str(function.__name__) + "() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!")
            output.append(True)
        elif result[0] == "Input":
            output.append("  Failed: Function " + str(function.__name__) + "() caused an error. It might contain an unexpected or extra input that is causing it to crash. Try adding some print statements to it to see what is happening!")
            output.append(True)
        else:
            output.append(result[0])
            output.append(False)
        self.progress.emit(3)
        return output

    def updateProgress(self, newValue):
        ## Connect to progress bar to move it aloong
        self.progressBar.setValue(self.progressBar.value() + newValue)

    def startAutoGrader(self, filename, testInfo, window):
        ## Connect necessary functions to signals from the Worker
        ## Pass the necessary paramters to the Worker
        ## Run the Worker
        
        self.thread = QThread()
        self.worker = Worker(filename, testInfo, window)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.end.connect(self.thread.quit)
        self.worker.end.connect(self.worker.deleteLater)
        
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.errorOccurredSig.connect(self.handleError)
        self.worker.end.connect(self.handleResult)
        self.worker.end.connect(self.updateWindow)

        self.thread.start()
    def resource_path(self, relative_path):
        #Gets absolute path for check.png/redX.png
        try:
            base_path = sys._MEIPASS
        except:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def updateWindow(self):
        '''
        Once the autoGrader has finished, this method updates the window to display the results
        '''

        ## Error catching to ensure that testSets are correct
        ## Also ensure that "Task 1" Does not display for global error messages
        if(sum(self.testSets) != len(self.passes)):
            self.testSets = []

        ## Reset the cursor to normal
        QApplication.restoreOverrideCursor()


        ## Initialize variables
        num_passed = 0
        error_count = 0

        self.trimFailed()

        seperateSets = False
        if len(self.testSets) >=1:
                seperateSets = True
        index=0
        taskNum=1
        if seperateSets:
            self.addHeader(taskNum)
        ## Display information for all tests
        for i_test_num in range(len(self.passes)):
            if seperateSets and index<self.testSets[taskNum-1]:
                    index+=1
            elif seperateSets:
                    taskNum+=1
                    self.addHeader(taskNum)             
                    index=1

            test = QHBoxLayout()
            image = QLabel("Image here")
            image.setFixedSize(32,32)
            text = QLabel("Test" + str(i_test_num+1))
            text.setWordWrap(True)
            text.setMargin(5)
            if len(self.passes) == 1:
                image.setText("")
                text.setText("<font size=5><b>"+self.error_msgs[error_count]+"</b></font>")
            else:
                check = self.resource_path("check.png")
                redX = self.resource_path("redX.png")
                if self.passes[i_test_num]:
                    image.setText(f"<img src='{check}' width='32' height='32'>")
                    text.setText("<font size=5>Test " + str(i_test_num+1) +" Passed!</font>")
                    num_passed += 1
                else:
                    image.setText(f"<img src='{redX}' width='32' height='32'>")
                    text.setText("<font color=black size=5>Test " + str(i_test_num+1) + " Failed: <br></font>" + self.error_msgs[error_count])
                    
                    error_count += 1
            test.addWidget(image)
            test.addWidget(text)
            self.vbox.addLayout(test)

        self.summaryScreen(num_passed)
        
        self.vbox.addStretch()
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
              
        self.setCentralWidget(self.scroll)

        self.show()
        return

    def trimFailed(self):
        i=0
        while i < len(self.error_msgs):
            #print("errors", self.error_msgs)
            self.error_msgs[i] = self.error_msgs[i].replace(" Failed: ", "")                
            i+=1

    def summaryScreen(self, num_passed):
        # Summary at top
        if(len(self.passes) > 1):
            summary = QHBoxLayout()
            image = QLabel("")
            
            image.setFixedSize(52,52)
            object = QLabel("Summary of Tests")
            object.setWordWrap(True)
            object.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if(len(self.passes) == num_passed):
                object.setText("<font color=green>CONGRATULATIONS YOU PASSED ALL TESTS!!!</font>")
            else:
                object.setText("<font color=red>You passed " + str(num_passed) + "/" + str(len(self.passes)) + " tests")
            image.setGeometry(QRect(object.x(), object.y(), object.width()-100, object.height()))
            font = QFont(object.font().family(), pointSize=24, weight=105)
            font.setBold(True)
            object.setFont(font)
            summary.addWidget(image)
            summary.addWidget(object)
            self.vbox.insertLayout(0, summary)

    def addHeader(self, taskNum):
        ## Display Header, as needed
        test = QHBoxLayout()
        text = QLabel()
        text.setText("<font color=black size=7><b>Task " + str(taskNum)+ ":<br>")
        test.addWidget(text)
        test.setAlignment(Qt.AlignmentFlag.AlignBottom)
        text.setAlignment(Qt.AlignmentFlag.AlignBottom)
        text.setFixedSize(120,32)
        self.vbox.addLayout(test)

    # Dynamically resizes text wrapping as window is resized
    def resizeEvent(self, event):
        super().resizeEvent(event)
        for i in range(self.vbox.count()):
              widget = self.vbox.itemAt(i).widget()
              if isinstance(widget, QLabel):
                    widget.setMaximumWidth(self.scroll.viewport().width()-20)

        
    def handleResult(self, result):
        self.passes = result[0]
        self.error_msgs = result[1]
        self.flag = False
        
    def handleError(self, exception_info):
        QApplication.restoreOverrideCursor()
        self.close()
        raise problem(str(exception_info))
            
    def exitClicked(self):
        self.dialog.close()

    def show_spaces(self, result):
      '''
      This function makes the spaces in the student submissions visible
      The purpose of this is to remove the frustration that occurs when results appear to be correct
      but is off by only a space or a tab causing some invisible differences.
      '''
      if(type(result) == str):
        to_return = list(result)
        i=0
        while(i < len(result) and to_return[i] in " \t"):
          if(to_return[i] == " "):
            to_return[i] = '\u2423'
          else:
            to_return[i] = "\\t"
          i += 1
        i = -1
        while(i < len(result) and to_return[i] in " \t"):
          if(to_return[i] == " "):
            to_return[i] = '\u2423'
          else:
            to_return[i] = "\\t"
          i -= 1
        to_return = "".join(to_return)
      else:
        to_return = result
        
      return to_return
      
        
    def syntax_checker(self, filename):
      '''
      syntax_checker received the string file name for the student submission and checks for banned and potentially dangerous code.
      It also checks that the header structure for the student submission exists and so that the autoGrader may run
      '''
        try:
            with open(filename,"r") as f:
                code = f.read()
        except:
            return False, "Your file could not be read.  Make sure it is named correctly.  "

        parsed = ast.parse(code)
        for node in ast.walk(parsed):
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
                # set value to empty string
                node.value = ast.Constant(value='') 
        s_trimmed_code = astor.to_source(parsed)  
        pattern = r'^.*"""""".*$' # remove empty """"""
        s_trimmed_code = re.sub(pattern, '', s_trimmed_code, flags=re.MULTILINE)
        
        if("if __name__ != \"__main__\":" not in s_trimmed_code and "from input_override import input" not in s_trimmed_code):
            return False, "The header structure has been deleted. Please ensure that the following line is in the submission:<br><br> <font color=orange>if</font> __name__ != <font color=green>\"__main__\"</font>:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color=orange>from</font> input_override <font color=orange>import</font> <font color=purple>input</font>, <font color=purple>print</font>"
        
        if getattr(sys, "frozen", False):
            dir_path = os.path.dirname(sys.executable)
        else:
            dir_path = os.path.dirname(os.path.realpath(__file__))
        name = filename[:-3]
        specific_student = importlib.util.spec_from_file_location(name, os.path.join(dir_path, filename))
        sm = importlib.util.module_from_spec(specific_student)
        output = self.testFunction(specific_student.loader.exec_module, (sm,))
        if(output[1]):
            if("infinite" in output[0]):
                return False, "There is a problem with your code, you may have an infinite loop outside of a function. Check that all loops have a ending condition."
            elif("input" in output[0]):
                return False, "There is a problem with your code, you may have unexpected or extra input statements outside of a function. Run your code and check how many inputs are called."

        # Check for triple quote and triple apostrophes
        s_triple_res = ""#check_for_triples()
        try:
            input_file = open(filename, "r")
            s_text = input_file.read()
            if "'''" in s_text or '"""' in s_text:
                s_triple_res = "Contains Triples"
            else:
                s_triple_res = "No Triples"
            input_file.close()
        except:
            s_triple_res = "Error Reading File"
        
        # if no triples, remove comments and continue
        s_error_msg = ""
        if s_triple_res == "No Triples":
            b_proceed = True
            if "join(" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b>join</b>() which is not allowed.  "
            if "zip(" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b>zip</b>() which is not allowed.  "
            if "exit(" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b><font color=purple>exit</font></b>() which is not allowed.  "
            if "quit(" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b><font color=purple>quit</font></b>() which is not allowed.  "
            if "break" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b><font color=orange>break</font></b> which is not allowed.  "
            if "continue" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b><font color=orange>continue</font></b> which is not allowed.  "
            if "random.choice(" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b><font color=orange>random.choice</font></b> which is not allowed.  "

            # look for print(f or print(F
            if re.search("print\\s*\\(\\s*[fF]\\s*[\'\"]+", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains formatted print statement(s) like print(f... or print(F... which are not allowed.  "


            # look for naked return
            if re.search(".*\\s+return\\s*\\n", s_trimmed_code) != None or re.search(".*\\s+return(\\s*\\\\s*)*\\n", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a 'naked return' which is not allowed.  A naked return is a return that is not followed by a variable or literal.  "

            # look for with open(
            if re.search("with\\s+open\\s*\\(", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code uses a <b><font color=orange>with</font> <font color=purple>open</font></b> statement which is not allowed.  "
            
            
            # look for _ as a variable name
            if re.search(".*\\s+_\\s+=.*", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a variable named _ which is not allowed.  "
            
            # look for comprehensions
            if re.search("=\\s*\\[+\\s*\\w+\\s+for\\s+", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a list comprehension which is not allowed.  "
                
            elif re.search("=\\s*\\[+.*for\\s+", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a list comprehension which is not allowed.  "
                
            if re.search("=\\s*\\{\\s*.*:\\s*.+\\s+for\\s+", s_trimmed_code) != None: 
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a dictionary comprehension which is not allowed.  "
          
            if re.search("=\\s*\\{+\\s*\\w+\\s+for\\s+", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a set comprehension which is not allowed.  "
            
            if re.search("=\\s*\\(+\\s*\\w+\\s+for\\s+", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a generator comprehension which is not allowed.  "
    
        
        else: # otherwise error message re triples and exit
            b_proceed = False
            if s_triple_res == "Contains Triples":
                s_error_msg = "Your code contains either triple quotes \"\"\" or triple apostrophes ''' which are not allowed."
            else:
                s_error_msg = "Your file could not be read.  Make sure it is named correctly.  "

        return b_proceed, s_error_msg


def displayWindow(filename, testFile):
    '''
    Create an instance of MainWindow
    '''
    app = QApplication(sys.argv)
    window = MainWindow(filename, testFile)
    window.show()
    app.exec()

def main():
    '''
    Get necessary filenames for student submission and json file, run displayWindow
    '''
    if getattr(sys, "frozen", False):
        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            dir_path = sys._MEIPASS
        except Exception as e:
            dir_path = os.path.abspath(".")
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))

    for name in os.listdir(dir_path):
        if(re.match("lab_\\d\\d_student_submission.py", name)):
            filename = name
            testFile = filename[:6] + "_testFile.json"

    displayWindow(filename, os.path.join(dir_path, testFile))

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
