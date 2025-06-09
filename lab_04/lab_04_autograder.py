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



        # Test 1: Task 1: Test biggest_number() function with biggest in 1st position
        try:
            result = assistant.is_inf(sm.double_a_number, (3,))
        except:
            result = "Error"
        
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within double_a_number(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function double_a_number() caused an error.  Try adding some print statements to it to see what is happening!")
        else:
            if(result == 6):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: double_a_number() should return 6 when the user enters 3, but it returns " + str(result) + ".</font>")
        
        

        ######################


        # Test 2: Task 2: Test biggest_number() function - biggest in 1st arg
        
        try:
            result = assistant.is_inf(sm.biggest_number, (1,2,3))
        except:
            result = "Error"
            
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within biggest_number(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function biggest_number() caused an error.  Try adding some print statements to it to see what is happening!")
        else:
            if(result == 3):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: biggest_number() should return 3 when the arguments are 1, 2, and 3, but it returns " + str(result) + ".</font>")



        # Test 3: Task 2: Test biggest_number() function - biggest in 2nd arg

        try:
            result = assistant.is_inf(sm.biggest_number, (1,3,2))
        except:
            result = "Error"
            
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within biggest_number(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function biggest_number() caused an error.  Try adding some print statements to it to see what is happening!")
        else:
            if(result == 3):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: biggest_number() should return 3 when the arguments are 1, 3, and 2, but it returns " + str(result) + ".</font>")
            

        # Test 4: Task 2: Test biggest_number() function - biggest in 3rd arg

        try:
            result = assistant.is_inf(sm.biggest_number, (3,1,2))
        except:
            result = "Error"
        
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within biggest_number(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function biggest_number() caused an error. or it might not be defined (perhaps you made a typo in the name). Try adding some print statements to it to see what is happening!")
        else:
            if(result == 3):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: biggest_number() should return 3 when the arguments are 3, 1, and 2, but it returns " + str(result) + ".</font>")
        
        

        ######################


        # Test 5: Task 3: Test is_even() function with odd number
        try:
            result = assistant.is_inf(sm.is_even, (17,))
        except:
            result = "Error"
          
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within is_even(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function is_even() caused an error. or it might not be defined (perhaps you made a typo in the name). Try adding some print statements to it to see what is happening!")
        else:
            if(result == False):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: is_even() should return False with odd number 17, but it returns " + str(result) + ".</font>")


        # Test 6: Task 3: Test is_even() function with even number
        
        try:
            result = assistant.is_inf(sm.is_even, (16,))
        except:
            result = "Error"
            
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within is_even(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function is_even() caused an error. or it might not be defined (perhaps you made a typo in the name). Try adding some print statements to it to see what is happening!")
        else:
            if(result == True):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: is_even() should return True with odd number 16, but it returns " + str(result) + ".</font>")


        ######################


        # Test 7: Task 4: Test rectangle_area() function with length and width 5 and 3
        
        try:
            result = assistant.is_inf(sm.rectangle_area, (5,3))
        except:
            result = "Error"
             
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within rectangle_area(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function rectangle_area() caused an error. or it might not be defined (perhaps you made a typo in the name). Try adding some print statements to it to see what is happening!")
        else:
            if(result == 15):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: rectangle_area() should return 15 with length 5 and width 3, but it returns " + str(result) + ".</font>")


        ######################


        # Test 8: Task 5: Test km_to_miles() function with 10 km which equals 6.2 miles
        try:
            result = assistant.is_inf(sm.km_to_miles, (10,))
        except:
            result = "Error"
           
        
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within km_to_miles(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function km_to_miles() caused an error. or it might not be defined (perhaps you made a typo in the name). Try adding some print statements to it to see what is happening!")
        else:
            if(result == 15):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: km_to_miles() should return 6.2 with 10 km as argument, but it returns " + str(result) + ".</font>")
        

        ######################



        # Test 9: Task 6: Test is_leap_year() function with 2111 (not a leap year)
        
        try:
            result = assistant.is_inf(sm.is_leap_year, (2111,))
        except:
            result = "Error"
           
        
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within is_leap_year(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function is_leap_year() caused an error or it might not be defined (perhaps you made a typo in the name). Try adding some print statements to it to see what is happening!")
        else:
            if(result == False):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: is_leap_year() should return False with argument 2111, but it returns " + str(result) + ".</font>")


        # Test 10: Task 6: Test is_leap_year() function with 1604 (is a leap year)
        try:
            result = assistant.is_inf(sm.is_leap_year, (1604,))
        except:
            result = "Error"
 
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within is_leap_year(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function is_leap_year() caused an error or it might not be defined (perhaps you made a typo in the name). Try adding some print statements to it to see what is happening!")
        else:
            if(result == True):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: is_leap_year() should return True with argument 1604, but it returns " + str(result) + ".</font>")



        # Test 11: Task 6: Test is_leap_year() function with 1900 (not a leap year)
        try:
            result = assistant.is_inf(sm.is_leap_year, (1900,))
        except:
            result = "Error"
         
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within is_leap_year(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function is_leap_year() caused an error or it might not be defined (perhaps you made a typo in the name). Try adding some print statements to it to see what is happening!")
        else:
            if(result == False):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: is_leap_year() should return False with argument 1900, but it returns " + str(result) + ".</font>")


        #####################

        # Test 12: Task 6: Test is_leap_year() function with 2000 (is a leap year)
        try:
            result = assistant.is_inf(sm.is_leap_year, (2000,))
        except:
            result = "Error"
           

        
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: An infinite loop is detected within is_leap_year(). Check for unchanged loop conditions.")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append("Function is_leap_year() caused an error or it might not be defined (perhaps you made a typo in the name). Try adding some print statements to it to see what is happening!")
        else:
            if(result == True):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: is_leap_year() should return True with argument 2000, but it returns " + str(result) + ".</font>")


        
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
    testSets = [1, 3, 2, 1, 1, 4]
    passes, error_msgs,assistant = autoGrader("lab_04_student_submission.py")
    assistant.displayWindow(passes, error_msgs, testSets)
	
if __name__ == "__main__":
    main()
