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
            ########################################################################
            # Start of tests #######################################################
            ########################################################################
            self.result = []

            # Test 1: Task 1: Test get_estimate() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.get_estimate()
                except:
                    result = "Function get_estimate() crashed or is not defined"
                    error_calling_function = True                
                assert result == 252
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function get_estimate() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: get_estimate() should return 252 when the user enters s:1, m:2, l:3, xl:4, xxl:5, xxxl:6.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1




            # Test 2: Task 1: Test get_quantities() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.get_quantities()
                except:
                    result = "Function get_quantities() crashed or is not defined"
                    error_calling_function = True                
                assert result == (1, 2, 3, 4, 5, 6)
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function get_quantities() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: get_quantities() should return 1, 2, 3, 4, 5, 6 when the user enters s:1, m:2, l:3, xl:4, xxl:5, xxxl:6.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ######################

            # Test 3: Task 2: Test validate_combination() function with valid data
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_combination(12, 33, 0)
                except:
                    result = "Function validate_combination() crashed or is not defined"
                    error_calling_function = True                
                assert result == True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return True when given 3 valid numbers like 12, 33, 0.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1



            # Test 4: Task 2: Test validate_combination() function with invalid data: first number below 0
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_combination(-1, 33, 0)
                except:
                    result = "Function validate_combination() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with first number &#60; 0.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1




            # Test 5: Task 2: Test validate_combination() function with invalid data: second number below 0
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_combination(33, -1, 0)
                except:
                    result = "Function validate_combination() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with second number &#60; 0.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1




            # Test 6: Task 2: Test validate_combination() function with invalid data: third number below 0
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_combination(12, 33, -1)
                except:
                    result = "Function validate_combination() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with third number &#60; 0.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 7: Task 2: Test validate_combination() function with invalid data: first number above 39
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_combination(40, 33, 0)
                except:
                    result = "Function validate_combination() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with first number > 39.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1




            # Test 8: Task 2: Test validate_combination() function with invalid data: second number above 39
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_combination(1, 40, 0)
                except:
                    result = "Function validate_combination() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with second number > 39.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1




            # Test 9: Task 2: Test validate_combination() function with invalid data: third number above 39
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_combination(20, 33, 40)
                except:
                    result = "Function validate_combination() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with third number > 39.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1



            # Test 10: Task 2: Test validate_combination() function with invalid data: first number same as second number
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_combination(33, 33, 0)
                except:
                    result = "Function validate_combination() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with the same first and second numbers.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1



            # Test 11: Task 2: Test validate_combination() function with invalid data: second number same as third number
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_combination(0, 33, 33)
                except:
                    result = "Function validate_combination() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with the same second and third numbers.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            #####################

            # Test 12: Task 3: Test order_combo_meal() function with valid data
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                try:
                    result = sm.order_combo_meal(1, 2, 4)
                except:
                    result = "Function order_combo_meal() crashed or is not defined"
                    error_calling_function = True                                
                assert result == (8.97, True)
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function order_combo_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: order_combo_meal() should return 8.97 and True when given a sandwich, side, and drink with values of 1, 2, and 4 respectively.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 13: Task 3: Test order_combo_meal() function with invalid data: invalid sandwich < 1
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.order_combo_meal(0, 1, 1)
                except:
                    result = "Function order_combo_meal() crashed or is not defined"
                    error_calling_function = True                                
                assert result == (2.99, False)
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function order_combo_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: order_combo_meal() should return 2.99 and False when given a side and drink with values of 1 and a sandwich with a value of 0.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 14: Task 3: Test order_combo_meal() function with invalid data: invalid side < 1
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.order_combo_meal(1, 0, 1)
                except:
                    result = "Function order_combo_meal() crashed or is not defined"
                    error_calling_function = True                                
                assert result == (2.99, False)
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function order_combo_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: order_combo_meal() should return 2.99 and False when given a sandwich and drink with values of 1 and a side with a value of 0.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 15: Task 3: Test order_combo_meal() function with invalid data: invalid drink < 1
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.order_combo_meal(1, 1, 0)
                except:
                    result = "Function order_combo_meal() crashed or is not defined"
                    error_calling_function = True                                
                assert result == (3.98, False)
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function order_combo_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: order_combo_meal() should return 3.98 and False when given a sandwich and side with values of 1 and a drink with a value of 0.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 16: Task 3: Test get_item_price() function with valid data
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.get_item_price("drink", 4)
                except:
                    result = "Function get_item_price() crashed or is not defined"
                    error_calling_function = True                                
                assert result == 3.99
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function get_item_price() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: get_item_price() should return 3.99 when given a drink with a value of 4.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 17: Task 3: Test get_item_price() function with invalid data: invalid item name < 1
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.get_item_price("sandwich", -1)
                except:
                    result = "Function get_item_price() crashed or is not defined"
                    error_calling_function = True                                
                assert result == 0.0
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function get_item_price() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: get_item_price() should return 0.0 when given a sandwich with a value of -1.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 18: Task 3: Test get_item_price() function with invalid data: invalid item number > 4
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.get_item_price("sandwich", 5)
                except:
                    result = "Function get_item_price() crashed or is not defined"
                    error_calling_function = True                                
                assert result == 0.0
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function get_item_price() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: get_item_price() should return 0.0 when given a sandwich with a value of 5.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 19: Task 3: Test validate_meal() function with valid data
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_meal(1, 1, 1)
                except:
                    result = "Function validate_meal() crashed or is not defined"
                    error_calling_function = True                                
                assert result == True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return True when given a sandwich, side, and drink all with values of 1.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 20: Task 3: Test validate_meal() function with invalid data: invalid sandwich < 1
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_meal(0, 1, 1)
                except:
                    result = "Function validate_meal() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a sandwich with a value of 0.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 21: Task 3: Test validate_meal() function with invalid data: invalid side < 1
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_meal(1, 0, 1)
                except:
                    result = "Function validate_meal() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a side with a value of 0.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 22: Task 3: Test validate_meal() function with invalid data: invalid drink < 1
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_meal(1, 1, 0)
                except:
                    result = "Function validate_meal() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a drink with a value of 0.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 23: Task 3: Test validate_meal() function with invalid data: invalid sandwich > 3
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_meal(4, 1, 1)
                except:
                    result = "Function validate_meal() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a sandwich with a value of 4.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 24: Task 3: Test validate_meal() function with invalid data: invalid side > 2
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_meal(1, 3, 1)
                except:
                    result = "Function validate_meal() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a side with a value of 3.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 25: Task 3: Test validate_meal() function with invalid data: invalid drink > 4
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.validate_meal(1, 1, 5)
                except:
                    result = "Function validate_meal() crashed or is not defined"
                    error_calling_function = True                                
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a drink with a value of 5.</font>")

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
        self.setWindowTitle('Functions Lab 2 Autograder')
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
	window = MainWindow("lab_05_student_submission.py")
	ret = queue.get()
	ret["result"] = window.result
	window.hide()
	queue.put(ret)
	return
def main():
	app = QApplication(sys.argv)
	window = MainWindow("lab_05_student_submission.py")
	window.show()
	app.exec()
if __name__ == "__main__":
    main()
