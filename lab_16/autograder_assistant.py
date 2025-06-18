# Python imports
import sys
import math
import ast
import astor
import re
import threading
import trace
import os
from multiprocessing import shared_memory as shm
import importlib.util
import traceback

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt, QRect, pyqtSlot, QThreadPool, QObject, QThread, pyqtSignal, QTimer
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication
import PyQt6.QtWidgets
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QColor, QPalette

try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

# Override Python's built in input() function so we can get test data fed into
# a program without having to use the command line to redirect input.
class InputException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def input(*args, **kwargs):    
    try:
        l_data = shm.ShareableList(sequence=None,name="l_data")
    except:
        l_data = [None]
    i_data = l_data[0]
    if(i_data == None):
        raise InputException("InputException")

    for i in range(len(l_data)-1):
        l_data[i] = l_data[i+1]
    # Set last input in list of inputs to None
    l_data[-1] = None
    
    print("\n====================\nYour input statement:", args[0])
    print("The value entered by the autograder:", str(i_data), "\n====================\n")
    
    l_data.shm.close()
    
    return i_data

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
    
def wrapper(function, parameter_list, result):
    '''
    Input: Function to run (student functions), paramaters for function, var result to return result
    Outputs: result (error or output if passes)
    '''
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


def syntax_checker(filename, window, timeout=0):
    '''
    Inputs filename, looks for banned syntax
    Outputs b_proceed and s_error_msg
    '''
    try:
        with open(filename,"r") as f:
            code = f.read()
    except Exception as exc:
        return False, "Your file could not be read.  Make sure it is named correctly.  "
    parsed = ast.parse(code)
    for node in ast.walk(parsed):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
            # set value to empty string
            node.value = ast.Constant(value='')
    s_trimmed_code = astor.to_source(parsed)  
    pattern = r'^.*"""""".*$' # remove empty """"""
    s_trimmed_code = re.sub(pattern, '', s_trimmed_code, flags=re.MULTILINE)

    # Added checker to ensure the header is not removed and would crash test_all_submissions
    if("if __name__ != \"__main__\":" not in s_trimmed_code and "from autograder_assistant import input" not in s_trimmed_code):
        return False, "The header structure has been deleted. Please ensure that the following line is in the submission:<br><br> <font color=orange>if</font> __name__ != <font color=green>\"__main__\"</font>:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color=orange>from</font> autograder_assistant <font color=orange>import</font> <font color=purple>input</font>"


    # Dynamically import student file and test for global Scope infinite loop
    if getattr(sys, "frozen", False):
        dir_path = os.path.dirname(sys.executable)
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))
    name = filename[:-3]
    specific_student = importlib.util.spec_from_file_location(name, os.path.join(dir_path, filename))
    sm = importlib.util.module_from_spec(specific_student)
    output = window.testFunction(specific_student.loader.exec_module, (sm,))
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
        # remove comments


        # https://stackoverflow.com/questions/1769332/script-to-remove-python-comments-docstrings
##            with open(filename,"r") as f:
##                code = f.read() 
##            parsed = ast.parse(code)
##            for node in ast.walk(parsed):
##                if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
##                    # set value to empty string
##                    node.value = ast.Constant(value='') 
##            s_trimmed_code = astor.to_source(parsed)  
##            pattern = r'^.*"""""".*$' # remove empty """"""
##            s_trimmed_code = re.sub(pattern, '', s_trimmed_code, flags=re.MULTILINE) 

        
        # look for syntax that is not allowed
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
    
class Worker(QObject):
    '''
    Worker Thread to run Autograder
    requires autoGrader module, filename of student_submission, assistant module, and window reference
        
    Sends errorOccured,and end pyqtSignals
    '''
    end = pyqtSignal(object)
    errorOccurredSig = pyqtSignal(object)

    def __init__(self, autoGrader, filename, assistant, window):
        super().__init__()
        self.autoGrader = autoGrader
        self.filename = filename
        self.assistant = assistant
        self.window = window
    
    def run(self):
        '''
        This function runs the autograder and catches high level errors in the autograder to return
        '''
        try:
            result = self.autoGrader(self.filename, self.assistant, self.window)
            self.end.emit(result)
        except Exception as exc:
            exception_info = traceback.format_exc()
            result = [[False], ["<font color=red size = 5>" + "<br><br>line".join(str(exception_info).split(", line")) + "</font>"]]
            self.end.emit(result)
        
# Autograder GUI
# Inputs window, list of passes/fails, error messages to display, testSets (how many test in each task)
class MainWindow(QMainWindow):
    '''
    Autograder GUI
    Inputs window, list of passes/fails, error messages to display, testSets (how many test in each task)
    '''
    progress = pyqtSignal(int)
    def __init__(self, autoGrader, filename, assistant,testSets):
        super().__init__()
        
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle('Autograder')
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)

        ## Loading Screen
        widget = QWidget()
        layout = QVBoxLayout()
        message = QLabel("<b>Autograder is running...<br> Please be patient.</b>")
        font = widget.font()
        font.setPointSize(30)
        message.setFont(font)
        message.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(message)
        self.passes = []
        self.error_msgs = []
        self.testSets = testSets
        self.flag = True

        self.progressBar = PyQt6.QtWidgets.QProgressBar(self)
        self.progressBar.setMaximum((sum(testSets)+1)*3)
        self.progressBar.setGeometry(200, 400, 400, 30)
        self.progress.connect(self.updateProgress)
        layout.addWidget(self.progressBar)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        if(len(testSets) == 1):
            self.testSets = []
        
        self.show()
        self.startAutoGrader(autoGrader, filename, assistant, self)

    # Tests for infinite loops, errors
    # Inputs: function to test, paramater list to pass, input list for input statements
    # Outputs: result or error message
    def testFunction(self, function, parameter_list=(), input_list=[]):
        '''
        Tests for infinite loops, errors
        Inputs: function to test, paramater list to pass, input list for input statements
        Outputs: result or error message 
        '''
        # Return either Infinite, Error, or All Good
        global l_data
        l_data = input_list
        result =["Error"]
        #print(l_data)
        p = thread_with_trace(target=wrapper, args=(function,parameter_list, result), daemon=True)
        p.start()
        p.join(3)
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
        '''
        Handle progress signal
        '''
        self.progressBar.setValue(self.progressBar.value() + newValue)

    def startAutoGrader(self, autoGrader, filename, assistant, window):
        '''
        Start Autograder thread and worker
        '''
        self.thread = QThread()
        self.worker = Worker(autoGrader, filename, assistant, window)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.end.connect(self.thread.quit)
        self.worker.end.connect(self.worker.deleteLater)
        
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.errorOccurredSig.connect(self.handleError)
        self.worker.end.connect(self.handleResult)
        self.worker.end.connect(self.updateWindow)

        self.thread.start()
        
    def updateWindow(self):
        '''
        After thread has run, update window with results
        '''
        if(sum(self.testSets) != len(self.passes)):
            self.testSets = []
        QApplication.restoreOverrideCursor()
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

                if self.passes[i_test_num]:
                    image.setText("<img src='check.png' width='32' height='32'>")
                    text.setText("<font size=5>Test " + str(i_test_num+1) +" Passed!</font>")
                    num_passed += 1
                else:
                    image.setText("<img src='redX.png' width='32' height='32'>")
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
        '''
        Display summary message at the top of the window
        '''
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

    # The following function handle the signals being sent
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

        
def displayWindow(autoGrader, filename, assistant, testSets = []):
    app = QApplication(sys.argv)
    window = MainWindow(autoGrader, filename, assistant, testSets)
    window.show()
    app.exec()
