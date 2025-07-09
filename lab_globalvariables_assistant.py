## This autograder is non-functioning. This is a template to demonstrate how to construct an autograder module for a new lab.
## Specifically this assistant template is to demonstrate how to construct an autograder to test a lab with global variables
## This template is divided into 5 functions

## Function 1: autoGrader
## This function is called from the autograder assistant in order to run the specific tests for a given lab
## To create the autograder copy the portion between "Start of Test" and "End of Test".
## Provide the function to be tested, parameters and inputs as necessary, and the correct result

## Function 2: loadAssistant
## This function is called in order to load the assistant so that it's function may be used by the autograder
## In particular it calls the main displayWindow function and the syntax checker

## Function 3: getTestsNum
## This function only returns the number of tests to test_all_submissions in order to accurately measure the progress bar

## Function 4: testing
## This function is called by test_all_submissions in order to return only the results and not run the window

## Function 5: main
## This function is called when the file is run directly from idle. This calls the displayWindow from the assistant.
## The loading window is displayed while the autograder runs and the results are afterwards displayed


# The following are the required imports
# Python imports
import sys
import ast
import astor
import re
import os
import importlib.util
from multiprocessing import shared_memory as shm
import multiprocessing


def autoGrader(student_submission, window):
    '''
    This function takes three arguments: student_submission, assistant, and window
    student_submission is the name of the file the student submitted to test.
    assistant is loaded module of autograder_assistant
    window is the active display window running from either autograder_assistant or test_all_submissions

    This function returns two lists: passes and s_error_msgs
    passes is a list of bools indicating whether the ith test passed or not
    error_msgs are append for each failed test and are accessed to be displayed in autograder_assistant
    '''

    # Ensure that the shareable list does not currently exist, if so delete it
    try:
        l_data = shm.ShareableList(sequence=None, name="l_data")
        l_data.shm.close()
        l_data.shm.unlink()
    except:
        pass


    # Initialize the output variables
    passes = []
    error_msgs = []

    # Initialize the input list for the entirety of the submission
    l_data = shm.ShareableList([value1,value2,value3], name="l_data")

    i_test_num = 1

    # This if else is necessary to ensure that the exectuables are able to locate the appropriate files
    print("Autograder starting...")
    if getattr(sys, "frozen", False):
        dir_path = os.path.dirname(sys.executable)
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))

    name = student_submission[:-3]
    specific_student = importlib.util.spec_from_file_location(name, os.path.join(dir_path, student_submission))
    sm = importlib.util.module_from_spec(specific_student)



    b_proceed, s_error_msg = window.syntax_checker(os.path.join(dir_path, student_submission))
    ## The first set of inputs is used in the syntax_checker to look for infinite loops, l_data must be closed and remade
    l_data.shm.close()
    l_data.shm.unlink()
    
    if b_proceed == False:
        passes.append(False)
        if s_error_msg != "":
            error_msgs.append(s_error_msg)
        else:
            error_msgs.append("There is a problem with your file.")
    else:
        ## Remake l_data for the inputs of the student submission
        l_data = shm.ShareableList([value1,value2,value3], name="l_data")
        specific_student.loader.exec_module(sm)

        


        ########################################################################
        # Start of tests #######################################################
        ########################################################################

        ######################### Start of Test n: Task k: Test global_variable #############################
        try:

            ## Additonal input variables may be added
            ## Similarly multiple correct answers may be compared against multiple variable in the submission
            input_variable = sm.input_variable
            correct_answer1 = solution_calculation1(input_variable)
            correct_answer2 = solution_calculation2(input_variable)
           # __________OR___________ #
            correct_answer1
            correct_answer2
            

            
            assert sm.final_answer1 == correct_answer1
            assert sm.final_answer2 == correct_answer2
 
            passes.append(True)
        except:
            passes.append(False)
            try:
                error_msgs.append("Failed: " + str(correct_answer1) + " and " + str(correct_answer2) + "expected, but " +str(sm.final_answer1) + " and " + str(sm.final_answer2) + " received. </font>")
            except:
                error_msgs.append(" Failed:  variables are not named correctly or have incorrect values.</font>")


        
        ###################################### End of Test ##############################################


        ########################################################################
        # End of tests
        ########################################################################
        l_data.shm.close()
        l_data.shm.unlink()

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")
    
    return passes, error_msgs

def getTestSets():
    '''
    This function returns the TestSets
    TestSets is a list representing how the tests are organized into tasks in the lab.
    
    For example: Lab 6 has 22 tests divided into 5 tasks. Task 1 contains 4 tests, task 2 has 2 tests, etc.
                 Thus lab 6 has the line -> testsSets = [4,2,6,3,7]


    '''
    return [4]

def testing(window):
        '''
    This function takes the window from testing_all_submissions
    It proceeds to fun the autograder and return student passes
    It does not return the error messages

    This function is called from testing_all_submissions
    '''
    passes, error_msgs = autoGrader("lab_02_student_submission.py", window)
    return passes
