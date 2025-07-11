# Python imports
import os
import sys
import re
import subprocess
import astor
import ast
import shutil
import importlib.util
import threading

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt, QObject, QThread, pyqtSignal
from PyQt6.QtWidgets import *
import PyQt6.QtWidgets

## This section contains to function to block and enable print
## The purpose of this is to avoid flooding the shell with
## Numerous autograder starting/ending messages

# Disable Printing
def blockPrint():
    idleStdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    return idleStdout

# Restore Printing
def enablePrint(idleStdout):
    sys.stdout = idleStdout


def disperse_documents():
    ## Place this document into a top level folder
    ## This script will copy overall files in the top level folder into all subfolders
    ## This script will not copy over itself.

    # Organize Files and Directories
    cwd = os.getcwd()
    files = []
    dirs = []
    for name in os.listdir(cwd):
        if(os.path.isfile(name)):
            files.append(name)
        else:
            dirs.append(name)

    # Do the Copying
    for file in files:
        if(file != "test_all_submissions.py" and len(re.findall("lab_\\d\\d_student_submission", file)) != 1):
            for directory in dirs:
                if(directory != "__pycache__"):
                    shutil.copy(file, directory)

class Worker(QObject):
    end = pyqtSignal(object)
    errorOccurredSig = pyqtSignal(object)
    testNum = pyqtSignal(int)

    def __init__(self, cwd, window):
        super().__init__()
        self.cwd = cwd
        self.window = window
        self.names = []
        self.results = []

    def run(self):
        self.navigate_submissions(self.window)
        output = [self.names, self.results]
        self.end.emit(output)
        
    def navigate_submissions(self, window):
        for name in os.listdir(self.cwd):
            if(not os.path.isfile(name) and name != "__pycache__"):
                testCase = QHBoxLayout()
                image = QLabel("")
                image.setFixedSize(52,52)
                text = QLabel("Test for " + str(name))
                text.setWordWrap(True)
                text.setMargin(5)
                
                idleStdout = blockPrint()
                try:
                    student_result = self.test_submission(name, window)
                except Exception as exc:
                    print(exc)
                    student_result = [["Bad"], "Bad"]
                    
                enablePrint(idleStdout)
                self.names.append(name)
                if("WARNING" in student_result[1]):
                    student_result[0].append("WARNING")
                self.results.append(student_result[0])

    def test_submission(self,directory_name, window):
        # This function tests each individual submission
        # Given the directory name, it runs the autograder inside and returns the result
        # This requires each autograder to be refactored to include a 
        files = os.listdir(directory_name)

        # Find the autograder amongst the files 
        for file in files:
            if( len(re.findall("lab_\\d\\d_assistant.py", file)) == 1):
                cwd = os.getcwd()
                path_to_autograder = os.path.join(cwd,directory_name,file)
                sys.path.append(os.path.join(cwd,directory_name))
                autograder_file = file[:-3]
                specific = importlib.util.spec_from_file_location(autograder_file, path_to_autograder)
                assistant = importlib.util.module_from_spec(specific)
                specific.loader.exec_module(assistant)
                test_num = sum(assistant.getTestSets())
                self.testNum.emit(test_num)
                student_result = assistant.testing(window)
                return student_result
        return [False]
    
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
            result[0] = "Error"

class MainWindow(QMainWindow):
    # VBox layout
    # Similar to AutoGrader Main Window
    # But displays one QHLayout per student, instead of per test.
    # Changes to AutoGrader Main Window methods should be implemented here as well

    progress = pyqtSignal(int)
    def __init__(self):
        ## Prepare Window
        super().__init__()
        self.names = []
        self.results = []
        self.cwd = os.getcwd()
        self.studentCount = -1
        for name in os.listdir(self.cwd):
            if(not os.path.isfile(name)):
                self.studentCount += 1

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle('Test All Submissions')
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)

        ## Loading Screen
        
        widget = QWidget()
        layout = QVBoxLayout()
        message = QLabel("<b>Autograders are running...<br> Please be patient.</b>")
        font = widget.font()
        font.setPointSize(30)
        message.setFont(font)
        message.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(message)
        self.progressBar = PyQt6.QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(200, 400, 400, 30)
        self.progress.connect(self.updateProgress)
        layout.addWidget(self.progressBar)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        ## Run through all files and folders
        ## In each folder, that is not pycache, run the autograder inside it
        self.show()
        self.beginTesting()


    def beginTesting(self):
        self.thread = QThread()
        self.worker = Worker(self.cwd, self)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.end.connect(self.thread.quit)
        self.worker.end.connect(self.worker.deleteLater)
        
        self.worker.testNum.connect(self.setMaximumBar)
        self.worker.end.connect(self.handleResults)
        self.worker.end.connect(self.updateWindow)

        self.thread.start()

    def updateWindow(self):
        #print("NAMES: ", self.names)
        #print("RESULTS: ", self.results)
        QApplication.restoreOverrideCursor()
        self.setCentralWidget(self.widget)
        
        ## This section process the individual's result and adds the appropriate message to the display
        student_num = 0
        for name in self.names:
            
            testCase = QHBoxLayout()
            test = QHBoxLayout()
            image = QLabel("Image here")
            image.setFixedSize(52,52)
            text = QLabel("Student Test")
            text.setWordWrap(True)
            text.setMargin(5)

            num_passed = 0
            failed_list = []

            for index in range(len(self.results[student_num])):
                if self.results[student_num][index] == True:
                    num_passed +=1
                else:
                    failed_list.append(str(index+1))
            if(num_passed == len(self.results[student_num])):
                image.setText("<img src='check.png' width='52' height='52'>")
                text.setText("<font size=6><b>" + str(name) + " passed all tests!</b></font>")
            else:
                image.setText("<img src='redX.png' width='52' height='52'>")
                if(self.results[student_num][-1] == "WARNING"):
                    text.setText("<font size=8 color=red><b>WARNING: </b></font> <font size=6><b>" + str(name) + "'s submission may contain malicious code.</b></font>")
                elif(self.results[student_num][0] == "Bad"):
                    text.setText("<font size=6><b>" + str(name) + " The autograder has crashed, the most likely issue is a syntax error in the student submission.</b></font>")
                elif(len(self.results[student_num]) > 1):
                    text.setText("<font size=6><b>" + str(name) + " passed " + str(num_passed) + " tests. They need to complete test(s) " + ", ".join(failed_list) + ".</b></font>")
                else:
                    text.setText("<font size=6><b>" + str(name) + " did not pass all tests. There may be a global infinite loop, syntax error, or other file problem.</b></font>")
                
            testCase.addWidget(image)
            testCase.addWidget(text)
            self.vbox.addLayout(testCase)
            student_num += 1
        
        self.vbox.addStretch()
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 820, 600)
        self.setWindowTitle('All Submissions')
        self.show()
        
        return

    # Tests for infinite loops, errors
    # Inputs: function to test, paramater list to pass, input list for input statements
    # Outputs: result or error message
    def testFunction(self,function, parameter_list=(), input_list=[]):
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
        self.progressBar.setValue(self.progressBar.value() + newValue)

    def setMaximumBar(self, testNum):
        self.progressBar.setMaximum(self.studentCount * testNum * 3)

    def handleResults(self,output):
        self.names = output[0]
        self.results = output[1]
    ## Allows for Scrollable Text
    def resizeEvent(self, event):
        super().resizeEvent(event)
        for i in range(self.vbox.count()):
            widget = self.vbox.itemAt(i).widget()
            if isinstance(widget, QLabel):
                widget.setMaximumWidth(self.scroll.viewport().width()-20)

    def exit_clicked(self):
        self.dialog.close()
        
    def show_spaces(self, result):
      '''
      This function makes the spaces in the student submissions visible
      The purpose of this is to remove the frustration that occurs when results appear to be correct
      but is off by only a space or a tab causing some invisible differences.
      '''
      try:
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
    
      except Exception as e:
        print("failed :(", e, result)
        return result
        
    def syntax_checker(self, filename):
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

        if("if __name__ != \"__main__\":" not in s_trimmed_code and "from input_override import input, print" not in s_trimmed_code):
            return False, "The header structure has been deleted. Please ensure that the following line is in the submission:<br><br> <font color=orange>if</font> __name__ != <font color=green>\"__main__\"</font>:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font color=orange>from</font> input_override <font color=orange>import</font> <font color=purple>input</font>, <font color=purple>print</font>"

        malicious_list = ["__import__(", "import os", ".run(", "from os import", "import subprocess", "import sys", "from sys import", "from subprocess import"]
        malicious_search_list = ["(\\s|^)eval\\(", "[^a-zA-Z0-9]rm[^a-zA-Z0-9]"]
        for phrase in malicious_list:
            if(phrase in s_trimmed_code):    
                return False, "WARNING"
        for expression in malicious_search_list:
            if(re.search(expression, s_trimmed_code) != None):
                return False, "WARNING"

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
            else:
                return False, "There is likely a syntax error in this code"

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

def main():
    disperse_documents()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()

    
