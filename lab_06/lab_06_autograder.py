# Python imports
import sys
import ast
import astor
import re
import os
import importlib.util

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt, QRect
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from layout_colorwidget import Color


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
    ##################################################################################################
    ###end new code
    ##################################################################################################

        ########################################################################
        # Start of tests #######################################################
        ########################################################################
        i_test_num = 1
        # Test 1: Task 1: Test biggest_number() function with biggest in 1st position
        error_calling_function = False
        try:
            try:
                result = sm.biggest_number()
            except:
                result = '"Function biggest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 100
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function biggest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: biggest_number() should return 100 when the user enters 100, 80, 30, 90, 20, 10, 50, 40, 70, 60, but it returns " + str(result) + ".</font>")
                
        i_test_num = i_test_num + 1

        
        # Test 2: Task 1: Test biggest_number() function with biggest in 10th position
        error_calling_function = False        
        try:
            try:
                result = biggest_number()
            except:
                result = '"Function biggest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 100
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function biggest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:            
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: biggest_number() should return 100 when the user enters 50, 20, 80, 40, 10, 70, 90, 60, 30, 100, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1
        

        # Test 3: Task 1: Test biggest_number() function with biggest in 5th position



        error_calling_function = False        
        try:
            try:
                result = biggest_number()
            except:
                result = '"Function biggest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 100
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function biggest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:            
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: biggest_number() should return 100 when the user enters 40, 70, 30, 80, 100, 90, 60, 10, 20, 50, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1
        

        # Test 4: Task 1: Test biggest_number() function with biggest in 5th position but all numbers are negative



        error_calling_function = False        
        try:
            try:
                result = biggest_number()
            except:
                result = '"Function biggest_number() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == -10
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function biggest_number() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:            
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: biggest_number() should return -10 when the user enters -50, -80, -100, -30, -10, -20, -70, -90, -60, -40, but it returns " + str(result) + ".</font>")


        
        i_test_num = i_test_num + 1

        ######################

        
        # Test 5: Task 2: Test repeated_doubler() function - double 5 4 times



        error_calling_function = False        
        try:
            try:
                result = repeated_doubler(5, 4)
            except:
                result = '"Function repeated_doubler() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 80
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function repeated_doubler() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: repeated_doubler() should return 80 when the arguments are 5 and 4, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 6: Task 2: Test repeated_doubler() function - double 0 3 times
        error_calling_function = False        



        try:
            try:
                result = repeated_doubler(0, 3)
            except:
                result = '"Function repeated_doubler() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 0
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function repeated_doubler() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: repeated_doubler() should return 0 when the arguments are 0 and 3, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ######################
        

        # Test 7: Task 3: Test fib_num() function - 1st fib is 0
        error_calling_function = False        



        try:
            try:
                result = fib_num(1)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 0
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 0 when the argument is 1, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 8: Task 3: Test fib_num() function - 2nd fib is 1
        error_calling_function = False        



        try:
            try:
                result = fib_num(2)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 1
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 1 when the argument is 2, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 9: Task 3: Test fib_num() function - 3rd fib is 1
        error_calling_function = False        



        try:
            try:
                result = fib_num(3)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 1
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 1 when the argument is 3, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 10: Task 3: Test fib_num() function - 4th fib is 2
        error_calling_function = False        



        try:
            try:
                result = fib_num(4)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 2
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 2 when the argument is 4, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 11: Task 3: Test fib_num() function - 9th fib is 21
        error_calling_function = False        



        try:
            try:
                result = fib_num(9)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 21
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 21 when the argument is 9, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 12: Task 3: Test fib_num() function - 16th fib is 610
        error_calling_function = False        



        try:
            try:
                result = fib_num(16)
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 610
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function fib_num() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: fib_num() should return 610 when the argument is 16, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ######################

        
        # Test 13: Task 4: Test make_bill() function with 2 items and no invalid input that requires running the input validation loops: coke, 1.99, 2, burger, 4.99, 2, done - answer: $17.84088 (without the $)
        error_calling_function = False        



        try:
            try:
                result = make_bill()
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert math.isclose(result, 17.84088)
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function make_bill() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: make_bill() should return $17.84088 (without the $ and possibly a few more decimal places due to inaccuracies of floating point numbers) when the user inputs coke, 1.99, 2, burger, 4.99, 2, done, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1
        

        # Test 14: Task 4: Test make_bill() function with 3 items and 3 invalid prices for the 1st item: coke, -1, -4, 0, 1.99, 4, burger, 4.99, 3, fries, 3.49, 3, done - answer: $42.6852 (without the $)
        error_calling_function = False        



        try:
            try:
                result = make_bill()
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert math.isclose(result, 42.6852)
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function make_bill() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: make_bill() should return $42.6852 (without the $ and possibly a few more decimal places due to inaccuracies of floating point numbers) when the user inputs coke, -1, -4, 0, 1.99, 4, burger, 4.99, 3, fries, 3.49, 3, done, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 15: Task 4: Test make_bill() function with 3 items and 3 invalid quantities for the 2nd item: shake, 4.59, 2, fish, 9.99, 0, -4, 0, 2, broccoli, 1.99, 1, done - answer: $39.8097 (without the $)
        error_calling_function = False        



        try:
            try:
                result = make_bill()
            except:
                result = '"Function fib_num() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert math.isclose(result, 39.8097)
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function make_bill() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: make_bill() should return $39.8097 (without the $ and possibly a few more decimal places due to inaccuracies of floating point numbers) when the user inputs shake, 4.59, 2, fish, 9.99, 0, -4, 0, 2, broccoli, 1.99, 1, done, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1
        
        ######################


        # Test 16: Task 5: Test is_prime() function with prime number: 3
        error_calling_function = False        



        try:
            try:
                result = is_prime(3)
            except:
                result = '"Function is_prime() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == True
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function is_prime() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: is_prime() should return True with even number 3, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        # Test 17: Task 5: Test is_prime() function with prime number: 11
        error_calling_function = False        



        try:
            try:
                result = is_prime(11)
            except:
                result = '"Function is_prime() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == True
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function is_prime() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: is_prime() should return True with even number 11, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        # Test 18: Task 5: Test is_prime() function with non-prime number: 1
        error_calling_function = False        



        try:
            try:
                result = is_prime(1)
            except:
                result = '"Function is_prime() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == False
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function is_prime() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: is_prime() should return False with even number 1, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        # Test 19: Task 5: Test is_prime() function with non-prime number: 2
        error_calling_function = False        



        try:
            try:
                result = is_prime(2)
            except:
                result = '"Function is_prime() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == True
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function is_prime() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: is_prime() should return True with even number 2, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        # Test 20: Task 5: Test is_prime() function with non-prime number: 12
        error_calling_function = False        



        try:
            try:
                result = is_prime(12)
            except:
                result = '"Function is_prime() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == False
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function is_prime() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: is_prime() should return False with even number 12, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        

        # Test 21: Task 5: Test count_primes() function with 17 answer: 7 numbers <= 17 are prime: 2, 3, 5, 7, 11, 13, 17
        error_calling_function = False        



        try:
            try:
                result = count_primes(17)
            except:
                result = '"Function count_primes() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 7
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function count_primes() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:            
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: count_primes() should return 7 with argument 17, but it returns " + str(result) + ".</font>")

        i_test_num = i_test_num + 1

        # Test 22: Task 5: Test count_primes() function with 16 answer: 6 numbers <= 16 are prime: 2, 3, 5, 7, 11, 13
        error_calling_function = False        
        try:
            try:
                result = count_primes(16)
            except:
                result = '"Function count_primes() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert result == 6
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function count_primes() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:            
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: count_primes() should return 6 with argument 16, but it returns " + str(result) + ".</font>")


        
        ########################################################################
        # End of tests
        ########################################################################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")

    return passes, error_msgs, assistant

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_06_student_submission.py")
	ret = queue.get()
	ret["result"] = passes
	queue.put(ret)
	return

def main():
	passes, error_msgs,assistant = autoGrader("lab_06_student_submission.py")
	assistant.displayWinow(passes, error_msgs)
	
if __name__ == "__main__":
    main()
