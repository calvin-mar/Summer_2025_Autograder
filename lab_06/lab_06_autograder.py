# Python imports
import sys
import ast
import astor
import re
import os
import math
import importlib.util
from multiprocessing import shared_memory as shm

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt, QRect
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont

dir_path = os.path.dirname(os.path.realpath(__file__))
specific = importlib.util.spec_from_file_location("autograder_assistant", os.path.join(dir_path, "autograder_assistant.py"))
assistant = importlib.util.module_from_spec(specific)
specific.loader.exec_module(assistant)

def autoGrader(student_submission):
    passes = []
    error_msgs = []
    
    print("Autograder starting...")


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
            error_msgs.append("There is a problem with your file")
    else:
        specific_student.loader.exec_module(sm)

        ########################################################################
        # Start of tests #######################################################
        ########################################################################

        # Test 1: Task 1: Test biggest_number() function with biggest in 1st position
        l_data = shm.ShareableList([100, 80, 30, 90, 20, 10, 50, 40, 70, 60], name="l_data")
        try:
            result = assistant.testFunction(sm.biggest_number)
            if(result[1]):
                result[0] = result[0] + " The inputs were 100, 80, 30, 90, 20, 10, 50, 40, 70, 60. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 100):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_number() should return 100 when the user enters 100, 80, 30, 90, 20, 10, 50, 40, 70, 60, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()
        
       # Test 2: Task 1: Test biggest_number() function with biggest in 10th position

        l_data = shm.ShareableList([50, 20, 80, 40, 10, 70, 90, 60, 30, 100], name="l_data")
        try:
            result = assistant.testFunction(sm.biggest_number)
            if(result[1]):
                result[0] = result[0] + " The inputs were 50, 20, 80, 40, 10, 70, 90, 60, 30, 100. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 100):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_number() should return 100 when the user enters 50, 20, 80, 40, 10, 70, 90, 60, 30, 100, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink() 
 
        # Test 3: Task 1: Test biggest_number() function with biggest in 5th position
        
        l_data = shm.ShareableList([40, 70, 30, 80, 100, 90, 60, 10, 20, 50], name="l_data")
        try:
            result = assistant.testFunction(sm.biggest_number)
            if(result[1]):
                result[0] = result[0] + " The inputs were 40, 70, 30, 80, 100, 90, 60, 10, 20, 50. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 100):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_number() should return 100 when the user enters 40, 70, 30, 80, 100, 90, 60, 10, 20, 50, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()      

        # Test 4: Task 1: Test biggest_number() function with biggest in 5th position but all numbers are negative

        l_data = shm.ShareableList([-50, -80, -100, -30, -10, -20, -70, -90, -60, -40], name="l_data")
        try:
            result = assistant.testFunction(sm.biggest_number)
            if(result[1]):
                result[0] = result[0] + " The inputs were -50, -80, -100, -30, -10, -20, -70, -90, -60, -40. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == -10):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_number() should return -10 when the user enters -50, -80, -100, -30, -10, -20, -70, -90, -60, -40, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()              

        ######################
       
        # Test 5: Task 2: Test repeated_doubler() function - double 5 4 times
        try:
            result = assistant.testFunction(sm.repeated_doubler, (5,4))
            if(result[1]):
                result[0] = result[0] + " The paramters were 5, 4. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 80):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: repeated_doubler() should return 80 when the arguments are 5 and 4, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function repeated_doubler() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 6: Task 2: Test repeated_doubler() function - double 0 3 times

        try:
            result = assistant.testFunction(sm.repeated_doubler, (0,3))
            if(result[1]):
                result[0] = result[0] + " The paramters were 0, 3. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 0):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: repeated_doubler() should return 0 when the arguments are 0 and 3, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function repeated_doubler() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

       ######################

        # Test 7: Task 3: Test fib_num() function - 1st fib is 0

        try:
            result = assistant.testFunction(sm.fib_num, (1,))
            if(result[1]):
                result[0] = result[0] + " The paramter was 1. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 0):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: fib_num() should return 0 when the argument is 1, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function fib_num() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")


        # Test 8: Task 3: Test fib_num() function - 2nd fib is 1

        try:
            result = assistant.testFunction(sm.fib_num, (2,))
            if(result[1]):
                result[0] = result[0] + " The paramter was 2. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 1):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: fib_num() should return 1 when the argument is 2, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function fib_num() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 9: Task 3: Test fib_num() function - 3rd fib is 1

        try:
            result = assistant.testFunction(sm.fib_num, (3,))
            if(result[1]):
                result[0] = result[0] + " The paramter was 3. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 1):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: fib_num() should return 1 when the argument is 3, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function fib_num() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 10: Task 3: Test fib_num() function - 4th fib is 2
        try:
            result = assistant.testFunction(sm.fib_num, (4,))
            if(result[1]):
                result[0] = result[0] + " The paramter was 4. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 2):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: fib_num() should return 2 when the argument is 4, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function fib_num() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 11: Task 3: Test fib_num() function - 9th fib is 21
        try:
            result = assistant.testFunction(sm.fib_num, (9,))
            if(result[1]):
                result[0] = result[0] + " The paramter was 9. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 21):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: fib_num() should return 21 when the argument is 9, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function fib_num() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 12: Task 3: Test fib_num() function - 16th fib is 610
        try:
            result = assistant.testFunction(sm.fib_num, (16,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 16. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 610):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: fib_num() should return 610 when the argument is 16, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function fib_num() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ######################
        
        # Test 13: Task 4: Test make_bill() function with 2 items and no invalid input that requires running the input validation loops: coke, 1.99, 2, burger, 4.99, 2, done - answer: $17.84088 (without the $)

        l_data = shm.ShareableList(["coke", "1.99", "2", "burger", "4.99", "2", "done"], name="l_data")
        try:
            result = assistant.testFunction(sm.make_bill)
            if(result[1]):
                result[0] = result[0] + " The inputs were \"coke\", \"1.99\", \"2\", \"burger\", \"4.99\", \"2\", \"done\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(math.isclose(result[0], 17.84088)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: make_bill() should return $17.84088 (without the $ and possibly a few more decimal places due to inaccuracies of floating point numbers) when the user inputs coke, 1.99, 2, burger, 4.99, 2, done, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function make_bill() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink() 

        # Test 14: Task 4: Test make_bill() function with 3 items and 3 invalid prices for the 1st item: coke, -1, -4, 0, 1.99, 4, burger, 4.99, 3, fries, 3.49, 3, done - answer: $42.6852 (without the $)

        l_data = shm.ShareableList(["coke", "-1", "-4", "0", "1.99", "4", "burger", "4.99", "3", "fries", "3.49", "3","done"], name="l_data")
        try:
            result = assistant.testFunction(sm.make_bill)
            if(result[1]):
                result[0] = result[0] + ' The inputs were "coke", "-1", "-4", "0", "1.99", "4", "burger", "4.99", "3", "fries", "3.49", "3","done". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(math.isclose(result[0], 42.6852)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: make_bill() should return $42.6852 (without the $ and possibly a few more decimal places due to inaccuracies of floating point numbers) when the user inputs coke, -1, -4, 0, 1.99, 4, burger, 4.99, 3, fries, 3.49, 3, done, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function make_bill() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink() 

        # Test 15: Task 4: Test make_bill() function with 3 items and 3 invalid quantities for the 2nd item: shake, 4.59, 2, fish, 9.99, 0, -4, 0, 2, broccoli, 1.99, 1, done - answer: $39.8097 (without the $)

        l_data = shm.ShareableList(["shake", "4.59", "2", "fish", "9.99", "0", "-4", "0", "2", "broccoli", "1.99", "1", "done"], name="l_data")
        try:
            result = assistant.testFunction(sm.make_bill)
            if(result[1]):
                result[0] = result[0] + ' The inputs were "shake", "4.59", "2", "fish", "9.99", "0", "-4", "0", "2", "broccoli", "1.99", "1", "done". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(math.isclose(result[0], 39.8097)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: make_bill() should return $39.8097 (without the $ and possibly a few more decimal places due to inaccuracies of floating point numbers) when the user inputs shake, 4.59, 2, fish, 9.99, 0, -4, 0, 2, broccoli, 1.99, 1, done, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function make_bill() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink() 
                    
        ######################


        # Test 16: Task 5: Test is_prime() function with prime number: 3

        try:
            result = assistant.testFunction(sm.is_prime, (3,))
            if(result[1]):
                result[0] = result[0] + ' The parameter was 3. </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_prime() should return True with even number 3, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_prime() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 17: Task 5: Test is_prime() function with prime number: 11
        
        try:
            result = assistant.testFunction(sm.is_prime, (11,))
            if(result[1]):
                result[0] = result[0] + ' The parameter was 11. </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_prime() should return True with even number 11, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_prime() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 18: Task 5: Test is_prime() function with non-prime number: 1
        
        try:
            result = assistant.testFunction(sm.is_prime, (1,))
            if(result[1]):
                result[0] = result[0] + ' The parameter was 1. </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_prime() should return False with even number 1, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_prime() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 19: Task 5: Test is_prime() function with prime number: 2
        
        try:
            result = assistant.testFunction(sm.is_prime, (2,))
            if(result[1]):
                result[0] = result[0] + ' The parameter was 2. </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_prime() should return True with even number 2, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_prime() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 20: Task 5: Test is_prime() function with non-prime number: 12
        
        try:
            result = assistant.testFunction(sm.is_prime, (12,))
            if(result[1]):
                result[0] = result[0] + ' The parameter was 12. </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_prime() should return False with even number 12, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_prime() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 21: Task 5: Test count_primes() function with 17 answer: 7 numbers <= 17 are prime: 2, 3, 5, 7, 11, 13, 17
        
        try:
            result = assistant.testFunction(sm.count_primes, (17,))
            if(result[1]):
                result[0] = result[0] + ' The parameter was 17. </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 7):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: count_primes() should return 7 with argument 17, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function count_primes() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 22: Task 5: Test count_primes() function with 16 answer: 6 numbers <= 16 are prime: 2, 3, 5, 7, 11, 13
        try:
            result = assistant.testFunction(sm.count_primes, (16,))
            if(result[1]):
                result[0] = result[0] + ' The parameter was 17. </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 6):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: count_primes() should return 6 with argument 16, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function count_primes() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        
        ########################################################################
        # End of tests
        ########################################################################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")

    return passes, error_msgs

def testing():
	passes, error_msgs,assistant = autoGrader("lab_06_student_submission.py")
	return passes

def main():
    testSets = [4, 2, 6, 3, 5, 2]
    
    #passes, error_msgs = autoGrader("lab_06_student_submission.py")
    try:
        assistant.displayWindow(autoGrader, "lab_06_student_submission.py", testSets)
    except Exception as e:
        print("assistant crashed:", e)
	
if __name__ == "__main__":
    main()
