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
                result = sm.double_a_number(3)
            except:
                result = '"Function double_a_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 6
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function double_a_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: double_a_number() should return 6 when the user enters 3, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ######################


        # Test 2: Task 2: Test biggest_number() function - biggest in 1st arg
        
        

        error_calling_function = False
        try:
            try:
                result = sm.biggest_number(1, 2, 3)
            except:
                result = '"Function biggest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 3
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function biggest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: biggest_number() should return 3 when the arguments are 1, 2, and 3, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 3: Task 2: Test biggest_number() function - biggest in 2nd arg
        
        

        error_calling_function = False
        try:
            try:
                result = sm.biggest_number(1, 3, 2)
            except:
                result = '"Function biggest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 3
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function biggest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: biggest_number() should return 3 when the arguments are 1, 3, and 2, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1



        # Test 4: Task 2: Test biggest_number() function - biggest in 3rd arg
        
        

        error_calling_function = False
        try:
            try:
                result = sm.biggest_number(3, 1, 2)
            except:
                result = '"Function biggest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 3
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function biggest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: biggest_number() should return 3 when the arguments are 3, 1, and 2, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ######################


        # Test 5: Task 3: Test is_even() function with odd number
        
        

        error_calling_function = False
        try:
            try:
                result = sm.is_even(17)
            except:
                result = '"Function is_even() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == False
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function is_even() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: is_even() should return False with odd number 17, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1




        # Test 6: Task 3: Test is_even() function with even number
        
        

        error_calling_function = False
        try:
            try:
                result = sm.is_even(16)
            except:
                result = '"Function is_even() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == True
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function is_even() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: is_even() should return True with even number 16, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        ######################


        # Test 7: Task 4: Test rectangle_area() function with length and width 5 and 3
        
        

        error_calling_function = False
        try:
            try:
                result = sm.rectangle_area(5, 3)
            except:
                result = '"Function rectangle_area() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 15
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function rectangle_area() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: rectangle_area() should return 15 with length 5 and width 3, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        ######################


        # Test 8: Task 5: Test km_to_miles() function with 10 km which equals 6.2 miles
        
        

        error_calling_function = False
        try:
            try:
                result = sm.km_to_miles(10)
            except:
                result = '"Function km_to_miles() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 6.2
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function km_to_miles() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: km_to_miles() should return 6.2 with 10 km as argument, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ######################



        # Test 9: Task 6: Test is_leap_year() function with 2111 (not a leap year)
        
        

        error_calling_function = False
        try:
            try:
                result = sm.is_leap_year(2111)
            except:
                result = '"Function is_leap_year() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == False
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function is_leap_year() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: is_leap_year() should return False with argument 2111, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1



        # Test 10: Task 6: Test is_leap_year() function with 1604 (is a leap year)
        
        

        error_calling_function = False
        try:
            try:
                result = sm.is_leap_year(1604)
            except:
                result = '"Function is_leap_year() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == True
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function is_leap_year() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: is_leap_year() should return True with argument 1604, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1



        # Test 11: Task 6: Test is_leap_year() function with 1900 (not a leap year)
        
        

        error_calling_function = False
        try:
            try:
                result = sm.is_leap_year(1900)
            except:
                result = '"Function is_leap_year() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == False
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function is_leap_year() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: is_leap_year() should return False with argument 1900, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        #####################

        # Test 12: Task 6: Test is_leap_year() function with 2000 (is a leap year)
        
        

        error_calling_function = False
        try:
            try:
                result = sm.is_leap_year(2000)
            except:
                result = '"Function is_leap_year() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == True
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function is_leap_year() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: is_leap_year() should return True with argument 2000, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        
        ########################################################################
        # End of tests
        ########################################################################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")

    return passes, error_msgs, assistant

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_04_student_submission.py")
	ret = queue.get()
	ret["result"] = passes
	queue.put(ret)
	return

def main():
	passes, error_msgs,assistant = autoGrader("lab_04_student_submission.py")
	assistant.displayWindow(passes, error_msgs)
	
if __name__ == "__main__":
    main()
