# Python imports
import sys
import math
import ast
import astor
import re
import importlib.util
import os

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from layout_colorwidget import Color

import lab_15_diff

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

            # Test 1: Test get_data() function with test_file.txt file
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                try:
                    result = sm.get_data("test_file.txt")
                except:
                    result = '"Function get_data() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function get_data() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == ["This is line 1 of the test file!", "This is line 2 of the test file!", "Line 3 of the data file.", "I love computer science!", "I love dogs!"]
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: get_data(\"test_file.txt\") should return [\"This is line 1 of the test file!\", \"This is line 2 of the test file!\", \"Line 3 of the data file.\", \"I love computer science!\", \"I love dogs!\"], but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1



            # Test 2: Test count_item_records() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                try:
                    result = sm.count_item_records("student", ["John", "student", "student_id_123", "Dave", "faculty", "faculty_id_151", "Suzy", "student", "student_id_563"])
                except:
                    result = '"Function count_item_records() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function count_item_records() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == 2
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: count_item_records(\"student\", [\"John\", \"student\", \"student_id_123\", \"Dave\", \"faculty\", \"faculty_id_151\", \"Suzy\", \"student\", \"student_id_563\"]) should return 2, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 3: Test count_item_records() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                try:
                    result = sm.count_item_records("faculty", ["John Harney", "faculty", "faculty_id_123", "John Doe", "faculty", "faculty_id_151", "Bruce Johnson", "faculty", "faculty_id_563", "John Ac", "staff", "staff_id_15632", "Ilike Badjokes", "faculty", "faculty_id_542151", "Ima Plumber", "staff", "staff_id_5653"])
                except:
                    result = '"Function count_item_records() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function count_item_records() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == 4
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: count_item_records(\"student\", [\"John Harney\", \"faculty\", \"faculty_id_123\", \"John Doe\", \"faculty\", \"faculty_id_151\", \"Bruce Johnson\", \"faculty\", \"faculty_id_563\", \"John Ac\", \"staff\", \"staff_id_15632\", \"Ilike Badjokes\", \"faculty\", \"faculty_id_542151\", \"Ima Plumber\", \"staff\", \"staff_id_5653\"]) should return 2, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1



            # Test 4: Test count_csv_records() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                try:
                    result = sm.count_csv_records("faculty", ["John Harney,faculty,faculty_id_123","John Doe,faculty,faculty_id_151","Bruce Johnson,faculty,faculty_id_563","John Ac,staff,staff_id_15632","Ilike Badjokes,faculty,faculty_id_542151","Ima Plumber,staff,staff_id_5653"])
                except:
                    result = '"Function count_csv_records() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function count_csv_records() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                assert result == 4
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: count_csv_records(\"faculty\", [\"John Harney,faculty,faculty_id_123\", \"John Doe,faculty,faculty_id_151\", \"Bruce Johnson,faculty,faculty_id_563\", \"John Ac,staff,staff_id_15632\", \"Ilike Badjokes,faculty,faculty_id_542151\", \"Ima Plumber\", \"staff\", \"staff_id_5653\"]) should return 4, but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 5: Test make_data_file() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                try:
                    result = sm.make_data_file("sample_file3.txt", ["John Harney","faculty","faculty_id_123","John Doe","faculty","faculty_id_151","Bruce Johnson","faculty","faculty_id_563","John Ac","staff","staff_id_15632","Ilike Badjokes","faculty","faculty_id_542151","Ima Plumber","staff","staff_id_5653"])
                except:
                    result = '"Function make_data_file() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function make_data_file() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")

                l_data = ["John Harney","faculty","faculty_id_123","John Doe","faculty","faculty_id_151","Bruce Johnson","faculty","faculty_id_563","John Ac","staff","staff_id_15632","Ilike Badjokes","faculty","faculty_id_542151","Ima Plumber","staff","staff_id_5653"]
                output_file = open("correct_file3.txt", "w")
                for index in range(len(l_data) -1):
                    output_file.write(l_data[index] + "\n")
                output_file.write(l_data[len(l_data) -1])
                output_file.close()

                diff_result = lab_15_diff.diff("sample_file3.txt", "correct_file3.txt")
                NO_DIFFS = 0
                assert diff_result == NO_DIFFS
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function make_data_file() produced an incorrect file.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1



            # Test 6: Test make_data_csv_file() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                try:
                    result = sm.make_data_csv_file("sample_file.txt", 3, ["John Harney","faculty","faculty_id_123","John Doe","faculty","faculty_id_151","Bruce Johnson","faculty","faculty_id_563","John Ac","staff","staff_id_15632","Ilike Badjokes","faculty","faculty_id_542151","Ima Plumber","staff","staff_id_5653"])
                except:
                    result = '"Function make_data_csv_file() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function make_data_csv_file() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                diff_result = lab_15_diff.diff("sample_file.txt", "correct_file.txt")
                NO_DIFFS = 0
                assert diff_result == NO_DIFFS
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function make_data_csv_file() produced an incorrect file.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1

            
            # Test 7: Test append_to_file() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error = ""
            error_code = "none"
            try:
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                try:
                    output_file = open("sample_file2.txt", "w")
                    output_file.write("ImaTestFile")
                    output_file.close()
                    result = sm.append_to_file("sample_file2.txt", ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"])
                except:
                    result = '"Function get_data() crashed with an error!"'
                    error_code = "crash"
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function append_to_file() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
                diff_result = lab_15_diff.diff("sample_file2.txt", "correct_file2.txt")
                NO_DIFFS = 0
                assert diff_result == NO_DIFFS
                self.result[i_test_num-1] = True
            except:
                if error_code != "crash":
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function append_to_file() produced an incorrect file.  Look at the file sample_file2.txt to see what was produced.  Look at the file example.txt to see a copy of the file that was appended to.</font>")

            i_test_num = i_test_num + 1
            
            self.vbox.insertWidget(0, object)
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
        self.setWindowTitle('File I/O Lab 15 Autograder')
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
	window = MainWindow("lab_15_student_submission.py")
	ret = queue.get()
	ret["result"] = window.result
	window.hide()
	queue.put(ret)
	return
def main():
	app = QApplication(sys.argv)
	window = MainWindow("lab_15_student_submission.py")
	window.show()
	app.exec()
if __name__ == "__main__":
    main()
