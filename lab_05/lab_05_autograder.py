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
        # Test 1: Task 1: Test biggest_number() function with biggest in 1st position
        error_calling_function = False
        try:
            try:
                result = sm.get_estimate()
            except:
                result = "Function get_estimate() crashed or is not defined"
                error_calling_function = True                
            assert result == 252
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function get_estimate() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: get_estimate() should return 252 when the user enters s:1, m:2, l:3, xl:4, xxl:5, xxxl:6.</font>")

        
        i_test_num = i_test_num + 1

        # Test 2: Task 1: Test get_quantities() function
   
        error_calling_function = False
        try:
            try:
                result = sm.get_quantities()
            except:
                result = "Function get_quantities() crashed or is not defined"
                error_calling_function = True                
            assert result == (1, 2, 3, 4, 5, 6)
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function get_quantities() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: get_quantities() should return 1, 2, 3, 4, 5, 6 when the user enters s:1, m:2, l:3, xl:4, xxl:5, xxxl:6.</font>")
        i_test_num = i_test_num + 1


        # Test 3: Task 2: Test validate_combination() function with valid data

        error_calling_function = False
        try:
            try:
                result = sm.validate_combination(12, 33, 0)
            except:
                result = "Function validate_combination() crashed or is not defined"
                error_calling_function = True                
            assert result == True
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return True when given 3 valid numbers like 12, 33, 0.</font>")

        
        i_test_num = i_test_num + 1



        # Test 4: Task 2: Test validate_combination() function with invalid data: first number below 0

        error_calling_function = False
        try:
            try:
                result = sm.validate_combination(-1, 33, 0)
            except:
                result = "Function validate_combination() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with first number &#60; 0.</font>")

        
        i_test_num = i_test_num + 1


        # Test 5: Task 2: Test validate_combination() function with invalid data: second number below 0

        error_calling_function = False
        try:
            try:
                result = sm.validate_combination(33, -1, 0)
            except:
                result = "Function validate_combination() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with second number &#60; 0.</font>")

        i_test_num = i_test_num + 1



        # Test 6: Task 2: Test validate_combination() function with invalid data: third number below 0

        
        error_calling_function = False
        try:
            try:
                result = sm.validate_combination(12, 33, -1)
            except:
                result = "Function validate_combination() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with third number &#60; 0.</font>")

        i_test_num = i_test_num + 1

        # Test 7: Task 2: Test validate_combination() function with invalid data: first number above 39

        error_calling_function = False
        try:
            try:
                result = sm.validate_combination(40, 33, 0)
            except:
                result = "Function validate_combination() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with first number > 39.</font>")

        
        i_test_num = i_test_num + 1

        # Test 8: Task 2: Test validate_combination() function with invalid data: second number above 39

        error_calling_function = False
        try:
            try:
                result = sm.validate_combination(1, 40, 0)
            except:
                result = "Function validate_combination() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with second number > 39.</font>")

        i_test_num = i_test_num + 1

        # Test 9: Task 2: Test validate_combination() function with invalid data: third number above 39

        error_calling_function = False
        try:
            try:
                result = sm.validate_combination(20, 33, 40)
            except:
                result = "Function validate_combination() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with third number > 39.</font>")

        i_test_num = i_test_num + 1

        # Test 10: Task 2: Test validate_combination() function with invalid data: first number same as second number

        error_calling_function = False
        try:
            try:
                result = sm.validate_combination(33, 33, 0)
            except:
                result = "Function validate_combination() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with the same first and second numbers.</font>")

        i_test_num = i_test_num + 1

        # Test 11: Task 2: Test validate_combination() function with invalid data: second number same as third number

        error_calling_function = False
        try:
            try:
                result = sm.validate_combination(0, 33, 33)
            except:
                result = "Function validate_combination() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_combination() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_combination() should return False with the same second and third numbers.</font>")

        i_test_num = i_test_num + 1

        #####################

        # Test 12: Task 3: Test order_combo_meal() function with valid data
     
        try:
            try:
                result = sm.order_combo_meal(1, 2, 4)
            except:
                result = "Function order_combo_meal() crashed or is not defined"
                error_calling_function = True                                
            assert result == (8.97, True)
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function order_combo_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: order_combo_meal() should return 8.97 and True when given a sandwich, side, and drink with values of 1, 2, and 4 respectively.</font>")

        
        i_test_num = i_test_num + 1

        # Test 13: Task 3: Test order_combo_meal() function with invalid data: invalid sandwich < 1
        

        error_calling_function = False
        try:
            try:
                result = sm.order_combo_meal(0, 1, 1)
            except:
                result = "Function order_combo_meal() crashed or is not defined"
                error_calling_function = True                                
            assert result == (2.99, False)
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function order_combo_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: order_combo_meal() should return 2.99 and False when given a side and drink with values of 1 and a sandwich with a value of 0.</font>")

        i_test_num = i_test_num + 1

        # Test 14: Task 3: Test order_combo_meal() function with invalid data: invalid side < 1
 
        error_calling_function = False
        try:
            try:
                result = sm.order_combo_meal(1, 0, 1)
            except:
                result = "Function order_combo_meal() crashed or is not defined"
                error_calling_function = True                                
            assert result == (2.99, False)
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function order_combo_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: order_combo_meal() should return 2.99 and False when given a sandwich and drink with values of 1 and a side with a value of 0.</font>")

        i_test_num = i_test_num + 1

        # Test 15: Task 3: Test order_combo_meal() function with invalid data: invalid drink < 1
        
        error_calling_function = False
        try:
            try:
                result = sm.order_combo_meal(1, 1, 0)
            except:
                result = "Function order_combo_meal() crashed or is not defined"
                error_calling_function = True                                
            assert result == (3.98, False)
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function order_combo_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: order_combo_meal() should return 3.98 and False when given a sandwich and side with values of 1 and a drink with a value of 0.</font>")
 
        i_test_num = i_test_num + 1

        # Test 16: Task 3: Test get_item_price() function with valid data

        error_calling_function = False
        try:
            try:
                result = sm.get_item_price("drink", 4)
            except:
                result = "Function get_item_price() crashed or is not defined"
                error_calling_function = True                                
            assert result == 3.99
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function get_item_price() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: get_item_price() should return 3.99 when given a drink with a value of 4.</font>")

        i_test_num = i_test_num + 1

        # Test 17: Task 3: Test get_item_price() function with invalid data: invalid item name < 1
 
        error_calling_function = False
        try:
            try:
                result = sm.get_item_price("sandwich", -1)
            except:
                result = "Function get_item_price() crashed or is not defined"
                error_calling_function = True                                
            assert result == 0.0
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function get_item_price() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: get_item_price() should return 0.0 when given a sandwich with a value of -1.</font>")

        
        i_test_num = i_test_num + 1

        # Test 18: Task 3: Test get_item_price() function with invalid data: invalid item number > 4

        error_calling_function = False
        try:
            try:
                result = sm.get_item_price("sandwich", 5)
            except:
                result = "Function get_item_price() crashed or is not defined"
                error_calling_function = True                                
            assert result == 0.0
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function get_item_price() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: get_item_price() should return 0.0 when given a sandwich with a value of 5.</font>")

        
        i_test_num = i_test_num + 1

        # Test 19: Task 3: Test validate_meal() function with valid data

        error_calling_function = False
        try:
            try:
                result = sm.validate_meal(1, 1, 1)
            except:
                result = "Function validate_meal() crashed or is not defined"
                error_calling_function = True                                
            assert result == True
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return True when given a sandwich, side, and drink all with values of 1.</font>")

        
        i_test_num = i_test_num + 1

        # Test 20: Task 3: Test validate_meal() function with invalid data: invalid sandwich < 1
      
        error_calling_function = False
        try:
            try:
                result = sm.validate_meal(0, 1, 1)
            except:
                result = "Function validate_meal() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a sandwich with a value of 0.</font>")

        i_test_num = i_test_num + 1

        # Test 21: Task 3: Test validate_meal() function with invalid data: invalid side < 1

        error_calling_function = False
        try:
            try:
                result = sm.validate_meal(1, 0, 1)
            except:
                result = "Function validate_meal() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a side with a value of 0.</font>")

        i_test_num = i_test_num + 1

        # Test 22: Task 3: Test validate_meal() function with invalid data: invalid drink < 1

        error_calling_function = False
        try:
            try:
                result = sm.validate_meal(1, 1, 0)
            except:
                result = "Function validate_meal() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a drink with a value of 0.</font>")

        i_test_num = i_test_num + 1

        # Test 23: Task 3: Test validate_meal() function with invalid data: invalid sandwich > 3

        error_calling_function = False
        try:
            try:
                result = sm.validate_meal(4, 1, 1)
            except:
                result = "Function validate_meal() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a sandwich with a value of 4.</font>")

        
        i_test_num = i_test_num + 1

        # Test 24: Task 3: Test validate_meal() function with invalid data: invalid side > 2

        error_calling_function = False
        try:
            try:
                result = sm.validate_meal(1, 3, 1)
            except:
                result = "Function validate_meal() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a side with a value of 3.</font>")

        i_test_num = i_test_num + 1

        # Test 25: Task 3: Test validate_meal() function with invalid data: invalid drink > 4

        error_calling_function = False
        try:
            try:
                result = sm.validate_meal(1, 1, 5)
            except:
                result = "Function validate_meal() crashed or is not defined"
                error_calling_function = True                                
            assert result == False
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function validate_meal() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: validate_meal() should return False when given a drink with a value of 5.</font>")

        i_test_num = i_test_num + 1
        ########################################################################
        # End of tests
        ########################################################################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")

    return passes, error_msgs, assistant

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_05_student_submission.py")
	ret = queue.get()
	ret["result"] = passes
	queue.put(ret)
	return

def main():
	passes, error_msgs,assistant = autoGrader("lab_05_student_submission.py")
	assistant.displayWinow(passes, error_msgs)
	
if __name__ == "__main__":
    main()
