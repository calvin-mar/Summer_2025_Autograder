# Python imports
import os
import sys
import re
import subprocess
import shutil
import importlib.util

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from layout_colorwidget import Color

## This section contains to function to block and enable print
## The purpose of this is to avoid flooding the shell with
## Numerous autograder starting/ending messages

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
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
        if(file != "test_all_submissions.py"):
            for directory in dirs:
                if(directory != "__pycache__"):
                    shutil.copy(file, directory)

def test_submission(directory_name):
    # This function tests each individual submission
    # Given the directory name, it runs the autograder inside and returns the result
    # This requires each autograder to be refactored to include a 
    files = os.listdir(directory_name)

    # Find the autograder amongst the files 
    for file in files:
        if( len(re.findall("lab_\d\d_autograder", file)) == 1):
            cwd = os.getcwd()
            path_to_autograder = os.path.join(cwd,directory_name,file)
            #print(path_to_autograder)
            sys.path.append(os.path.join(cwd,directory_name))
            autograder_file = file[:-3]
            specific = importlib.util.spec_from_file_location(autograder_file, path_to_autograder)
            autograder = importlib.util.module_from_spec(specific)
            specific.loader.exec_module(autograder)
            # Add Timer and Exceptions
            student_result = autograder.testing()

            return student_result
    return False

class MainWindow(QMainWindow):
    def __init__(self):
        ## Prepare Window
        super().__init__()

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        ## Run through all files and folders
        ## In each folder, that is not pycache, run the autograder inside it
        cwd = os.getcwd()
        for name in os.listdir(cwd):
            if(not os.path.isfile(name) and name != "__pycache__"):
                testCase = QLabel("Test for " + str(name))
                blockPrint()
                result = test_submission(name)
                enablePrint()
                if(result):
                    testCase.setText("<img src='check.png' width='32' height='32'><font color=black>Test for " + str(name) + " Passed </font>")
                else:
                    testCase.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test for " + str(name) + " Failed </font>")

                testCase.setWordWrap(True)
                self.vbox.addWidget(testCase)
        
        self.vbox.addStretch()
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle('All Submissions')
        self.show()
        
        return 

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

    
