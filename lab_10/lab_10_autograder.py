# Python imports
import sys
import ast
import astor
import re
import os
import importlib.util

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
    b_proceed, s_error_msg = assistant.syntax_checker(os.path.join(dir_path, student_submission), TIMEOUT)
    if b_proceed == False:
        passes.append(False)
        error_msgs.append("There is a problem with your file.")
    else:
        specific_student.loader.exec_module(sm)
        ########################################################################
        # Start of tests #######################################################
        ########################################################################
        i_test_num = 1
        # Test 1: Task 1: Test biggest_number() function with biggest in 1st position
        error_calling_function = False
        try:
            assert len(sm.l_first) == 4
            assert sm.l_first[0] == "A"
            assert sm.l_first[1] == "B"
            assert sm.l_first[2] == "C"
            assert sm.l_first[3] == "D"
            
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_first does not contain the correct values of \"A\", \"B\", \"C\", and \"D\" or it does not have length exactly 4. </font>")

        
        i_test_num = i_test_num + 1

        # Test 2: 
        
        
        
        try:
            assert len(sm.l_last) == 3
            assert sm.l_last[0] == "K"
            assert sm.l_last[1] == "L"
            assert sm.l_last[2] == "M"
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_last does not contain the correct values of \"K\", \"L\", and \"M\" or it does not have length exactly 3. </font>")

        
        i_test_num = i_test_num + 1

        # Test 3: 
        
        
        
        try:
            assert len(sm.l_mid) == 3
            assert sm.l_mid[0] == "F"
            assert sm.l_mid[1] == "G"
            assert sm.l_mid[2] == "H"
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_last does not contain the correct values of \"F\", \"G\", and \"H\" or it does not have length exactly 3. </font>")

        
        i_test_num = i_test_num + 1

        # Test 4: 
        
        
        
        try:
            sm.l_copy_nums[0] = 5
            sm.l_copy_nums[1] = 15
            sm.l_copy_nums[2] = 25
            sm.l_copy_nums[3] = 35
            sm.l_copy_nums[4] = 45
            assert len(sm.l_nums) == 5
            assert len(sm.l_copy_nums) == 5
            assert sm.l_nums[0] == 0
            assert sm.l_nums[1] == 10
            assert sm.l_nums[2] == 20
            assert sm.l_nums[3] == 30
            assert sm.l_nums[4] == 40
            assert sm.l_copy_nums[0] == 5
            assert sm.l_copy_nums[1] == 15
            assert sm.l_copy_nums[2] == 25
            assert sm.l_copy_nums[3] == 35
            assert sm.l_copy_nums[4] == 45

            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_copy_nums is not a correct copy of l_nums because overwriting a value in l_copy_nums overwrites a value in l_nums or the length of l_copy_nums is not correct. </font>")
        ########################################################################
        # End of tests
        ########################################################################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")
    
    return passes, error_msgs, assistant

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_10_student_submission.py")
	ret = queue.get()
	ret["result"] = passes
	queue.put(ret)
	return

def main():
    #
    testSets = []
    passes, error_msgs,assistant = autoGrader("lab_10_student_submission.py")
    assistant.displayWindow(passes, error_msgs, testSets)
	
if __name__ == "__main__":
    main()
