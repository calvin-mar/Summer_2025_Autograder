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
            # Test 1: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(lab_10_student_submission.l_first) == 4
                assert lab_10_student_submission.l_first[0] == "A"
                assert lab_10_student_submission.l_first[1] == "B"
                assert lab_10_student_submission.l_first[2] == "C"
                assert lab_10_student_submission.l_first[3] == "D"
                
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_first does not contain the correct values of \"A\", \"B\", \"C\", and \"D\" or it does not have length exactly 4. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 2: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(lab_10_student_submission.l_last) == 3
                assert lab_10_student_submission.l_last[0] == "K"
                assert lab_10_student_submission.l_last[1] == "L"
                assert lab_10_student_submission.l_last[2] == "M"
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_last does not contain the correct values of \"K\", \"L\", and \"M\" or it does not have length exactly 3. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 3: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(lab_10_student_submission.l_mid) == 3
                assert lab_10_student_submission.l_mid[0] == "F"
                assert lab_10_student_submission.l_mid[1] == "G"
                assert lab_10_student_submission.l_mid[2] == "H"
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_last does not contain the correct values of \"F\", \"G\", and \"H\" or it does not have length exactly 3. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 4: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                lab_10_student_submission.l_copy_nums[0] = 5
                lab_10_student_submission.l_copy_nums[1] = 15
                lab_10_student_submission.l_copy_nums[2] = 25
                lab_10_student_submission.l_copy_nums[3] = 35
                lab_10_student_submission.l_copy_nums[4] = 45
                assert len(lab_10_student_submission.l_nums) == 5
                assert len(lab_10_student_submission.l_copy_nums) == 5
                assert lab_10_student_submission.l_nums[0] == 0
                assert lab_10_student_submission.l_nums[1] == 10
                assert lab_10_student_submission.l_nums[2] == 20
                assert lab_10_student_submission.l_nums[3] == 30
                assert lab_10_student_submission.l_nums[4] == 40
                assert lab_10_student_submission.l_copy_nums[0] == 5
                assert lab_10_student_submission.l_copy_nums[1] == 15
                assert lab_10_student_submission.l_copy_nums[2] == 25
                assert lab_10_student_submission.l_copy_nums[3] == 35
                assert lab_10_student_submission.l_copy_nums[4] == 45

                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_copy_nums is not a correct copy of l_nums because overwriting a value in l_copy_nums overwrites a value in l_nums or the length of l_copy_nums is not correct. </font>")

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
        self.setWindowTitle('Lists Part 2 Autograder')
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
	window = MainWindow("lab_10_student_submission.py")
	ret = queue.get()
	ret["result"] = window.result
	window.hide()
	queue.put(ret)
	return

def main():
	app = QApplication(sys.argv)
	window = MainWindow("lab_10_student_submission.py")
	window.show()
	app.exec()
if __name__ == "__main__":
    main()
