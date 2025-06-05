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
                assert len(sm.l_cities) == 0
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_cities is not empty or does not exist. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 2: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(sm.l_miles) == 4
                assert sm.l_miles[0] == 3.1
                assert sm.l_miles[1] == 6.2
                assert sm.l_miles[2] == 13.1
                assert sm.l_miles[3] == 26.2
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_miles does not contain precisely 3.1, 6.2, 13.1, 26.2 in that order or else it also contains additional values.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 3: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.f_third == 26.2
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Variable f_third doesn't hold the value 26.2. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 4: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(sm.l_states) == 4
                assert sm.l_states[0] == "MA"
                assert sm.l_states[1] == "IN"
                assert sm.l_states[2] == "TN"
                assert sm.l_states[3] == "WV"
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_states does not contain precisely \"MA\", \"IN\", \"TN\", and \"WV\" in that order or else it also contains additional values. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 5: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.s_state == "IN"
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: Variable s_state doesn't hold the value \"IN\". </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 6: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(sm.l_countries) == 5
                assert sm.l_countries[0] == "US"
                assert sm.l_countries[1] == "Japan"
                assert sm.l_countries[2] == "Brazil"
                assert sm.l_countries[3] == "Mexico"
                assert sm.l_countries[4] == "Canada"
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_countries does not contain precisely \"US\", \"Japan\", \"Brazil\", \"Mexico\", \"Canada\" in that order or else it also contains additional values. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 7: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(sm.l_cars) == 6
                assert sm.l_cars[0] == "Ferrari"
                assert sm.l_cars[1] == "Sonata"
                assert sm.l_cars[2] == "Bug"
                assert sm.l_cars[3] == "Rio"
                assert sm.l_cars[4] == "Corolla"
                assert sm.l_cars[5] == "Maserati"
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_cars does not contain precisely \"Ferrari\", \"Sonata\", \"Bug\", \"Rio\", \"Corolla\", \"Maserati\" in that order or else it also contains additional values. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 8: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(sm.l_names) == 8
                assert sm.l_names[0] == "Suzanne"
                assert sm.l_names[1] == "Alvin"
                assert sm.l_names[2] == "Simon"
                assert sm.l_names[3] == "Theodore"
                assert sm.l_names[4] == "Dave"
                assert sm.l_names[5] == "Brittany"
                assert sm.l_names[6] == "Jeanette"
                assert sm.l_names[7] == "Eleanor"
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_names does not contain the correct number of items or the correct items. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 9: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(sm.l_names2) == 8
                assert sm.l_names2[0] == "Suzanne"
                assert sm.l_names2[1] == "Billy"
                assert sm.l_names2[2] == "Alvin"
                assert sm.l_names2[3] == "Simon"
                assert sm.l_names2[4] == "Dave"
                assert sm.l_names2[5] == "Brittany"
                assert sm.l_names2[6] == "Jeanette"
                assert sm.l_names2[7] == "Eleanor"
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_names does not contain the correct number of items or the correct items. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 10: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(sm.l_names2) == 8
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: The value of i_num_names is not correct. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 11: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.b_camry_present == False
                assert sm.b_sonata_present == True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: b_camry_present and/or b_sonata_present is incorrect. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 12: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.i_suzy_location == -1
                assert sm.i_dave_location == 4
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: i_suzy_location and/or i_dave_location is incorrect. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 13: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(sm.l_grades) == 4
                assert sm.l_grades[0] == 102
                assert sm.l_grades[1] == 52
                assert sm.l_grades[2] == 79
                assert sm.l_grades[3] == 34
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_grades does not contain precisely the values returned by the function call all increased by 2. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 14: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(sm.l_grades2) == 4
                assert sm.l_grades2[0] == 32
                assert sm.l_grades2[1] == 50
                assert sm.l_grades2[2] == 77
                assert sm.l_grades2[3] == 100
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_grades2 is not sorted from low to high or contains the wrong number of grades (should be 4). </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 15: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert len(sm.l_grades3) == 4
                assert sm.l_grades3[0] == 100
                assert sm.l_grades3[1] == 77
                assert sm.l_grades3[2] == 50
                assert sm.l_grades3[3] == 32
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: List l_grades3 is not sorted from high to low or contains the wrong number of grades (should be 4). </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 16: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.i_biggest == 100
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: i_biggest is not the biggest value in the list l_grades. </font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 17: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.i_smallest == 32
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Failed: i_smallest is not the smallest value in the list l_grades. </font>")

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
        self.setWindowTitle('Lists Part 1 Autograder')
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
	window = MainWindow("lab_09_student_submission.py")
	ret = queue.get()
	ret["result"] = window.result
	window.hide()
	queue.put(ret)
	return

def main():
	app = QApplication(sys.argv)
	window = MainWindow("lab_09_student_submission.py")
	window.show()
	app.exec()
if __name__ == "__main__":
    main()
