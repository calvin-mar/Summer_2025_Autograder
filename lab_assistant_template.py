## This autograder is non-functioning. This is a template to demonstrate how to construct an autograder module for a new lab.
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
import math
import importlib.util
from multiprocessing import shared_memory as shm
from multiprocessing import freeze_support

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
    # Initialize the output variables
    passes = []
    error_msgs = []
    
    print("Autograder starting...")


    # This if else is necessary to ensure that the exectuables are able to locate the appropriate files
    if getattr(sys, "frozen", False):
        dir_path = os.path.dirname(sys.executable)
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))

    # Ensure that the shareable list does not currently exist, if so delete it
    try:
        l_data = shm.ShareableList(sequence=None, name="l_data")
        l_data.shm.close()
        l_data.shm.unlink()
    except:
        pass

    # Import the student submission dynamically
    name = student_submission[:-3]
    specific_student = importlib.util.spec_from_file_location(name, os.path.join(dir_path, student_submission))
    sm = importlib.util.module_from_spec(specific_student)

    TIMEOUT = 30

    # Run the syntax checker module from the autograder_assistant
    # The syntax checker looks for global infinite loops, banned syntax, and missing input header
    b_proceed, s_error_msg = assistant.syntax_checker(os.path.join(dir_path, student_submission), window, TIMEOUT)


    # If the syntax_checker finds an issue, this prevents the code from running any other tests
    if b_proceed == False:
        passes.append(False)
        if(s_error_msg != ""):
            error_msgs.append(s_error_msg)
        else:
            error_msgs.append("There is a problem with your file")
    else:
        # Load student submission as a runnable module as sm
        specific_student.loader.exec_module(sm)

        ########################################################################
        # Start of tests #######################################################
        ########################################################################


        ############ Start of Test n: Task k: Test function() with inputs = x* and parameters = y*    ##################

        # Initialize the shareableList so that the input statements have access to all necessary inputs
        l_data = shm.ShareableList([x*], name="l_data")
        try:
            # Run the testFunction from the autograder_assistant or test_all_submissions.
            # This function catches most errors and will test for an infinite loop
            # The result returned will be of the form [output, boolean]
            # The output is the regular output from the function and the boolean indicates if the function contained an error


            # Note: on this line that the sm.function_name does not have parantheses
            # Note: if there is only one parameter, the tuple ought to have a comma to indicate that is a tuple
            result = window.testFunction(sm.function, (y*,))
            
            if(result[1]):
                # If an error occurs, rather than nothing, result contains the error message
                # Here the inputs and parameters are appended to the message in order to let the student run their own tests
                result[0] = result[0] + " The inputs were x* and the parameters were y*. </font>"
                error_msgs.append(result[0])
                passes.append(False)
                
            else:
                # If no error occurs, test if the answer is correct
                if(result[0] == correct_result):
                    passes.append(True)
                    # Note: No message needs to appended since all passes have the same message and it is handled in autograder_assistant
                else:
                    # If there is an incorrect result, display the correct answer, inputs, parameters, and what the function returned
                    passes.append(False)
                    error_msgs.append(" Failed: function() should return correct_result when the user enters x* and y*, but it returns " + str(result[0]) + ".</font>")
        except:
            # This catches extra errors from the function crashing. The most likely occurrence is the function being undefined
            passes.append(False)
            error_msgs.append(" Failed: Function function() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Close and unlink the shareable list to prepare for a new set of inputs
        # This is necessary because the length and size of inputs may change between tests
        l_data.shm.close()
        l_data.shm.unlink()
        
        ###################################### End of Test ##############################################

        # Tests may be added as necessary by copying the above code and replacing variables
        
        ########################################################################
        # End of tests
        ########################################################################

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
    return [1]

def testing(window):
    '''
    This function takes the window from testing_all_submissions
    It proceeds to fun the autograder and return student passes
    It does not return the error messages

    This function is called from testing_all_submissions
    '''
    passes, error_msgs = autoGrader("lab_\d\d_student_submission.py", window)
    return passes
