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
            try:
                result = sm.biggest_smallest_number()
            except:
                result = '"Function biggest_smallest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == (100, 10)
            object.setText("<img src='check.png' width='32' height='32'><font color=black>Test " + str(i_test_num) + " Passed </font>")
            passes.append(True)
        except:
            if error_calling_function == True:
                error_msgs.append(" Failed: Function biggest_smallest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: biggest_smallest_number() should return 100 and 10 when the user enters 100, 80, 30, 90, 20, 10, 50, 40, 70, 60, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

        
        i_test_num = i_test_num + 1

        
        # Test 2: Task 1: Test biggest_smallest_number() function with biggest in 10th (last) position and smallest in 1st position
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.biggest_smallest_number()
            except:
                result = '"Function biggest_smallest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == (100, 10)
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function biggest_smallest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: biggest_smallest_number() should return 100 and 10 when the user enters 50, 20, 80, 40, 10, 70, 90, 60, 30, 100, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 3: Task 1: Test biggest_smallest_number() function with biggest in 5th position and smallest in 10th (last) position
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.biggest_smallest_number()
            except:
                result = '"Function biggest_smallest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == (100, 10)
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function biggest_smallest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: biggest_smallest_number() should return 100 and 10 when the user enters 40, 70, 30, 80, 100, 90, 60, 10, 20, 50, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 4: Task 1: Test biggest_smallest_number() function with biggest in 5th position and smallest in 3rd position but all numbers are negative
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.biggest_smallest_number()
            except:
                result = '"Function biggest_smallest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == (-10, -100)
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function biggest_smallest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: biggest_smallest_number() should return -10 and -100 when the user enters -50, -80, -100, -30, -10, -20, -70, -90, -60, -40, but it returns " + str(result[0]) + " and " + str(result[1]) + ".</font>")

        
        i_test_num = i_test_num + 1
        
        ######################

        
        # Test 5: Task 2: Test repeated_doubler() function - double 5 4 times
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.repeated_doubler(5, 4)
            except:
                result = '"Function repeated_doubler() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 80
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function repeated_doubler() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: repeated_doubler() should return 80 when the arguments are 5 and 4, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 6: Task 2: Test repeated_doubler() function - double 0 3 times
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.repeated_doubler(0, 3)
            except:
                result = '"Function repeated_doubler() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 0
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function repeated_doubler() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: repeated_doubler() should return 0 when the arguments are 0 and 3, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ######################
        

        # Test 7: Task 3: Test fib_num() function - 1st fib is 0
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.fib_num(1)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 0
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: fib_num() should return 0 when the argument is 1, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 8: Task 3: Test fib_num() function - 2nd fib is 1
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.fib_num(2)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 1
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: fib_num() should return 1 when the argument is 2, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 9: Task 3: Test fib_num() function - 3rd fib is 1
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.fib_num(3)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 1
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: fib_num() should return 1 when the argument is 3, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 10: Task 3: Test fib_num() function - 4th fib is 2
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.fib_num(4)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 2
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: fib_num() should return 2 when the argument is 4, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 11: Task 3: Test fib_num() function - 9th fib is 21
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.fib_num(9)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 21
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: fib_num() should return 21 when the argument is 9, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 12: Task 3: Test fib_num() function - 16th fib is 610
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.fib_num(16)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 610
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: fib_num() should return 610 when the argument is 16, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1
        

        ######################
        # Test 13: Task 4: Test leaf_sum() function with argument 4 for 4 days with values of 1, 2, 3, 4 for a total of 10 leaves
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.leaf_sum(4)
            except:
                result = '"Function leaf_sum() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 10
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function leaf_sum() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: leaf_sum() should return 10 when the argument is 4 and values entered are 1, 2, 3 and 4, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        
        ######################

        # Test 14: Task 5: Test class_leaf_sum() function with argument 3 for 3 students.  This will then call leaf sum for each student.  Student 1: 2 days, 9 + 8 leaves.  Student 2: 3 days, 1 + 1 + 1 leaves.  Student 3: 4 days, 4 +5 + 6 + 5 leaves.  Total 40 leaves.
        
        
        
        error_calling_function = False
        try:
            try:
                result = sm.class_leaf_sum(3)
            except:
                result = '"Function class_leaf_sum() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 40
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function class_leaf_sum() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: class_leaf_sum() should return 40 when the argument is 3 and values entered are (Student 1: 2 days, 9 + 8 leaves.  Student 2: 3 days, 1 + 1 + 1 leaves.  Student 3: 4 days, 4 +5 + 6 + 5 leaves), but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ######################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")
    
    return passes, error_msgs, assistant

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_08_student_submission.py")
	ret = queue.get()
	ret["result"] = passes
	queue.put(ret)
	return

def main():
	passes, error_msgs,assistant = autoGrader("lab_08_student_submission.py")
	assistant.displayWindow(passes, error_msgs)
	
if __name__ == "__main__":
    main()
