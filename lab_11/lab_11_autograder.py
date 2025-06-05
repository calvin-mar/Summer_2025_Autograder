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
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_len([])
            except:
                result = '"Function my_len() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == 0
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_len() should return 0 with an empty list argument, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 2: Task 1: Test my_len() function with list [8, 6, 7, 5, 3]
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_len([8, 6, 7, 5, 3])
            except:
                result = '"Function my_len() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == 5
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_len() should return 5 with this list [8, 6, 7, 5, 3] as an argument, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ###


        # Test 3: Task 2: Test my_in_list() function with list [8, 6, 7, 5, 3] and integer 0
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_in_list([8, 6, 7, 5, 3], 0)
            except:
                result = '"Function my_in_list() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_in_list() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == False
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_in_list() should return False with this list [8, 6, 7, 5, 3] and 0 as arguments, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 4: Task 2: Test my_in_list() function with list [8, 6, 7, 5, 3] and integer 8
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_in_list([8, 6, 7, 5, 3], 8)
            except:
                result = '"Function my_in_list() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_in_list() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == True
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_in_list() should return True with this list [8, 6, 7, 5, 3] and 8 as arguments, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ###

        # Test 5: Task 3: Test my_location() function with list [8, 6, 8, 5, 3] and integer 8
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_location([8, 6, 8, 5, 3], 8)
            except:
                result = '"Function my_location() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_location() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == 0
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_location() should return 0 with this list [8, 6, 8, 5, 3] and 8 as arguments, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        # Test 6: Task 3: Test my_location() function with list [8, 6, 8, 5, 3] and integer 77
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_location([8, 6, 8, 5, 3], 77)
            except:
                result = '"Function my_location() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_location() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == -1
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_location() should return -1 with this list [8, 6, 8, 5, 3] and 77 as arguments, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        ###
        
        # Test 7: Task 4: Test my_reverse() function with list [8, 6, 77, 5, 3] 
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_reverse([8, 6, 77, 5, 3])
            except:
                result = '"Function my_reverse() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_reverse() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == [3, 5, 77, 6, 8]
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_reverse() should return [3, 5, 77, 6, 8] with this list [8, 6, 7, 5, 3] argument, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1



        ###
        
        # Test 8: Task 5: Test my_extrema() function with list [77, 6, -1, 5, 3] 
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_extrema([77, 6, -1, 5, 3])
            except:
                result = '"Function my_extrema() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_extrema() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == (-1, 77)
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_extrema() should return -1 and 77 with this list [77, 6, -1, 5, 3] argument, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 9: Task 5: Test my_extrema() function with list [-1, 6, 3, 5, 77] 
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_extrema([-1, 6, 3, 5, 77])
            except:
                result = '"Function my_extrema() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_extrema() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == (-1, 77)
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_extrema() should return -1 and 77 with this list [-1, 6, 3, 5, 77] argument, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 10: Task 5: Test my_extrema() function with list [6, 77, 3, 5, -1] 
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_extrema([6, 77, 3, 5, -1])
            except:
                result = '"Function my_extrema() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_extrema() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == (-1, 77)
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_extrema() should return -1 and 77 with this list [6, 77, 3, 5, -1] argument, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

        
        i_test_num = i_test_num + 1


        ###

        # Test 11: Task 6: Test my_count() function with list [6, 77, 3, 5, -1] and 99
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_count([6, 77, 3, 5, -1], 99)
            except:
                result = '"Function my_count() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_count() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == 0
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_count() should return 0 with this list [6, 77, 3, 5, -1] and 99 as argument, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 11: Task 6: Test my_count() function with list [6, 77, 3, 5, 77] and 77
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_count([6, 77, 3, 5, 77], 77)
            except:
                result = '"Function my_count() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_count() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == 2
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_count() should return 0 with this list [6, 77, 3, 5, 77] and 77 as argument, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ###


        # Test 12: Task 7: Test my_insert() function with list [0, 1, 2, 3, 4], 0, and "X"
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_insert([0, 1, 2, 3, 4], 0, "X")
            except:
                result = '"Function my_insert() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_insert() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == ["X", 0, 1, 2, 3, 4]
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_insert() should return [\"X\", 0, 1, 2, 3, 4] with this list [0, 1, 2, 3, 4], 0, and \"X\" as argument, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        # Test 13: Task 7: Test my_insert() function with list [0, 1, 2, 3, 4], 4, and "X"
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_insert([0, 1, 2, 3, 4], 4, "X")
            except:
                result = '"Function my_insert() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_insert() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == [0, 1, 2, 3, "X", 4]
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_insert() should return [0, 1, 2, 3, \"X\", 4] with this list [0, 1, 2, 3, 4], 4, and \"X\" as argument, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        ###

        # Test 14: Task 8: Test my_remove() function with list [0, 1, 2, 3, 4, 1, 2, 1, 2], 1
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_remove([0, 1, 2, 3, 4, 1, 2, 1, 2], 1)
            except:
                result = '"Function my_remove() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_remove() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == [0, 2, 3, 4, 2, 2]
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_remove() should return [0, 2, 3, 4, 2, 2] with this list [0, 1, 2, 3, 4, 1, 2, 1, 2] and 1, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        # Test 15: Task 8: Test my_remove() function with list [0, 1, 2, 3, 4, 1, 2, 1, 2], 11
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_remove([0, 1, 2, 3, 4, 1, 2, 1, 2], 11)
            except:
                result = '"Function my_remove() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_remove() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == [0, 1, 2, 3, 4, 1, 2, 1, 2]
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_remove() should return [0, 1, 2, 3, 4, 1, 2, 1, 2] with this list [0, 1, 2, 3, 4, 1, 2, 1, 2] and 11, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        ###

        # Test 16: Task 9: Test my_sort() function with list [8, 7, 6, 5, 4, 3, 2, 1, 0]
        
        
        
        error = ""
        error_code = "none"
        try:
            try:
                result = sm.my_sort([8, 7, 6, 5, 4, 3, 2, 1, 0])
            except:
                result = '"Function my_sort() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function my_sort() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8]
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: my_sort() should return [0, 1, 2, 3, 4, 5, 6, 7, 8] with this list [8, 7, 6, 5, 4, 3, 2, 1, 0], but it returns " + str(result) + ".</font>")

        ########################################################################
        # End of tests
        ########################################################################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")
    

    return passes, error_msgs, assistant

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_11_student_submission.py")
	ret = queue.get()
	ret["result"] = passes
	queue.put(ret)
	return

def main():
	passes, error_msgs,assistant = autoGrader("lab_11_student_submission.py")
	assistant.displayWindow(passes, error_msgs)
	
if __name__ == "__main__":
    main()
