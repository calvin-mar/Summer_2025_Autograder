# Python imports
import sys
import ast
import astor
import re
import os
import importlib.util
from multiprocessing import shared_memory as shm

def autoGrader(student_submission):
    #Making sure shared memory file does not already exist
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
        if s_error_msg != "":
            error_msgs.append(s_error_msg)
        else:
            error_msgs.append("There is a problem with your file.")

    else:
        specific_student.loader.exec_module(sm)
        ########################################################################
        # Start of tests #######################################################
        ########################################################################
        
        # Test 1: Task 1: Test biggest_smallest_number() 

        l_data = shm.ShareableList([100, 80, 30, 90, 20, 10, 50, 40, 70, 60], name="l_data")
        try:
            result = assistant.is_inf(sm.biggest_smallest_number)
            if(result[1]):
                result[0] = result[0] + " The inputs were 100, 80, 30, 90, 20, 10, 50, 40, 70, 60. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (100,10)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_smallest_number() should return 100 and 10 when the user enters 100, 80, 30, 90, 20, 10, 50, 40, 70, 60, but it returns " + str(result[0][0]) + " and " + str(result[0][1]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_smallest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()


        # Test 2: Task 1: Test biggest_smallest_number() function with biggest in 10th (last) position and smallest in 1st position
        
        
        
        l_data = shm.ShareableList([50, 20, 80, 40, 10, 70, 90, 60, 30, 100], name="l_data")
        try:
            result = assistant.is_inf(sm.biggest_smallest_number)
            if(result[1]):
                result[0] = result[0] + " The inputs were 50, 20, 80, 40, 10, 70, 90, 60, 30, 100. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (100,10)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_smallest_number() should return 100 and 10 when the user enters 50, 20, 80, 40, 10, 70, 90, 60, 30, 100, but it returns " + str(result[0][0]) + " and " + str(result[0][1]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_smallest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()

        # Test 3: Task 1: Test biggest_smallest_number() function with biggest in 5th position and smallest in 10th (last) position
        
        
        
        l_data = shm.ShareableList([40, 70, 30, 80, 100, 90, 60, 10, 20, 50], name="l_data")
        try:
            result = assistant.is_inf(sm.biggest_smallest_number)
            if(result[1]):
                result[0] = result[0] + " The inputs were 40, 70, 30, 80, 100, 90, 60, 10, 20, 50. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (100,10)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_smallest_number() should return 100 and 10 when the user enters 40, 70, 30, 80, 100, 90, 60, 10, 20, 50, but it returns " + str(result[0][0]) + " and " + str(result[0][1]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_smallest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()

        



        # Test 4: Task 1: Test biggest_smallest_number() function with biggest in 5th position and smallest in 3rd position but all numbers are negative
        
        
        l_data = shm.ShareableList([-50, -80, -100, -30, -10, -20, -70, -90, -60, -40], name="l_data")
        try:
            result = assistant.is_inf(sm.biggest_smallest_number)
            if(result[1]):
                result[0] = result[0] + " The inputs were -50, -80, -100, -30, -10, -20, -70, -90, -60, -40. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (-10, -100)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: biggest_smallest_number() should return -10 and -100 when the user enters -50, -80, -100, -30, -10, -20, -70, -90, -60, -40, but it returns " + str(result[0][0]) + " and " + str(result[0][1]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function biggest_smallest_number() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()
  
        ######################
 
        # Test 5: Task 2: Test repeated_doubler() function - double 5 4 times
        
        try:
            result = assistant.is_inf(sm.repeated_doubler, (5,4))
            if(result[1]):
                result[0] = result[0] + " The parameters were 5, 4. </font>"
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
            result = assistant.is_inf(sm.repeated_doubler, (0, 3))
            if(result[1]):
                result[0] = result[0] + " The parameters were 0, 3. </font>"
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
            result = assistant.is_inf(sm.fib_num, (1,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 1. </font>"
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
            result = assistant.is_inf(sm.fib_num, (2,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 2. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 1):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: fib_num() should return 0 when the argument is 1, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function fib_num() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 9: Task 3: Test fib_num() function - 3rd fib is 1
        
        
        try:
            result = assistant.is_inf(sm.fib_num, (3,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 3. </font>"
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
            result = assistant.is_inf(sm.fib_num, (4,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 4. </font>"
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
            result = assistant.is_inf(sm.fib_num, (9,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 9. </font>"
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
            result = assistant.is_inf(sm.fib_num, (16,))
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
        # Test 13: Task 4: Test leaf_sum() function with argument 4 for 4 days with values of 1, 2, 3, 4 for a total of 10 leaves
        
        
        l_data = shm.ShareableList([1,2,3,4], name="l_data")
        try:
            result = assistant.is_inf(sm.leaf_sum, (4,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 4 and the inputs were 1, 2, 3, 4. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 10):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: leaf_sum() should return 10 when the argument is 4 and values entered are 1, 2, 3 and 4, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function leaf_sum() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()


        
        ######################

        # Test 14: Task 5: Test class_leaf_sum() function with argument 3 for 3 students.  This will then call leaf sum for each student.  Student 1: 2 days, 9 + 8 leaves.  Student 2: 3 days, 1 + 1 + 1 leaves.  Student 3: 4 days, 4 +5 + 6 + 5 leaves.  Total 40 leaves.
        
        
        l_data = shm.ShareableList([2, 9, 8, 3, 1, 1, 1, 4, 4, 5, 6, 5], name="l_data")
        try:
            result = assistant.is_inf(sm.class_leaf_sum, (3,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 3 and the inputs were 2, 9, 8, 3, 1, 1, 1, 4, 4, 5, 6, 5. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 40):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: class_leaf_sum() should return 40 when the argument is 3 and values entered are (Student 1: 2 days, 9 + 8 leaves.  Student 2: 3 days, 1 + 1 + 1 leaves.  Student 3: 4 days, 4 +5 + 6 + 5 leaves), but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function class_leaf_sum() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()

        


        ######################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")
    
    return passes, error_msgs, assistant

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_08_student_submission.py")
	return passes

def main():
    testSets = [4, 2, 6, 1, 1]
    passes, error_msgs,assistant = autoGrader("lab_08_student_submission.py")
    assistant.displayWindow(passes, error_msgs, testSets)
	
if __name__ == "__main__":
    main()
