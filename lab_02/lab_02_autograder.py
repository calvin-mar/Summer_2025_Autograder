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
            object.setWordWrap(True) 
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
                assert sm.f_temp_fahr == (9/5) * sm.f_celsius + 32
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Temperature Conversions Passed </font>")
                self.result[i_test_num-1] = True
            except:
                try:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Temperature Conversions Failed: " + str(sm.f_celsius) + " degrees Celsius should equal " + str(((9/5) * lab_02_studentsub.f_celsius + 32)) + " degrees Fahrenheit but your code has it equal " + str(lab_02_studentsub.f_temp_fahr) + " degrees Fahrenheit.  Make sure your variables are named correctly if your value is correct.</font>")
                except:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Temperature Conversions Failed: variables are not named correctly or have incorrect values.</font>")


            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 2: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                assert sm.f_distance_km == (sm.f_miles / 3.1) * 5
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Distance Conversions Passed </font>")
                self.result[i_test_num-1] = True
            except:
                try:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Distance Conversions Failed: " + str(sm.f_miles) + " miles should equal " + str((lab_02_studentsub.f_miles / 3.1) * 5) + " kilometers but your code has it equal " + str(lab_02_studentsub.f_distance_km) + " kilometers.  Make sure your variables are named correctly if your value is correct.</font>")
                except:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Distance Conversions Failed: variables are not named correctly or have incorrect values.</font>")
                    

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 3: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:
                f_small_area = 3.14 * 6 ** 2
                f_med_area = 3.14 * 8 ** 2
                f_large_area = 3.14 * 9 ** 2
                f_small_cost = 8 / f_small_area
                f_med_cost = 12 / f_med_area
                f_large_cost = 16 / f_large_area

                assert sm.f_small_area == f_small_area
                assert sm.f_med_area == f_med_area
                assert sm.f_large_area == f_large_area
                assert sm.f_small_cost == f_small_cost
                assert sm.f_med_cost == f_med_cost
                assert sm.f_large_cost == f_large_cost
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Pizza Data Passed </font>")
                self.result[i_test_num-1] = True
            except:
                try:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Pizza Data Failed: Areas should be S: " + str(f_small_area) + ", M: " + str(f_med_area) + ", L: " + str(f_large_area) + " and costs should be S: " + str(f_small_cost) + ", M: " + str(f_med_cost) + ", L: " + str(f_large_cost) + ". Make sure your variables are named correctly if your values are correct.</font>")
                except:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Pizza Data Failed: variables are not named correctly or have incorrect values.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            # Test 4: 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            try:

                i_roll_packs = i_people // 12 + 1
                i_soda_packs = (2 * i_people) // 12 + 1
                i_hot_dog_packs = i_people // 8 + 1
                i_chip_boxes = i_people // 16 + 1

                i_rem_rolls = (i_roll_packs * 12) - i_people
                i_rem_sodas = (i_soda_packs * 12) - (i_people * 2)
                i_rem_hot_dogs = (i_hot_dog_packs * 8) - i_people
                i_rem_chips = (i_chip_boxes * 16) - i_people
                
                assert sm.i_roll_packs == i_roll_packs
                assert sm.i_soda_packs == i_soda_packs
                assert sm.i_hot_dog_packs == i_hot_dog_packs
                assert sm.i_chip_boxes == i_chip_boxes
                assert sm.i_rem_rolls == i_rem_rolls
                assert sm.i_rem_sodas == i_rem_sodas
                assert sm.i_rem_hot_dogs == i_rem_hot_dogs
                assert sm.i_rem_chips == i_rem_chips
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Olympics Party Passed </font>")
                self.result[i_test_num-1] = True
            except:
                try:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Olympics Party Failed: For " + str(sm.i_people) + " people, the values should be " + str(i_roll_packs) + " roll packs, "  + str(i_soda_packs) + " soda packs, "  + str(i_hot_dog_packs) + " hot dog packs, "  + str(i_chip_boxes) + " chip boxes.  There should be the following items left over: "  + str(i_rem_rolls) + " rolls, "  + str(i_rem_sodas) + " sodas, "  + str(i_rem_hot_dogs) + " hot dogs, and "  + str(i_rem_chips) + " bags of chips.  Make sure your variables are named correctly if your values are correct.</font>")
                except:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Question " + str(i_test_num) + " Olympics Party Failed: variables are not named correctly or have incorrect values.</font>")


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
	window = MainWindow("lab_02_student_submission.py")
	ret = queue.get()
	ret["result"] = window.result
	window.hide()
	queue.put(ret)
	return

def main():
	app = QApplication(sys.argv)
	window = MainWindow("lab_02_student_submission.py")
	window.show()
	app.exec()
if __name__ == "__main__":
    main()
