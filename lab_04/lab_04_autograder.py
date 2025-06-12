# Python imports
import sys
import ast
import astor
import re
import os
import importlib.util

def autoGrader(student_submission):
    try:
        l_data = shm.ShareableList(sequence=None, name="l_data")
        l_data.shm.close()
        l_data.shm.unlink()
    except:
        pass
    
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
        if(s_error_msg != ""):
            error_msgs.append(s_error_msg)
        else:
            error_msgs.append("There is a problem with your file.")
    else:
        specific_student.loader.exec_module(sm)

        ########################################################################
        # Start of tests #######################################################
        ########################################################################

        # Test 1: Task 1: Test biggest_number() function with biggest in 1st position

        try:
            result = assistant.testFunction(sm.double_a_number, (3,))
            print('youtashdliahsdoavuhsbljh',result)
            if(result[1]):
                result[0] = result[0] + " The parameter was 3. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 6):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: double_a_number() should return 6 when the user enters 3, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function double_a_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ######################


        # Test 2: Task 2: Test biggest_number() function - biggest in 1st arg
        
        try:
            result = assistant.testFunction(sm.biggest_number, (1,2,3))
            if(result[1]):
                result[0] = result[0] + " The parameters were 1, 2, 3. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 3):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_number() should return 3 when the arguments are 1, 2, and 3, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")


        # Test 3: Task 2: Test biggest_number() function - biggest in 2nd arg

        try:
            result = assistant.testFunction(sm.biggest_number, (1,3,2))
            if(result[1]):
                result[0] = result[0] + " The parameters were 1, 3, 2. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 3):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_number() should return 3 when the arguments are 1, 3, and 2, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            

        # Test 4: Task 2: Test biggest_number() function - biggest in 3rd arg

        try:
            result = assistant.testFunction(sm.biggest_number, (3,1,2))
            if(result[1]):
                result[0] = result[0] + " The parameters were 3, 1, 2. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 3):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_number() should return 3 when the arguments are 3, 1, and 2, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        
        # Test 5: Task 2: Test biggest_number() function - with negative numbers

        try:
            result = assistant.testFunction(sm.biggest_number, (-3,-1,-2))
            if(result[1]):
                result[0] = result[0] + " The parameters were -3,-1,-2. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == -1):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_number() should return -1 when the arguments are -3, -1, and -2, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ######################


        # Test 6: Task 3: Test is_even() function with odd number
        try:
            result = assistant.testFunction(sm.is_even, (17,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 17. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_even() should return False with odd number 17, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_even() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 7: Task 3: Test is_even() function with even number
        
        try:
            result = assistant.testFunction(sm.is_even, (16,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 16. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_even() should return True with odd number 16, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_even() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ######################

        # Test 8: Task 4: Test rectangle_area() function with length and width 5 and 3
        
        try:
            result = assistant.testFunction(sm.rectangle_area, (5,3))
            if(result[1]):
                result[0] = result[0] + " The parameters were 5, 3. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 15):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: rectangle_area() should return 15 with length 5 and width 3, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function rectangle_area() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ######################

        # Test 9: Task 5: Test km_to_miles() function with 10 km which equals 6.2 miles
        try:
            result = assistant.testFunction(sm.km_to_miles, (10,))
            if(result[1]):
                result[0] = result[0] + " The parameters were 5, 3. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 6.2):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: km_to_miles() should return 6.2 with 10 km as argument, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function km_to_miles() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ######################



        # Test 10: Task 6: Test is_leap_year() function with 2111 (not a leap year)
        
        try:
            result = assistant.testFunction(sm.is_leap_year, (2111,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 2111. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_leap_year() should return False with argument 2111, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_leap_year() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 11: Task 6: Test is_leap_year() function with 1604 (is a leap year)
        try:
            result = assistant.testFunction(sm.is_leap_year, (1604,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 1604. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_leap_year() should return True with argument 1604, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_leap_year() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 12: Task 6: Test is_leap_year() function with 1900 (not a leap year)
        
        try:
            result = assistant.testFunction(sm.is_leap_year, (1900,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 1900. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_leap_year() should return False with argument 1900, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_leap_year() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 13: Task 6: Test is_leap_year() function with 2000 (is a leap year)
        try:
            result = assistant.testFunction(sm.is_leap_year, (2000,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 2000. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_leap_year() should return True with argument 2000, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_leap_year() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ########################################################################
        # End of tests
        ########################################################################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")

    return passes, error_msgs, assistant

def testing():
	passes, error_msgs,assistant = autoGrader("lab_04_student_submission.py")
	return passes

def main():
    testSets = [1, 4, 2, 1, 1, 4]
    passes, error_msgs,assistant = autoGrader("lab_04_student_submission.py")
    assistant.displayWindow(passes, error_msgs, testSets)
	
if __name__ == "__main__":
    main()
