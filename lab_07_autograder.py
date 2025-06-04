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
            # Test 1: Task 1: Test double_it() function with 0
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                result = sm.double_it(0)
                assert result == 0
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: double_it() should return 0 with argument 0, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            
            # Test 2: Task 1: Test double_it() function with 13
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                result = sm.double_it(13)
                assert result == 26
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: double_it() should return 26 with argument 13, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 3: Task 1: Test double_it() function with -27
            object = QLabel("Test " + str(i_test_num))
            try:
                result = sm.double_it(-27)
                assert result == -54
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: double_it() should return -54 with argument -27, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ###

            # Test 4: Task 2: Test get_total() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                result = sm.get_total()
                assert result == 73
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: get_total() should return 73 when the user enters 0, -9, 5, 77, -1, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ###

            # Test 5: Task 3: Test calc_avg() function
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                result = sm.calc_avg()
                assert result == 4.333333333333333
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: calc_avg() should return 4.333333333333333 when the user enters 5, 6, 2, -1, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ###

            
            # Test 6: Task 4: Test get_sum() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                try:
                    result = sm.get_sum(5)
                except:
                    result = '"Function get_sum() caused an error.  Try adding some print statements to it to see what is happening!"'
                assert result == 20
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: get_sum() should return 20 when the user calls it with argument 5 and then enters 5, 6, 2, -1, 8, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            ###

            
            # Test 7: Task 5: Test find_smallest() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                try:
                    result = sm.find_smallest(5)
                except:
                    result = '"Function find_smallest() caused an error.  Try adding some print statements to it to see what is happening!"'
                assert result == 40
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: find_smallest() should return 40 when the user calls it with argument 5 and then enters 100, 50, 60, 40, 70, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            ###

            
            # Test 8: Task 6: Test count_num_fives() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                try:
                    result = sm.count_num_fives(10)
                except:
                    result = '"Function count_num_fives() caused an error.  Try adding some print statements to it to see what is happening!"'
                assert result == 3
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: count_num_fives() should return 3 when the user calls it with argument 10 and then enters 100, 5, 60, 5, 70, 1, 6, 5, 4, 77 but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            ###

            
            # Test 9: Task 7: Test convert_euros_to_dollars() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                try:
                    result = sm.convert_dollars_to_euros()
                except:
                    result = '"Function convert_dollars_to_euros() caused an error.  Try adding some print statements to it to see what is happening!"'
                assert result == 2.5*.89
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: convert_dollars_to_euros() should return 2.225 when the user enters 2.5 but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            ###

            
            # Test 10: Task 8: Test is_even() function with even number argument
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                try:
                    result = sm.is_even(22)
                except:
                    result = '"Function is_even() caused an error.  Try adding some print statements to it to see what is happening!"'
                assert result == True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: is_even() should return True when the user enters 22 but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ###

            # Test 11: Task 8: Test is_even() function with odd number argument
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                try:
                    result = sm.is_even(21)
                except:
                    result = '"Function is_even() caused an error.  Try adding some print statements to it to see what is happening!"'
                assert result == False
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: is_even() should return False when the user enters 21 but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            ###

            # Test 12: Task 9: Test count_evens() function with args of smaller, larger
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                try:
                    result = sm.count_evens(2, 8)
                except:
                    result = '"Function count_evens() caused an error.  Try adding some print statements to it to see what is happening!"'
                assert result == 2
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: count_evens() should return 2 when the arguments are 2 and 8, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 13: Task 9: Test count_evens() function with args of larger, smaller
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                try:
                    result = sm.count_evens(8, 2)
                except:
                    result = '"Function count_evens() caused an error.  Try adding some print statements to it to see what is happening!"'
                assert result == 2
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: count_evens() should return 2 when the arguments are 8 and 2, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 14: Task 10: Test temp_monitor() function with arg 60.5 which returns the wrong value until the function is fixed
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                try:
                    result = sm.temp_monitor(60.5)
                except:
                    result = '"Function temp_monitor() caused an error.  Try adding some print statements to it to see what is happening!"'
                assert result == "pleasant"
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: temp_monitor() should return pleasant for argument 60.5.</font>")

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
        self.setWindowTitle('Debugging & Testing Autograder')
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
	window = MainWindow("lab_07_student_submission.py")
	ret = queue.get()
	ret["result"] = window.result
	window.hide()
	queue.put(ret)
	return

def main():
	app = QApplication(sys.argv)
	window = MainWindow("lab_07_student_submission.py")
	window.show()
	app.exec()
if __name__ == "__main__":
    main()
