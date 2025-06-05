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


from dave_utilities import *
import dave_utilities

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

            # Test 1: Task 1: Test load_misspellings() function
            test_dict = {"doofis":"doofus", "gote":"goat", "miztake":"mistake", "l8":"late", "kat":"cat"}
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.load_misspellings()
                except:
                    result = '"Function load_misspellings() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert dave_utilities.compare_dicts(result, test_dict) == True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function load_misspellings() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: load_misspellings() should return " + str(test_dict) + " but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1



            # Test 2: Task 1: Test fix_misspellings() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            s_text = ""
            error_calling_function = False
            try:
                try:
                    result = sm.fix_misspellings(test_dict)
                except:
                    result = '"Function fix_misspellings() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == "when i am late getting home my goat doofus may make a mistake and eat my cat this keeps mee from getting home late all the time becuz i love my goat and dont want him to get a hairball from eating my cat"
                s_text = result          
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function fix_misspellings() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: fix_misspellings() should return \"when i am late getting home my goat doofus may make a mistake and eat my cat this keeps mee from getting home late all the time becuz i love my goat and dont want him to get a hairball from eating my cat\", but it returns \"" + str(result) + "\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 3: Task 1: Test word_count() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            test_dict2 = {}
            s_text = "when i am late getting home my goat doofus may make a mistake and eat my cat this keeps mee from getting home late all the time becuz i love my goat and dont want him to get a hairball from eating my cat"
            l_words = s_text.split(" ")
            for word in l_words:
                if word in test_dict2.keys():
                    test_dict2[word] = test_dict2[word] + 1
                    
                else:
                    test_dict2[word] = 1
            error_calling_function = False
            try:
                try:
                    result = sm.word_count(s_text)
                except:
                    result = '"Function word_count() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert dave_utilities.compare_dicts(test_dict2, result) == True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function word_count() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: word_count() should return dictionary: \"" + str(test_dict2) + "\" with argument \"" + s_text + "\" but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 4: Task 1: Test output_fixed_text() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.output_fixed_text(s_text)
                except:
                    result = '"Function output_fixed_text() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                inp_file_1 = open("fixed.txt", "r")
                s_data1 = inp_file_1.read()
                inp_file_1.close()
                inp_file_2 = open("fixed_example.txt", "r")
                s_data2 = inp_file_2.read()
                inp_file_2.close()
                assert s_data1.strip() == s_data2.strip()
                self.result[i_test_num-1] = True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function output_fixed_text() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: output_fixed_text() writes an incorrect value to the file.  Look at the file fixed_example.txt to see what should have been written to the file fixed.txt.</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 5: Task 2: Test make_dictionary() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)

            spanish_dict = {"amigo":"friend", "hola":"hello", "mi":"my", "donde":"where", "esta":"is", "diablo":"devil", "bano":"bathroom"}        
            error_calling_function = False
            try:
                try:
                    result = sm.make_dictionary()
                except:
                    result = '"Function make_dictionary() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert dave_utilities.compare_dicts(result, spanish_dict) == True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function make_dictionary() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: make_dictionary() should return should return " + str(spanish_dict) + " but it returns " + str(result) + ".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 6: Task 2: Test get_text_to_translate() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)
            error_calling_function = False
            try:
                try:
                    result = sm.get_text_to_translate()
                except:
                    result = '"Function get_text_to_translate() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == "hola mi amigo donde esta la salle de de bano"
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function get_text_to_translate() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: get_text_to_translate() should return \"hola mi amigo donde esta la salle de de bano\" but it returns \"" + str(result) + "\".</font>")

            self.vbox.addWidget(object)
            i_test_num = i_test_num + 1


            # Test 7: Task 2: Test translate() function 
            object = QLabel("Test " + str(i_test_num))
            object.setWordWrap(True)
            self.result.append(False)            
            error_calling_function = False
            s_translate_me = "hola mi amigo donde esta la salle de de bano"
            try:
                try:
                    result, d_xlate_errors = sm.translate(spanish_dict, s_translate_me)
                except:
                    result = '"Function translate() caused an error.  Try adding some print statements to it to see what is happening!"'
                    error_calling_function = True
                assert result == "hello my friend where is ????? ????? ????? ????? bathroom"
                d_answer = {"la":1, "salle":1, "de":2}
                assert dave_utilities.compare_dicts(d_xlate_errors, d_answer) == True
                object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
                self.result[i_test_num-1] = True
            except:
                if error_calling_function == True:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: Function translate() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                else:
                    object.setText("<img src='octagon.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Failed: translate() should return \"hello my friend where is ????? ????? ????? ????? bathroom\" and " + str(d_answer) + ", but it returns \"" + result + "\" and " + str(d_xlate_errors) + ".</font>")

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
        self.setWindowTitle('Dictionaries Autograder')
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
	window = MainWindow("lab_17_student_submission.py")
	ret = queue.get()
	ret["result"] = window.result
	window.hide()
	queue.put(ret)
	return
def main():
	app = QApplication(sys.argv)
	window = MainWindow("lab_17_student_submission.py")
	window.show()
	app.exec()
if __name__ == "__main__":
    main()

