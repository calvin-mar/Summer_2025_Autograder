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

        # Test 1: Task 1: Test my_len function with list []
        
        try:
            result = assistant.testFunction(sm.my_len, ([],))
            if(result[1]):
                result[0] = result[0] + " The parameter was an empty list. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 0):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_len() should return 0 with an empty list argument, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_len() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 2: Task 1: Test my_len() function with list [8, 6, 7, 5, 3]
        
        
        try:
            result = assistant.testFunction(sm.my_len, ([8, 6, 7, 5, 3],))
            if(result[1]):
                result[0] = result[0] + " The parameter was [8, 6, 7, 5, 3]. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 5):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_len() should return 5 with this list [8, 6, 7, 5, 3] as an argument, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_len() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ###

        # Test 3: Task 2: Test my_in_list() function with list [8, 6, 7, 5, 3] and integer 0
        
        
        try:
            result = assistant.testFunction(sm.my_in_list, ([8, 6, 7, 5, 3],0))
            if(result[1]):
                result[0] = result[0] + " The parameters were [8, 6, 7, 5, 3] and 0. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_in_list() should return False with this list [8, 6, 7, 5, 3] and 0 as arguments, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_in_list() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 4: Task 2: Test my_in_list() function with list [8, 6, 7, 5, 3] and integer 8
        
        
        try:
            result = assistant.testFunction(sm.my_in_list, ([8, 6, 7, 5, 3], 8))
            if(result[1]):
                result[0] = result[0] + " The parameters were [8, 6, 7, 5, 3] and 8. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_in_list() should return True with this list [8, 6, 7, 5, 3] and 8 as arguments, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_in_list() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

         # Test 5: Task 2: Test my_in_list() function with list [8, 6, 7, 5, 3] and integer 3
        
        
        try:
            result = assistant.testFunction(sm.my_in_list, ([8, 6, 7, 5, 3], 3))
            if(result[1]):
                result[0] = result[0] + " The parameters were [8, 6, 7, 5, 3] and 3. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_in_list() should return True with this list [8, 6, 7, 5, 3] and 3 as arguments, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_in_list() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ###

        # Test 6: Task 3: Test my_location() function with list [8, 6, 8, 5, 3] and integer 8
        
        try:
            result = assistant.testFunction(sm.my_location, ([8, 6, 8, 5, 3], 8))
            if(result[1]):
                result[0] = result[0] + " The parameters were [8, 6, 8, 5, 3] and 8. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 0):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_location() should return 0 with this list [8, 6, 8, 5, 3] and 8 as arguments, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_location() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 7: Task 3: Test my_location() function with list [8, 6, 8, 5, 3] and integer 77
        
        
        try:
            result = assistant.testFunction(sm.my_location, ([8, 6, 8, 5, 3], 77))
            if(result[1]):
                result[0] = result[0] + " The parameters were [8, 6, 8, 5, 3] and 77. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == -1):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_location() should return -1 with this list [8, 6, 8, 5, 3] and 77 as arguments, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_location() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ###
        
        # Test 8: Task 4: Test my_reverse() function with list [8, 6, 8, 5, 3] 
        
        try:
            result = assistant.testFunction(sm.my_reverse, ([8, 6, 8, 5, 3],))
            if(result[1]):
                result[0] = result[0] + " The parameter was [8, 6, 8, 5, 3]. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == [3, 5, 8, 6, 8]):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_reverse() should return [3, 5, 8, 6, 8] with this list [8, 6, 7, 5, 3] argument, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_reverse() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ###
        
        # Test 9: Task 5: Test my_extrema() function with list [77, 6, -1, 5, 3] 
        
        
        try:
            result = assistant.testFunction(sm.my_extrema, ([77, 6, -1, 5, 3],))
            if(result[1]):
                result[0] = result[0] + " The parameter was [77, 6, -1, 5, 3]. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (-1,77)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_extrema() should return -1 and 77 with this list [77, 6, -1, 5, 3] argument, but it returns " + str(result[0][0]) + " and " + str(result[0][1]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_extrema() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 10: Task 5: Test my_extrema() function with list [-1, 6, 3, 5, 77] 
        
        try:
            result = assistant.testFunction(sm.my_extrema, ([-1, 6, 3, 5, 77],))
            if(result[1]):
                result[0] = result[0] + " The parameter was [77, 6, -1, 5, 3]. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (-1,77)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_extrema() should return -1 and 77 with this list [-1, 6, 3, 5, 77] argument, but it returns " + str(result[0][0]) + " and " + str(result[0][1]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_extrema() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")    

        # Test 11: Task 5: Test my_extrema() function with list [6, 77, 3, 5, -1] 
        
        try:
            result = assistant.testFunction(sm.my_extrema, ([6, 77, 3, 5, -1],))
            if(result[1]):
                result[0] = result[0] + " The parameter was [6, 77, 3, 5, -1]. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == (-1,77)):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_extrema() should return -1 and 77 with this list [6, 77, 3, 5, -1] argument, but it returns " + str(result[0][0]) + " and " + str(result[0][1]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_extrema() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")    

        ###

        # Test 12: Task 6: Test my_count() function with list [6, 77, 3, 5, -1] and 99
        
        try:
            result = assistant.testFunction(sm.my_count, ([6, 77, 3, 5, -1], 99))
            if(result[1]):
                result[0] = result[0] + " The parameters were [6, 77, 3, 5, -1], 99. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 0):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_count() should return 0 with this list [6, 77, 3, 5, -1] and 99 as argument, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_count() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")    

        # Test 13: Task 6: Test my_count() function with list [6, 77, 3, 5, 77] and 77
        
        try:
            result = assistant.testFunction(sm.my_count, ([6, 77, 3, 5, 77], 77))
            if(result[1]):
                result[0] = result[0] + " The parameters were [6, 77, 3, 5, -1], 77. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 2):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_count() should return 2 with this list [6, 77, 3, 5, 77] and 77 as argument, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_count() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")    

        ###

        # Test 14: Task 7: Test my_insert() function with list [0, 1, 2, 3, 4], 0, and "X"
        
        try:
            result = assistant.testFunction(sm.my_insert, ([0, 1, 2, 3, 4], 0, "X"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were [6, 77, 3, 5, -1], 0, and "X". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == ["X", 0, 1, 2, 3, 4]):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_insert() should return [\"X\", 0, 1, 2, 3, 4] with this list [0, 1, 2, 3, 4], 0, and \"X\" as argument, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_insert() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")    

        # Test 15: Task 7: Test my_insert() function with list [0, 1, 2, 3, 4], 4, and "X"
           
        try:
            result = assistant.testFunction(sm.my_insert, ([0, 1, 2, 3, 4], 4, "X"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were [6, 77, 3, 5, -1], 4, and "X". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == [0, 1, 2, 3, "X", 4]):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_insert() should return [0, 1, 2, 3, \"X\", 4] with this list [0, 1, 2, 3, 4], 4, and \"X\" as argument, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_insert() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")    

        ###

        # Test 16: Task 8: Test my_remove() function with list [0, 1, 2, 3, 4, 1, 2, 1, 2], 1
        
        try:
            result = assistant.testFunction(sm.my_remove, ([0, 1, 2, 3, 4, 1, 2, 1, 2], 1))
            if(result[1]):
                result[0] = result[0] + ' The parameters were [0, 1, 2, 3, 4, 1, 2, 1, 2], 1. </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == [0, 2, 3, 4, 2, 2]):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_remove() should return [0, 2, 3, 4, 2, 2] with this list [0, 1, 2, 3, 4, 1, 2, 1, 2] and 1, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_remove() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")            

        # Test 17: Task 8: Test my_remove() function with list [0, 1, 2, 3, 4, 1, 2, 1, 2], 11
        
        try:
            result = assistant.testFunction(sm.my_remove, ([0, 1, 2, 3, 4, 1, 2, 1, 2], 11))
            if(result[1]):
                result[0] = result[0] + ' The parameters were [0, 1, 2, 3, 4, 1, 2, 1, 2], 11. </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == [0, 1, 2, 3, 4, 1, 2, 1, 2]):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_remove() should return [0, 1, 2, 3, 4, 1, 2, 1, 2] with this list [0, 1, 2, 3, 4, 1, 2, 1, 2] and 11, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_remove() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")            

        ###

        # Test 18: Task 9: Test my_sort() function with list [8, 7, 6, 5, 4, 3, 2, 1, 0]
        
        
        try:
            result = assistant.testFunction(sm.my_sort, ([8, 7, 6, 5, 4, 3, 2, 1, 0],))
            if(result[1]):
                result[0] = result[0] + ' The parameters was [8, 7, 6, 5, 4, 3, 2, 1, 0. </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == [0, 1, 2, 3, 4, 5, 6, 7, 8]):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_sort() should return [0, 1, 2, 3, 4, 5, 6, 7, 8] with this list [8, 7, 6, 5, 4, 3, 2, 1, 0], but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_remove() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")            

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
    return assistant

def testing():
    assistant = loadAssistant()
    passes, error_msgs,assistant = autoGrader("lab_06_student_submission.py", assistant)
    return passes

def main():
    assistant = loadAssistant()
    testSets = [4, 2, 6, 3, 5, 2]
    assistant.displayWindow(autoGrader, "lab_06_student_submission.py", assistant, testSets)
    
if __name__ == "__main__":
    main()
