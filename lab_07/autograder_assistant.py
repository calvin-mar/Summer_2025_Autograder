# Python imports
import sys
import math
import ast
import astor
import re
import threading
import os
from multiprocessing import shared_memory as shm

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt, QRect
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from layout_colorwidget import Color

try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

# Override Python's built in input() function so we can get test data fed into
# a program without having to use the command line to redirect input.
def input(*args, **kwargs):
    # Access l_data Here
    try:
        l_data = shm.ShareableList(sequence=None,name="l_data")
    except:
        l_data = [None]
    list(l_data)
    #########
    i_data = l_data[0]
    if(i_data == None):
        raise Exception
    for i in range(len(l_data)-1):
        l_data[i] = l_data[i+1]
    l_data[-1] = None
    print("\n====================\nYour input statement:", args[0])
    print("The value entered by the autograder:", str(i_data), "\n====================\n")
    l_data.shm.close()
    return i_data

def wrapper(function, parameter_list, result):
    try:
        result[0] = function(*parameter_list)
        
    except Exception as e:
        print(e)
        result[0] = "Error"
        
def is_inf(function, parameter_list=(), input_list=[]):
    # Return either Infinite, Error, or All Good
    global l_data
    l_data = input_list
    result =["Error"]
    #print(l_data)
    p = threading.Thread(target=wrapper, args=(function,parameter_list, result), daemon=True)
    p.start()
    p.join(3)
    if result[0] == "Error":
        return "Error"
    elif p.is_alive():
        return "Infinite"
    else:
        return result[0]

def syntax_checker(filename, timeout):
        print("Syntax checker starting...")

        ##################################################################################################
        ### new code
        ##################################################################################################

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
            with open(filename,"r") as f:
                code = f.read() 
            parsed = ast.parse(code)
            for node in ast.walk(parsed):
                #if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
                if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
                    # set value to empty string
                    node.value = ast.Constant(value='') 
            s_trimmed_code = astor.to_source(parsed)  
            pattern = r'^.*"""""".*$' # remove empty """"""
            s_trimmed_code = re.sub(pattern, '', s_trimmed_code, flags=re.MULTILINE) 

            
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
                
            if re.search("=\\s*\\[+.*for\\s+", s_trimmed_code) != None:
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


        print("...Syntax checker completed.")
        print()
        print("You may close the syntax checker window to exit.")

        return b_proceed, s_error_msg

class MainWindow(QMainWindow):
    def __init__(self, passes, error_msgs, testSets):
        super().__init__()

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        num_passed = 0
        error_count = 0

        #print(error_msgs)

        #Trimming "failed" from error messages
        i=0

        while i < len(error_msgs):
                error_msgs[i]=error_msgs[i].replace(" Failed: ", "")
                
                i+=1
        #print(error_msgs)
        seperateSets = False
        if len(testSets) >=1:
                seperateSets = True
        #print(testSets)
        index=0
        j=1
        if seperateSets:
                test = QHBoxLayout()
                text = QLabel()
                text.setText("<font color=black size=7><b>Task 1:<br>")
                test.setAlignment(Qt.AlignmentFlag.AlignBottom)
                text.setAlignment(Qt.AlignmentFlag.AlignBottom)
                text.setFixedSize(100,32)
                test.addWidget(text)
                self.vbox.addLayout(test)
        for i_test_num in range(len(passes)):
            #task seperation

            if seperateSets and index<testSets[j-1]:
                    print("true ", index)
                    index+=1
            elif seperateSets:
                    print("false")
                    test = QHBoxLayout()
                    text = QLabel()
                    text.setText("<font color=black size=7><b>Task " + str(j+1)+ ":<br>")
                    test.addWidget(text)
                    test.setAlignment(Qt.AlignmentFlag.AlignBottom)
                    text.setAlignment(Qt.AlignmentFlag.AlignBottom)
                    text.setFixedSize(100,32)
                    self.vbox.addLayout(test)
                    j+=1
                    index=1

            test = QHBoxLayout()
            image = QLabel("Image here")
            image.setFixedSize(32,32)
            text = QLabel("Test" + str(i_test_num+1))
            text.setWordWrap(True)
            text.setMargin(5)
            if passes[i_test_num]:
                image.setText("<img src='check.png' width='32' height='32'>")
                text.setText("<b>Test " + str(i_test_num+1) +" Passed!</b>")
                num_passed += 1
            else:
                image.setText("<img src='redX.png' width='32' height='32'>")
                text.setText("<font color=black size=5>Test " + str(i_test_num+1) + " failed: <br></b></font>" + error_msgs[error_count])
                
                error_count += 1
            test.addWidget(image)
            test.addWidget(text)
            self.vbox.addLayout(test)





        if(len(passes) > 1):
            summary = QHBoxLayout()
            image = QLabel("")
            
            image.setFixedSize(52,52)
            object = QLabel("Summary of Tests")
            object.setWordWrap(True)
            object.setAlignment(Qt.AlignmentFlag.AlignCenter)
            if(len(passes) == num_passed):
                #image.setText("<img src='check.png' width='52' height='52'>")
                object.setText("<font color=green>CONGRATULATIONS YOU PASSED ALL TESTS!!!</font>")
            else:
                #image.setText("<img src='octagon.png' width='52' height='52'><font color=black>")
                object.setText("<font color=red>You passed " + str(num_passed) + "/" + str(len(passes)) + " tests")
            image.setGeometry(QRect(object.x(), object.y(), object.width()-100, object.height()))
            font = QFont(object.font().family(), pointSize=24, weight=105)
            font.setBold(True)
            object.setFont(font)
            summary.addWidget(image)
            summary.addWidget(object)
            self.vbox.insertLayout(0, summary)

        self.vbox.addStretch()
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle('Autograder')
        self.show()

        return
    
    def exit_clicked(self):
        self.dialog.close()
        
    def resizeEvent(self, event):
        super().resizeEvent(event)
        for i in range(self.vbox.count()):
              widget = self.vbox.itemAt(i).widget()
              if isinstance(widget, QLabel):
                    widget.setMaximumWidth(self.scroll.viewport().width()-20)
        
def displayWindow(passses, error_msgs, testSets = []):
    app = QApplication(sys.argv)
    window = MainWindow(passses, error_msgs, testSets = [])
    window.show()
    app.exec()
