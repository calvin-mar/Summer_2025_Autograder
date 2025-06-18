# Python imports
import os
import sys
import re
import subprocess
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
    sys.stdout = open(os.devnull, 'w')

# Restore Printing
def enablePrint():
    sys.stdout = sys.__stdout__

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
        if(file != "test_all_submissions.py" and len(re.findall("lab_\d\d_student_submission", file)) != 1):
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
                
                #blockPrint()
                try:
                    student_result = self.test_submission(name, window)
                except Exception as exc:
                    student_result = ["Bad"]
                    
                #enablePrint()
                self.names.append(name)
                self.results.append(student_result)

    def test_submission(self,directory_name, window):
        # This function tests each individual submission
        # Given the directory name, it runs the autograder inside and returns the result
        # This requires each autograder to be refactored to include a 
        files = os.listdir(directory_name)

        # Find the autograder amongst the files 
        for file in files:
            if( len(re.findall("lab_\d\d_autograder", file)) == 1):
                cwd = os.getcwd()
                path_to_autograder = os.path.join(cwd,directory_name,file)
                sys.path.append(os.path.join(cwd,directory_name))
                autograder_file = file[:-3]
                specific = importlib.util.spec_from_file_location(autograder_file, path_to_autograder)
                autograder = importlib.util.module_from_spec(specific)
                specific.loader.exec_module(autograder)

                test_num = autograder.getTestsNum()
                self.testNum.emit(test_num)
                student_result = autograder.testing(window)

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
            result[0]

class MainWindow(QMainWindow):
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
        widget = QLabel("<b>Autograders are running...<br> Please be patient.</b>")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(widget)

        self.progressBar = PyQt6.QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(200, 400, 400, 30)
        self.progress.connect(self.updateProgress)

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
                if(self.results[student_num][0] == "Bad"):
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

def main():
    disperse_documents()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()

    
