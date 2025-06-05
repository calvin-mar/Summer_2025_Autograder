# Python imports
import sys
import ast
import astor
import re
import os
import importlib.util

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from layout_colorwidget import Color

# Data file import
import csc170_strings_data
from csc170_strings_data import *


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
        ##################################################################################################
        ###end new code
        ##################################################################################################


            ########################################################################
            # Start of tests #######################################################
            ########################################################################

            s_task_1_data = csc170_strings_data.get_q1_string()
            s_task_2_data = csc170_strings_data.get_q2_string()
            s_task_3_A_data, s_task_3_B_data = csc170_strings_data.get_q3_string()
            s_task_4_data = csc170_strings_data.get_q4_string()
            s_task_5_data = csc170_strings_data.get_q5_string()
            s_task_6_data = csc170_strings_data.get_q6_string()
            s_task_7_data = csc170_strings_data.get_q7_string()
            s_task_9_data_A, s_task_9_data_B = csc170_strings_data.get_q9_string()
            s_task_12_data = csc170_strings_data.get_q12_string()
            s_task_13_data = csc170_strings_data.get_q13_string()
            s_task_14_data = csc170_strings_data.get_q14_string()
            s_task_15_data = csc170_strings_data.get_q15_string()
            s_task_16_data = csc170_strings_data.get_q16_string()
            s_task_17_A_data, s_task_17_B_data = csc170_strings_data.get_q17_string()
            s_task_18_data = csc170_strings_data.get_q18_string()
            s_task_19_data = csc170_strings_data.get_q19_string()
            s_task_20_data = csc170_strings_data.get_q20_string()
            s_task_23_data = csc170_strings_data.get_q23_string()
            s_task_24_data = csc170_strings_data.get_q24_string()
            s_task_25_A_data, s_task_25_B_data = csc170_strings_data.get_q25_string()
            s_task_26_data = csc170_strings_data.get_q26_string()
            s_task_27_data = csc170_strings_data.get_q27_string()
            

            self.result = []
            # Test 1: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            
            try:
                assert sm.i_task_1 == len(s_task_1_data)
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_1 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            
            # Test 2: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.s_task_2 == s_task_2_data[6]
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_2 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 3: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.b_task_3 == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_3 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 4: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.s_task_4 == s_task_4_data.strip()
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_4 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 5: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.b_task_5 == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_7 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 6: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.b_task_6 == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_6 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 7: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.l_task_7 == s_task_7_data.split(":")
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable l_task_7 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 8: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.i_task_8_start == 5 
                assert sm.i_task_8_stop == 10
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_8_start and i_task_8_stop exist and have the correct values. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 9: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.s_task_9 == s_task_9_data_A + s_task_9_data_B
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_9 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 10: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                l_tmp = s_task_7_data.split(":")
                l_tmp.reverse()
                tmp_str = ""
                for word in l_tmp:
                    tmp_str = tmp_str + word
                
                assert lab_12_student_submission.s_task_10 == tmp_str
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_10 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 11: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.i_task_11_end == 6
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_11 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 12: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.b_task_12 == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_12 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 13: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.b_task_13 == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_13 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 14: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.i_task_14 == len(s_task_14_data)
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_14 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 15: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.s_task_15 == s_task_15_data[1]
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_15 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 16: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.b_task_16 == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_16 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 17: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert lab_12_student_submission.b_task_17 == True
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_17 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 18: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.b_task_18 == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_18 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 19: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.s_task_19 == s_task_19_data.strip()
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_19 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 20: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.l_task_20 == s_task_20_data.split(", ")
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable l_task_20 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 21: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.i_task_21_start == 4
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_21 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 22: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                l_tmp = s_task_7_data.split(":")
                tmp_str = ""
                for word in l_tmp:
                    tmp_str = tmp_str + word
             
                assert sm.s_task_22 == tmp_str
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_22 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 23: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.i_task_23 == len(s_task_23_data)
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_23 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 24: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert lab_12_student_submission.s_task_24 == s_task_24_data.strip()
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable 2_task_24 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 25: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.b_task_25 == False
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_25 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 26: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.s_task_26 == s_task_26_data[3]
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_26 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 27: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                l_tmp = s_task_27_data.split("ball")
                        
                assert sm.l_task_27 == l_tmp
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable l_task_27 exists and has the correct value. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            
            


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
        self.setWindowTitle('Strings Part 1 Autograder')
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
	window = MainWindow("lab_12_student_submission.py")
	ret = queue.get()
	ret["result"] = window.result
	window.hide()
	queue.put(ret)
	return
def main():
	app = QApplication(sys.argv)
	window = MainWindow("lab_12_student_submission.py")
	window.show()
	app.exec()
if __name__ == "__main__":
    main()
