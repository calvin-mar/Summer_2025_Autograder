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


def autoGrader(student_submission):
    passes = []
    error_msgs = []
    print("Autograder starting...")

    dir_path = os.path.dirname(os.path.realpath(__file__))
    specific = importlib.util.spec_from_file_location("autograder_assistant", os.path.join(dir_path, "autograder_assistant.py"))
    assistant = importlib.util.module_from_spec(specific)
    specific.loader.exec_module(assistant)

    name = student_submission[:-3]
    specific_student = importlib.util.spec_from_file_location(name, os.path.join(dir_path, student_submission))
    sm = importlib.util.module_from_spec(specific_student)

    TIMEOUT = 30 
    b_proceed, s_error_msg = assistant.syntax_checker(student_submission, TIMEOUT)
    if b_proceed == False:
        passes.append(False)
        error_msgs.append("There is a problem with your file.")
    else:
        specific_student.loader.exec_module(sm)

        ########################################################################
        # Start of tests #######################################################
        ########################################################################
        i_test_num = 1
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
        

        # Test 1: 



        
        try:
            assert sm.i_task_1 == len(s_task_1_data)
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_1 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        
        # Test 2: 



        try:
            assert sm.s_task_2 == s_task_2_data[6]
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_2 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 3: 



        try:
            assert sm.b_task_3 == False
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_3 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 4: 



        try:
            assert sm.s_task_4 == s_task_4_data.strip()
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_4 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 5: 



        try:
            assert sm.b_task_5 == False
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_7 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 6: 



        try:
            assert sm.b_task_6 == False
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_6 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 7: 



        try:
            assert sm.l_task_7 == s_task_7_data.split(":")
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable l_task_7 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 8: 



        try:
            assert sm.i_task_8_start == 5 
            assert sm.i_task_8_stop == 10
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_8_start and i_task_8_stop exist and have the correct values. </font>")


        i_test_num = i_test_num + 1

        # Test 9: 



        try:
            assert sm.s_task_9 == s_task_9_data_A + s_task_9_data_B
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_9 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 10: 



        try:
            l_tmp = s_task_7_data.split(":")
            l_tmp.reverse()
            tmp_str = ""
            for word in l_tmp:
                tmp_str = tmp_str + word
            
            assert lab_12_student_submission.s_task_10 == tmp_str
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_10 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 11: 



        try:
            assert sm.i_task_11_end == 6
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_11 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 12: 



        try:
            assert sm.b_task_12 == False
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_12 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 13: 



        try:
            assert sm.b_task_13 == False
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_13 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 14: 



        try:
            assert sm.i_task_14 == len(s_task_14_data)
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_14 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 15: 



        try:
            assert sm.s_task_15 == s_task_15_data[1]
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_15 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 16: 



        try:
            assert sm.b_task_16 == False
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_16 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 17: 



        try:
            assert lab_12_student_submission.b_task_17 == True
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_17 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 18: 



        try:
            assert sm.b_task_18 == False
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_18 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 19: 



        try:
            assert sm.s_task_19 == s_task_19_data.strip()
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_19 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 20: 



        try:
            assert sm.l_task_20 == s_task_20_data.split(", ")
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable l_task_20 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 21: 



        try:
            assert sm.i_task_21_start == 4
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_21 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 22: 



        try:
            l_tmp = s_task_7_data.split(":")
            tmp_str = ""
            for word in l_tmp:
                tmp_str = tmp_str + word
         
            assert sm.s_task_22 == tmp_str
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_22 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 23: 



        try:
            assert sm.i_task_23 == len(s_task_23_data)
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable i_task_23 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 24: 



        try:
            assert lab_12_student_submission.s_task_24 == s_task_24_data.strip()
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable 2_task_24 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 25: 



        try:
            assert sm.b_task_25 == False
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable b_task_25 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 26: 



        try:
            assert sm.s_task_26 == s_task_26_data[3]
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable s_task_26 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        # Test 27: 



        try:
            l_tmp = s_task_27_data.split("ball")
                    
            assert sm.l_task_27 == l_tmp
            passes.append(True)
            
        except:
            passes.append(False)
            error_msgs.append("<font color=black>Question " + str(i_test_num) + " Failed: Make sure the variable l_task_27 exists and has the correct value. </font>")


        i_test_num = i_test_num + 1

        
        


        ########################################################################
        # End of tests
        ########################################################################
    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")

    return passes, error_msgs, assistant

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_12_student_submission.py")
	ret = queue.get()
	ret["result"] = passes
	queue.put(ret)
	return

def main():
	passes, error_msgs,assistant = autoGrader("lab_12_student_submission.py")
	assistant.displayWindow(passes, error_msgs)
	
if __name__ == "__main__":
    main()
