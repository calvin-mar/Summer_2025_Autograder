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
        error_msgs.append("There is a problem with your file.")
    else:
        specific_student.loader.exec_module(sm)
        ########################################################################
        # Start of tests #######################################################
        ########################################################################
        # Test 1: Task 1: Test double_it() 

        try:
            result = assistant.is_inf(sm.double_it, (0,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 0. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 0):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: double_it() should return 0 with argument 0, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function double_it() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        
        # Test 2: Task 1: Test double_it() function with 13

        try:
            result = assistant.is_inf(sm.double_it, (13,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 13. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 26):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: double_it() should return 26 with argument 13, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function double_it() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 3: Task 1: Test double_it() function with -27

        try:
            result = assistant.is_inf(sm.double_it, (-27,))
            if(result[1]):
                result[0] = result[0] + " The parameter was -27. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == -54):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: double_it() should return -54 with argument -27, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function double_it() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")


        ###

        # Test 4: Task 2: Test get_total() function

        l_data = shm.ShareableList([0, -9, 5, 77, -1], name="l_data")
        try:
            result = assistant.is_inf(sm.get_total)
            if(result[1]):
                result[0] = result[0] + " The inputs were 0, -9, 5, 77, -1. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 73):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: get_total() should return 73 when the user enters 0, -9, 5, 77, -1, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function get_total() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()  

        ###

        # Test 5: Task 3: Test calc_avg() function


        l_data = shm.ShareableList([5, 6, 2, -1], name="l_data")
        try:
            result = assistant.is_inf(sm.calc_avg)
            if(result[1]):
                result[0] = result[0] + " The inputs were 5, 6, 2, -1. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 4.333333333333333):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: calc_avg() should return 4.333333333333333 when the user enters 5, 6, 2, -1, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function calc_avg() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()

        ###

        
        # Test 6: Task 4: Test get_sum() function 


        l_data = shm.ShareableList([5, 6, 2, -1, 8], name="l_data")
        try:
            result = assistant.is_inf(sm.get_sum, (5,))
            if(result[1]):
                result[0] = result[0] + " The parameter given was 5 and the inputs were 5, 6, 2, -1, 8. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 20):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: get_sum() should return 20 when the user calls it with argument 5 and then enters 5, 6, 2, -1, 8, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function get_sum() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()


        ###

        
        # Test 7: Task 5: Test find_smallest() function 


        l_data = shm.ShareableList([100, 50, 60, 40, 70], name="l_data")
        try:
            result = assistant.is_inf(sm.find_smallest, (5,))
            if(result[1]):
                result[0] = result[0] + " The parameter given was 5 and the inputs were 100, 50, 60, 40, 70. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 40):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: find_smallest() should return 40 when the user calls it with argument 5 and then enters 100, 50, 60, 40, 70, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function find_smallest() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        l_data.shm.close()
        l_data.shm.unlink()


        ###

        
        # Test 8: Task 6: Test count_num_fives() function 


        l_data = shm.ShareableList([100, 5, 60, 5, 70, 1, 6, 5, 4, 77], name="l_data")
        try:
            result = assistant.is_inf(sm.count_num_fives, (10,))
            if(result[1]):
                result[0] = result[0] + " The parameter given was 10 and the inputs were 100, 5, 60, 5, 70, 1, 6, 5, 4, 77. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 3):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: count_num_fives() should return 3 when the user calls it with argument 10 and then enters 100, 5, 60, 5, 70, 1, 6, 5, 4, 77 but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function count_num_fives() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()


        



        ###

        
        # Test 9: Task 7: Test convert_euros_to_dollars() function 

        l_data = shm.ShareableList([2.5], name="l_data")
        try:
            result = assistant.is_inf(sm.convert_dollars_to_euros)
            if(result[1]):
                result[0] = result[0] + " The inputs was 2.5. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                                if(result[0] == 2.5*.89):
                                        passes.append(True)
                                else:
                                        passes.append(False)
                                        error_msgs.append(" Failed: convert_dollars_to_euros() should return 2.225 when the user enters 2.5 but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function convert_dollars_to_euros() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        l_data.shm.close()
        l_data.shm.unlink()


        ###

        
        # Test 10: Task 8: Test is_even() function with even number argument

        try:
            result = assistant.is_inf(sm.is_even, (22,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 22. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_even() should return True when the user enters 22 but it returns " + str(result[0]) + ".</font>")     
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_even() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ###

        # Test 11: Task 8: Test is_even() function with odd number argument


        try:
            result = assistant.is_inf(sm.is_even, (21,))
            if(result[1]):
                result[0] = result[0] + " The parameter was 21. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: is_even() should return False when the user enters 21 but it returns " + str(result[0]) + ".</font>")     
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function is_even() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ###

        # Test 12: Task 9: Test count_evens() function with args of smaller, larger


        try:
            result = assistant.is_inf(sm.count_evens, (2,8))
            if(result[1]):
                result[0] = result[0] + " The parameters were 2, 8. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 2):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: count_evens() should return 2 when the arguments are 2 and 8, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function count_evens() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 13: Task 9: Test count_evens() function with args of larger, smaller



        try:
            result = assistant.is_inf(sm.count_evens, (8,2))
            if(result[1]):
                result[0] = result[0] + " The parameters were 8, 2. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 2):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: count_evens() should return 2 when the arguments are 8 and 2, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function count_evens() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 14: Task 10: Test temp_monitor() function with arg 60.5 which returns the wrong value until the function is fixed



        try:
            result = assistant.is_inf(sm.temp_monitor, (60.5, ))
            if(result[1]):
                result[0] = result[0] + " The parameters were 8, 2. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "pleasant"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: temp_monitor() should return pleasant for argument 60.5.</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function temp_monitor() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")
    
    return passes, error_msgs, assistant

def testing():
    passes, error_msgs,assistant = autoGrader("lab_07_student_submission.py")
    return passes

def main():
    testSets=[3, 1, 1, 1, 1, 1, 1, 2, 2, 1]
    passes, error_msgs,assistant = autoGrader("lab_07_student_submission.py")
    assistant.displayWindow(passes, error_msgs, testSets)
    
if __name__ == "__main__":
    main()

