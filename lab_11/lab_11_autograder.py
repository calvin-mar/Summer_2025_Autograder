# Python imports
import sys
import ast
import astor
import re
import os
import importlib.util

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt, QRect
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

        TIMEOUT = 30 
        b_proceed, s_error_msg = module.syntax_checker(student_submission, TIMEOUT)

        if b_proceed == False:
            object = QLabel("There is a problem with your file.")
            object.setText("<img src='octagon.png' width='32' height='32'><font color=black>" + " There is a problem with your file.  " + s_error_msg + " </font>")
            self.vbox.addWidget(object)
        else:
            specific_student.loader.exec_module(sm)
        ##################################################################################################
        ###end new code
        ##################################################################################################


            ########################################################################
            # Start of tests #######################################################
            ########################################################################

            self.result = []
            # Test 1: Task 1: Test my_len() function with empty list
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                try:
                    result = my_len([])
                except:
                    result = '"Function my_len() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == 0
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_len() should return 0 with an empty list argument, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 2: Task 1: Test my_len() function with list [8, 6, 7, 5, 3]
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_len([8, 6, 7, 5, 3])
                except:
                    result = '"Function my_len() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == 5
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_len() should return 5 with this list [8, 6, 7, 5, 3] as an argument, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ###


            # Test 3: Task 2: Test my_in_list() function with list [8, 6, 7, 5, 3] and integer 0
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_in_list([8, 6, 7, 5, 3], 0)
                except:
                    result = '"Function my_in_list() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_in_list() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == False
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_in_list() should return False with this list [8, 6, 7, 5, 3] and 0 as arguments, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 4: Task 2: Test my_in_list() function with list [8, 6, 7, 5, 3] and integer 8
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_in_list([8, 6, 7, 5, 3], 8)
                except:
                    result = '"Function my_in_list() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_in_list() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == True
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_in_list() should return True with this list [8, 6, 7, 5, 3] and 8 as arguments, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ###

            # Test 5: Task 3: Test my_location() function with list [8, 6, 8, 5, 3] and integer 8
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_location([8, 6, 8, 5, 3], 8)
                except:
                    result = '"Function my_location() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_location() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == 0
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_location() should return 0 with this list [8, 6, 8, 5, 3] and 8 as arguments, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 6: Task 3: Test my_location() function with list [8, 6, 8, 5, 3] and integer 77
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_location([8, 6, 8, 5, 3], 77)
                except:
                    result = '"Function my_location() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_location() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == -1
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_location() should return -1 with this list [8, 6, 8, 5, 3] and 77 as arguments, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            ###
            
            # Test 7: Task 4: Test my_reverse() function with list [8, 6, 77, 5, 3] 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_reverse([8, 6, 77, 5, 3])
                except:
                    result = '"Function my_reverse() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_reverse() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == [3, 5, 77, 6, 8]
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_reverse() should return [3, 5, 77, 6, 8] with this list [8, 6, 7, 5, 3] argument, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1



            ###
            
            # Test 8: Task 5: Test my_extrema() function with list [77, 6, -1, 5, 3] 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_extrema([77, 6, -1, 5, 3])
                except:
                    result = '"Function my_extrema() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_extrema() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == (-1, 77)
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_extrema() should return -1 and 77 with this list [77, 6, -1, 5, 3] argument, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 9: Task 5: Test my_extrema() function with list [-1, 6, 3, 5, 77] 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_extrema([-1, 6, 3, 5, 77])
                except:
                    result = '"Function my_extrema() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_extrema() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == (-1, 77)
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_extrema() should return -1 and 77 with this list [-1, 6, 3, 5, 77] argument, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 10: Task 5: Test my_extrema() function with list [6, 77, 3, 5, -1] 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_extrema([6, 77, 3, 5, -1])
                except:
                    result = '"Function my_extrema() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_extrema() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == (-1, 77)
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_extrema() should return -1 and 77 with this list [6, 77, 3, 5, -1] argument, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            ###

            # Test 11: Task 6: Test my_count() function with list [6, 77, 3, 5, -1] and 99
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_count([6, 77, 3, 5, -1], 99)
                except:
                    result = '"Function my_count() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_count() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == 0
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_count() should return 0 with this list [6, 77, 3, 5, -1] and 99 as argument, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 11: Task 6: Test my_count() function with list [6, 77, 3, 5, 77] and 77
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_count([6, 77, 3, 5, 77], 77)
                except:
                    result = '"Function my_count() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_count() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == 2
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_count() should return 0 with this list [6, 77, 3, 5, 77] and 77 as argument, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ###


            # Test 12: Task 7: Test my_insert() function with list [0, 1, 2, 3, 4], 0, and "X"
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_insert([0, 1, 2, 3, 4], 0, "X")
                except:
                    result = '"Function my_insert() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_insert() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == ["X", 0, 1, 2, 3, 4]
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_insert() should return [\"X\", 0, 1, 2, 3, 4] with this list [0, 1, 2, 3, 4], 0, and \"X\" as argument, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 13: Task 7: Test my_insert() function with list [0, 1, 2, 3, 4], 4, and "X"
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_insert([0, 1, 2, 3, 4], 4, "X")
                except:
                    result = '"Function my_insert() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_insert() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == [0, 1, 2, 3, "X", 4]
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_insert() should return [0, 1, 2, 3, \"X\", 4] with this list [0, 1, 2, 3, 4], 4, and \"X\" as argument, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            ###

            # Test 14: Task 8: Test my_remove() function with list [0, 1, 2, 3, 4, 1, 2, 1, 2], 1
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_remove([0, 1, 2, 3, 4, 1, 2, 1, 2], 1)
                except:
                    result = '"Function my_remove() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_remove() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == [0, 2, 3, 4, 2, 2]
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_remove() should return [0, 2, 3, 4, 2, 2] with this list [0, 1, 2, 3, 4, 1, 2, 1, 2] and 1, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 15: Task 8: Test my_remove() function with list [0, 1, 2, 3, 4, 1, 2, 1, 2], 11
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_remove([0, 1, 2, 3, 4, 1, 2, 1, 2], 11)
                except:
                    result = '"Function my_remove() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_remove() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == [0, 1, 2, 3, 4, 1, 2, 1, 2]
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_remove() should return [0, 1, 2, 3, 4, 1, 2, 1, 2] with this list [0, 1, 2, 3, 4, 1, 2, 1, 2] and 11, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            ###

            # Test 16: Task 9: Test my_sort() function with list [8, 7, 6, 5, 4, 3, 2, 1, 0]
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")           
                try:
                    result = my_sort([8, 7, 6, 5, 4, 3, 2, 1, 0])
                except:
                    result = '"Function my_sort() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function my_sort() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8]
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: my_sort() should return [0, 1, 2, 3, 4, 5, 6, 7, 8] with this list [8, 7, 6, 5, 4, 3, 2, 1, 0], but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            object = QLabel("Summary of Tests")
            object.setWordWrap(True)
            num_passed = 0
            total = 0
            for value in self.result:
                total += 1
                if value:
                    num_passed += 1
            if(total == num_passed):
                object.setText("<img src='check.png' width='32' height='32'><font color=black>CONGRATULATIONS YOU PASSED ALL TESTS!!!</font>")
            else:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>You passed " + str(num_passed) + "/" + str(total) + " tests.</font>")
            self.vbox.insertWidget(0, object)
            
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
        self.setWindowTitle('Lists Big Lab Autograder')
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
	window = MainWindow("lab_11_student_submission.py")
	ret = queue.get()
	ret["result"] = window.result
	window.hide()
	queue.put(ret)
	return

def main():
	app = QApplication(sys.argv)
	window = MainWindow("lab_11_student_submission.py")
	window.show()
	app.exec()
if __name__ == "__main__":
    main()
