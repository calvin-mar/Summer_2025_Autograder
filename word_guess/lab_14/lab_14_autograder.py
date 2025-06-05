# Python imports
import sys
import ast
import astor
import re
import importlib.util
import os

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self, student_submission):
        super().__init__()

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        i_test_num = 1
        print("Autograder starting...")

        dir_path = os.path.dirname(os.path.realpath(__file__))
        specific = importlib.util.spec_from_file_location("syntax_checker_module", os.path.join(dir_path, "syntax_checker_module.py"))
        module = importlib.util.module_from_spec(specific)
        specific.loader.exec_module(module)

        name = student_submission[:-3]
        specific_student = importlib.util.spec_from_file_location(name, os.path.join(dir_path, student_submission))
        sm = importlib.util.module_from_spec(specific_student)


        timeoutAfterXSeconds = 30
        b_proceed, s_error_msg = module.syntax_checker(student_submission, timeoutAfterXSeconds)

        if b_proceed == False:
            object = QLabel("There is a problem with your file.")
            object.setText("<img src='octagon.png' width='32' height='32'><font color=black>" + " There is a problem with your file.  " + s_error_msg + " </font>")
            self.vbox.addWidget(object)
        else:

            specific_student.loader.exec_module(sm)


            ########################################################################
            # Start of tests #######################################################
            ########################################################################

            self.result = []
            
            # Test 1: Task 1: Test my_len() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_len("")
                except:
                    result = '"Function my_len() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == 0
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_len() should return 0 with argument \"\", but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 2: Task 1: Test my_len() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_len("1")
                except:
                    result = '"Function my_len() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == 1
                self.result[i_test_num-1] = True

                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_len() should return 1 with argument \"1\", but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 3: Task 1: Test my_len() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_len("ab")
                except:
                    result = '"Function my_len() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == 2
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_len() should return 2 with argument \"ab\", but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 4: Task 1: Test my_len() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_len("12345678")
                except:
                    result = '"Function my_len() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == 8
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_len() should return 8 with argument \"12345678\", but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ######################

            # Test 5: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip("abc")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "abc"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"abc\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 6: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip("  d  ")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "d"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"space space d space space\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 7: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip("\t\n abc")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "abc"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"tab new_line space abc\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 8: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip("abc\t\t\t\n ")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "abc"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"abc tab tab tab new_line space\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 9: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip("\n\n\n\t   x    \n\n\t")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "x"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"new_line new_line new_line tab space space space x space space space space new_line new_line tab\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 10: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip("  abc  def  ")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "abc  def"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"space space abc space space def space space\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 11: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip("  abc \n\t def  ")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "abc \n\t def"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"space space abc space new_line tab space def space space\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 12: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip("abc\t\n def")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "abc\t\n def"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"abc tab new_line space def\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 13: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip(" \t\n \t\n ")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == ""
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"space tab new_line space tab new_line space\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 14: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip("\n\n\n\n")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == ""
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"new_line new_line new_line new_line\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 15: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip("\t\t\t")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == ""
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"tab tab tab\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 16: Task 2: Test my_strip() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_strip("     ")
                except:
                    result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == ""
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_strip() fails for argument \"space space space space space\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ######################

            # Test 17: Task 3: Test my_in() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_in("abc", "abcdefg")
                except:
                    result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == True
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_in() should return True with arguments abc and abcdefg, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 18: Task 3: Test my_in() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_in("cdefg", "abcdefg")
                except:
                    result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == True
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_in() should return True with arguments abcdefg and cdefg, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1



            # Test 19: Task 3: Test my_in() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_in("ef", "abcdefg")
                except:
                    result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == True
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_in() should return True with arguments ef and abcdefg, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            

            # Test 20: Task 3: Test my_in() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_in("ce", "abcdefg")
                except:
                    result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_in() should return False with arguments ce and abcdefg, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            

            # Test 21: Task 3: Test my_in() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_in("xab", "abcdefg")
                except:
                    result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_in() should return False with arguments xab and abcdefg, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 22: Task 3: Test my_in() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_in("fgh", "abcdefg")
                except:
                    result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_in() should return False with arguments fgh and abcdefg, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1



            # Test 23: Task 3: Test my_in() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_in("x", "abcdefg")
                except:
                    result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_in() should return False with arguments x and abcdefg, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 24: Task 3: Test my_in() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_in("abcdefgx", "abcdefg")
                except:
                    result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_in() should return False with arguments abcdefgx and abcdefg, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1



            ######################

            # Test 25: Task 4: Test my_find() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_find("abc", "abcdefghi")
                except:
                    result = '"Function my_find() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == 0
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_find() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_find() should return 0 with arguments abc and abcdefghi, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 26: Task 4: Test my_find() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_find("ghi", "abcdefghi")
                except:
                    result = '"Function my_find() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == 6
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_find() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_find() should return 6 with arguments ghi and abcdefghi, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 27: Task 4: Test my_find() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_find("cde", "abcdefghi")
                except:
                    result = '"Function my_find() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == 2
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_find() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_find() should return 2 with arguments cde and abcdefghi, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 28: Task 4: Test my_find() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_find("abd", "abcdefghi")
                except:
                    result = '"Function my_find() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == -1
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_find() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_find() should return -1 with arguments abd and abcdefghi, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 29: Task 4: Test my_find() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_find("xyz", "abcdefghi")
                except:
                    result = '"Function my_find() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == -1
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_find() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_find() should return -1 with arguments xyz and abcdefghi, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ######################

            # Test 30: Task 5: Test my_replace() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_replace("fish is good", "fish", "xyz")
                except:
                    result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "xyz is good"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_replace() should return \"xyz is good\" with arguments \"fish is good\", \"fish\", and \"xyz\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 31: Task 5: Test my_replace() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_replace("fish is good", " i", "xyz")
                except:
                    result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "fishxyzs good"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_replace() should return \"fishxyzs good\" with arguments \"fish is good\", \" i\", and \"xyz\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 32: Task 5: Test my_replace() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_replace("fish is good", "goo", "xyz")
                except:
                    result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "fish is xyzd"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_replace() should return \"fish is xyzd\" with arguments \"fish is good\", \"goo\", and \"xyz\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 33: Task 5: Test my_replace() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_replace("fish is good", "od", "axyz")
                except:
                    result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "fish is goaxyz"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_replace() should return \"fish is goaxyz\" with arguments \"fish is good\", \"od\", and \"axyz\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 34: Task 5: Test my_replace() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_replace("fish is good", "h i", "xyz")
                except:
                    result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "fisxyzs good"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_replace() should return \"fisxyzs good\" with arguments \"fish is good\", \"h i\", and \"xyz\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 35: Task 5: Test my_replace() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_replace("fish is good", "x", "xyz")
                except:
                    result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "fish is good"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_replace() should return \"fish is good\" with arguments \"fish is good\", \"x\", and \"xyz\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 36: Task 5: Test my_replace() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_replace("fish is good", " ", "xyz")
                except:
                    result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "fishxyzis good"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_replace() should return \"fishxyzis good\" with arguments \"fish is good\", \" \", and \"xyz\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 37: Task 5: Test my_replace() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_replace("fish is fish", "ish", "xyz")
                except:
                    result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == "fxyz is fish"
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_replace() should return \"fxyz is fish\" with arguments \"fish is fish\", \"ish\", and \"xyz\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ######################

            # Test 38: Task 6: Test my_simple_split() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_simple_split("a", "banana")
                except:
                    result = '"Function my_simple_split() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == ["b", "n", "n", ""]
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_simple_split() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_simple_split(\"a\", \"banana\") should return the list [\"b\", \"n\", \"n\", \"\"].</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 39: Task 6: Test my_simple_split() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_simple_split("a", "anna")
                except:
                    result = '"Function my_simple_split() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == ["", "nn", ""]
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_simple_split() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_simple_split(\"a\", \"anna\") should return the list [\"\", \"nn\", \"\"].</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 40: Task 6: Test my_simple_split() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_simple_split("a", "xaax")
                except:
                    result = '"Function my_simple_split() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == ["x", "", "x"]
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_simple_split() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_simple_split(\"a\", \"xaax\") should return the list [\"x\", \"\", \"x\"].</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 41: Task 6: Test my_simple_split() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_simple_split("a", "xaaax")
                except:
                    result = '"Function my_simple_split() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == ["x", "", "", "x"]
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_simple_split() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_simple_split(\"a\", \"xaaax\") should return the list [\"x\", \"\", \"\", \"x\"].</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 42: Task 6: Test my_simple_split() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.my_simple_split("a", "a")
                except:
                    result = '"Function my_simple_split() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True                
                assert result == ["", ""]
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_simple_split() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_simple_split(\"a\", \"a\") should return the list [\"\", \"\"].</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ######################



            
            ########################################################################
            # End of tests
            ########################################################################

        print("...Autograder completed.")
        print()
        print("You may close the Autograder window to exit.")
        
        self.vbox.addStretch()
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle('Functions Day 2 Autograder')
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


def testing(queue):
	window = MainWindow("lab_14_student_submission.py")
	ret = queue.get()
	ret["result"] = window.result
	window.hide()
	queue.put(ret)
	return
def main():
	app = QApplication(sys.argv)
	window = MainWindow("lab_14_student_submission.py")
	window.show()
	app.exec()
if __name__ == "__main__":
    main()

