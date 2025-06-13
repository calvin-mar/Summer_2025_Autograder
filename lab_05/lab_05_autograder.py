# Python imports
import sys
import ast
import astor
import re
import os
import importlib.util
from multiprocessing import shared_memory as shm

def autoGrader(sm, assistant):
    try:
        l_data = shm.ShareableList(sequence=None, name="l_data")
        l_data.shm.close()
        l_data.shm.unlink()
    except:
        pass
    
    passes = []
    error_msgs = []
    print("Autograder starting...")

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

        # Test 1: Task 1: Test get_estimate()


        l_data = shm.ShareableList([1, 2, 3, 4, 5, 6], name="l_data")
        try:
            result = assistant.testFunction(sm.get_estimate)
            if(result[1]):
                result[0] = result[0] + " The inputs were 1, 2, 3, 4, 5, 6. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 252):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: get_estimate() should return 252 when the user enters s:1, m:2, l:3, xl:4, xxl:5, xxxl:6. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function get_estimate() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()

        # Test 2: Task 1: Test get_quantities() function


        l_data = shm.ShareableList([1, 2, 3, 4, 5, 6], name="l_data")
        try:
            result = assistant.testFunction(sm.get_quantities)
            if(result[1]):
                result[0] = result[0] + " The inputs were 1, 2, 3, 4, 5, 6. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (1, 2, 3, 4, 5, 6)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: get_quantities() should return 1, 2, 3, 4, 5, 6 when the user enters s:1, m:2, l:3, xl:4, xxl:5, xxxl:6. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function get_quantities() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        l_data.shm.close()
        l_data.shm.unlink()



        # Test 3: Task 2: Test validate_combination() function with valid data

        try:
            result = assistant.testFunction(sm.validate_combination, (12, 33, 0))
            if(result[1]):
                result[0] = result[0] + " The values were 12, 33, 0. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_combination() should return True when given 3 valid numbers like 12, 33, 0. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_combination() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 4: Task 2: Test validate_combination() function with invalid data: first number below 0

        try:
            result = assistant.testFunction(sm.validate_combination, (-1, 33, 0))
            if(result[1]):
                result[0] = result[0] + " The values were -1, 33, 0. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_combination() should return False with first number &#60; 0.</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_combination() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")


        # Test 5: Task 2: Test validate_combination() function with invalid data: second number below 0

        try:
            result = assistant.testFunction(sm.validate_combination, (33, -1, 0))
            if(result[1]):
                result[0] = result[0] + " The values were 33, -1, 0. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_combination() should return False with second number &#60; 0. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_combination() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 6: Task 2: Test validate_combination() function with invalid data: third number below 0
        
        try:
            result = assistant.testFunction(sm.validate_combination, (12, 33, -1))
            if(result[1]):
                result[0] = result[0] + " The values were 12, 33, -1. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_combination() should return False with third number &#60; 0. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_combination() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 7: Task 2: Test validate_combination() function with invalid data: first number above 39

        try:
            result = assistant.testFunction(sm.validate_combination, (40, 33, 0))
            if(result[1]):
                result[0] = result[0] + " The values were 40, 33, 0. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_combination() should return False with first number > 39. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_combination() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 8: Task 2: Test validate_combination() function with invalid data: second number above 39
        try:
            result = assistant.testFunction(sm.validate_combination, (1, 40, 0))
            if(result[1]):
                result[0] = result[0] + " The values were 1, 40, 0. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_combination() should return False with second number > 39. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_combination() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 9: Task 2: Test validate_combination() function with invalid data: third number above 39
        
        try:
            result = assistant.testFunction(sm.validate_combination, (20, 33, 40))
            if(result[1]):
                result[0] = result[0] + " The values were 20, 33, 40. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_combination() should return False with third number > 39. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_combination() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 10: Task 2: Test validate_combination() function with invalid data: first number same as second number
        try:
            result = assistant.testFunction(sm.validate_combination, (33, 33, 0))
            if(result[1]):
                result[0] = result[0] + " The values were 33, 33, 0. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_combination() should return False with the same first and second numbers.</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_combination() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 11: Task 2: Test validate_combination() function with invalid data: second number same as third number
        try:
            result = assistant.testFunction(sm.validate_combination, (0, 33, 33))
            if(result[1]):
                result[0] = result[0] + " The values were 0, 33, 33. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_combination() should return False with the same second and third numbers. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_combination() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        #####################

        # Test 12: Task 3: Test order_combo_meal() function with valid data
        try:
            result = assistant.testFunction(sm.order_combo_meal, (1,2,4))
            if(result[1]):
                result[0] = result[0] + " The parameters were 1,2,4. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (8.97, True)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: order_combo_meal() should return 8.97 and True when given a sandwich, side, and drink with values of 1, 2, and 4 respectively. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function order_combo_meal() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 13: Task 3: Test order_combo_meal() function with invalid data: invalid sandwich < 1
        try:
            result = assistant.testFunction(sm.order_combo_meal, (0, 1, 1))
            if(result[1]):
                result[0] = result[0] + " The parameters were 0, 1, 1. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (2.99, False)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: order_combo_meal() should return 2.99 and False when given a side and drink with values of 1 and a sandwich with a value of 0. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function order_combo_meal() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 14: Task 3: Test order_combo_meal() function with invalid data: invalid side < 1

        try:
            result = assistant.testFunction(sm.order_combo_meal, (1,0,1))
            if(result[1]):
                result[0] = result[0] + " The parameters were 1, 0, 1. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (2.99, False)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: order_combo_meal() should return 2.99 and False when given a sandwich and drink with values of 1 and a side with a value of 0. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function order_combo_meal() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 15: Task 3: Test order_combo_meal() function with invalid data: invalid drink < 1

        try:
            result = assistant.testFunction(sm.order_combo_meal, (1,1,0))
            if(result[1]):
                result[0] = result[0] + " The parameters were 1, 1 , 0. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (3.98, False)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: order_combo_meal() should return 3.98 and False when given a sandwich and side with values of 1 and a drink with a value of 0. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function order_combo_meal() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 16: Task 3: Test get_item_price() function with valid data
        try:
            result = assistant.testFunction(sm.get_item_price, ("drink", 4))
            if(result[1]):
                result[0] = result[0] + " The parameters were \"drink\", 4. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 3.99):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: get_item_price() should return 3.99 when given a drink with a value of 4. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function get_item_price() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                
        # Test 17: Task 3: Test get_item_price() function with invalid data: invalid item name < 1
        try:
            result = assistant.testFunction(sm.get_item_price, ("sandwich", -1))
            if(result[1]):
                result[0] = result[0] + " The parameters were \"sandwich\", -1. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 0.0):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: get_item_price() should return 0.0 when given a sandwich with a value of -1. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function get_item_price() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
                 
        # Test 18: Task 3: Test get_item_price() function with invalid data: invalid item number > 4

        try:
            result = assistant.testFunction(sm.get_item_price, ("sandwich", 5))
            if(result[1]):
                result[0] = result[0] + " The parameters were \"sandwich\", 5. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 0.0):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: get_item_price() should return 0.0 when given a sandwich with a value of 5. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function get_item_price() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 19: Task 3: Test validate_meal() function with valid data
        try:
            result = assistant.testFunction(sm.validate_meal, (1, 1, 1))
            if(result[1]):
                result[0] = result[0] + " The parameters were 1, 1, 1. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_meal() should return True when given a sandwich, side, and drink all with values of 1. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_meal() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 20: Task 3: Test validate_meal() function with invalid data: invalid sandwich < 1
        try:
            result = assistant.testFunction(sm.validate_meal, (0, 1, 1))
            if(result[1]):
                result[0] = result[0] + " The parameters were 0, 1, 1. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_meal() should return False when given a sandwich with a value of 0. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_meal() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 21: Task 3: Test validate_meal() function with invalid data: invalid side < 1
        try:
            result = assistant.testFunction(sm.validate_meal, (1, 0, 1))
            if(result[1]):
                result[0] = result[0] + " The parameters were 1, 0, 1. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_meal() should return False when given a side with a value of 0. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_meal() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 22: Task 3: Test validate_meal() function with invalid data: invalid drink < 1
        try:
            result = assistant.testFunction(sm.validate_meal, (1, 1, 0))
            if(result[1]):
                result[0] = result[0] + " The parameters were 1, 1, 0. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_meal() should return False when given a drink with a value of 0. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_meal() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 23: Task 3: Test validate_meal() function with invalid data: invalid sandwich > 3
        try:
            result = assistant.testFunction(sm.validate_meal, (4, 1, 0))
            if(result[1]):
                result[0] = result[0] + " The parameters were 4, 1, 0. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_meal() should return False when given a sandwich with a value of 4. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_meal() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 24: Task 3: Test validate_meal() function with invalid data: invalid side > 2
        try:
            result = assistant.testFunction(sm.validate_meal, (1, 3, 1))
            if(result[1]):
                result[0] = result[0] + " The parameters were 1, 3, 1. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_meal() should return False when given a side with a value of 3. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_meal() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 25: Task 3: Test validate_meal() function with invalid data: invalid drink > 4
        try:
            result = assistant.testFunction(sm.validate_meal, (1, 1, 5))
            if(result[1]):
                result[0] = result[0] + " The parameters were 1, 1, 5. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: validate_meal() should return False when given a drink with a value of 5. Instead it returned " + str(result[0]) + "</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function validate_meal() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ########################################################################
        # End of tests
        ########################################################################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")

    return passes, error_msgs, assistant

def loadAssistant():
    if getattr(sys, "frozen", False):
        dir_path = os.path.dirname(sys.executable)
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))

    specific = importlib.util.spec_from_file_location("autograder_assistant", os.path.join(dir_path, "autograder_assistant.py"))
    assistant = importlib.util.module_from_spec(specific)
    specific.loader.exec_module(assistant)

    name = student_submission[:-3]
    specific_student = importlib.util.spec_from_file_location(name, os.path.join(dir_path, student_submission))
    sm = importlib.util.module_from_spec(specific_student)
    return assistant

def testing():
    assistant = loadAssistant()
    passes, error_msgs,assistant = autoGrader("lab_02_student_submission.py", assistant)
    return passes

def main():
    assistant = loadAssistant()
    assistant.displayWindow(autoGrader, "lab_02_student_submission.py", assistant, testSets)

if __name__ == "__main__":
    main()
