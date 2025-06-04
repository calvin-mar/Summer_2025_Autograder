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
            # Test 1: Task 1: Test biggest_smallest_number() function with biggest in 1st position and smallest in 6th position
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.biggest_smallest_number()
                except:
                    result = '"Function biggest_smallest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == (100, 10)
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function biggest_smallest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: biggest_smallest_number() should return 100 and 10 when the user enters 100, 80, 30, 90, 20, 10, 50, 40, 70, 60, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            
            # Test 2: Task 1: Test biggest_smallest_number() function with biggest in 10th (last) position and smallest in 1st position
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.biggest_smallest_number()
                except:
                    result = '"Function biggest_smallest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == (100, 10)
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function biggest_smallest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: biggest_smallest_number() should return 100 and 10 when the user enters 50, 20, 80, 40, 10, 70, 90, 60, 30, 100, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 3: Task 1: Test biggest_smallest_number() function with biggest in 5th position and smallest in 10th (last) position
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.biggest_smallest_number()
                except:
                    result = '"Function biggest_smallest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == (100, 10)
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function biggest_smallest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: biggest_smallest_number() should return 100 and 10 when the user enters 40, 70, 30, 80, 100, 90, 60, 10, 20, 50, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 4: Task 1: Test biggest_smallest_number() function with biggest in 5th position and smallest in 3rd position but all numbers are negative
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.biggest_smallest_number()
                except:
                    result = '"Function biggest_smallest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == (-10, -100)
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function biggest_smallest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: biggest_smallest_number() should return -10 and -100 when the user enters -50, -80, -100, -30, -10, -20, -70, -90, -60, -40, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1
            
            ######################

            
            # Test 5: Task 2: Test repeated_doubler() function - double 5 4 times
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.repeated_doubler(5, 4)
                except:
                    result = '"Function repeated_doubler() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == 80
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function repeated_doubler() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: repeated_doubler() should return 80 when the arguments are 5 and 4, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 6: Task 2: Test repeated_doubler() function - double 0 3 times
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.repeated_doubler(0, 3)
                except:
                    result = '"Function repeated_doubler() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == 0
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function repeated_doubler() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: repeated_doubler() should return 0 when the arguments are 0 and 3, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ######################
            

            # Test 7: Task 3: Test fib_num() function - 1st fib is 0
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.fib_num(1)
                except:
                    result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == 0
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 0 when the argument is 1, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 8: Task 3: Test fib_num() function - 2nd fib is 1
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.fib_num(2)
                except:
                    result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == 1
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 1 when the argument is 2, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 9: Task 3: Test fib_num() function - 3rd fib is 1
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.fib_num(3)
                except:
                    result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == 1
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 1 when the argument is 3, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 10: Task 3: Test fib_num() function - 4th fib is 2
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.fib_num(4)
                except:
                    result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == 2
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 2 when the argument is 4, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 11: Task 3: Test fib_num() function - 9th fib is 21
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.fib_num(9)
                except:
                    result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == 21
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 21 when the argument is 9, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 12: Task 3: Test fib_num() function - 16th fib is 610
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.fib_num(16)
                except:
                    result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == 610
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 610 when the argument is 16, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1
            

            ######################
            # Test 13: Task 4: Test leaf_sum() function with argument 4 for 4 days with values of 1, 2, 3, 4 for a total of 10 leaves
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.leaf_sum(4)
                except:
                    result = '"Function leaf_sum() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == 10
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function leaf_sum() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: leaf_sum() should return 10 when the argument is 4 and values entered are 1, 2, 3 and 4, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            
            ######################

            # Test 14: Task 5: Test class_leaf_sum() function with argument 3 for 3 students.  This will then call leaf sum for each student.  Student 1: 2 days, 9 + 8 leaves.  Student 2: 3 days, 1 + 1 + 1 leaves.  Student 3: 4 days, 4 +5 + 6 + 5 leaves.  Total 40 leaves.
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.class_leaf_sum(3)
                except:
                    result = '"Function class_leaf_sum() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == 40
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function class_leaf_sum() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: class_leaf_sum() should return 40 when the argument is 3 and values entered are (Student 1: 2 days, 9 + 8 leaves.  Student 2: 3 days, 1 + 1 + 1 leaves.  Student 3: 4 days, 4 +5 + 6 + 5 leaves), but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ######################

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
        self.setWindowTitle('For Loops Autograder')
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
	window = MainWindow("lab_08_student_submission.py")
	ret = queue.get()
	ret["result"] = window.result
	window.hide()
	queue.put(ret)
	return

def main():
	app = QApplication(sys.argv)
	window = MainWindow("lab_08_student_submission.py")
	window.show()
	app.exec()
if __name__ == "__main__":
    main()
