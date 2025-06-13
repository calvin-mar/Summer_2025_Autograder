# Python imports
import sys
import math
import ast
import astor
import re
import importlib.util
import os

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
#from layout_colorwidget import Color

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
    ##################################################################################################
    ###end new code
    ##################################################################################################

        ########################################################################
        # Start of tests #######################################################
        ########################################################################

        # Test 1: Task 1: Test load_misspellings() function
        test_dict = {"doofis":"doofus", "gote":"goat", "miztake":"mistake", "l8":"late", "kat":"cat"}
        try:
            result = assistant.testFunction(sm.load_misspellings)
            if(result[1]):
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(compare_dicts(result[0], test_dict) == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: load_misspellings() should return " + str(test_dict) + " but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function load_misspellings() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 2: Task 1: Test fix_misspellings() function

        test_dict = {"doofis":"doofus", "gote":"goat", "miztake":"mistake", "l8":"late", "kat":"cat"}

        try:
            result = assistant.testFunction(sm.fix_misspellings, (test_dict,))
            if(result[1]):
                result[0] = result[0] + " The testing dictionary was 'doofis':'doofus', 'gote':'goat', 'miztake':'mistake', 'l8':'late', 'kat':'cat'. </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "when i am late getting home my goat doofus may make a mistake and eat my cat this keeps mee from getting home late all the time becuz i love my goat and dont want him to get a hairball from eating my cat"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: fix_misspellings() should return \"when i am late getting home my goat doofus may make a mistake and eat my cat this keeps mee from getting home late all the time becuz i love my goat and dont want him to get a hairball from eating my cat\", but it returns \"" + str(result) + "\".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function load_misspellings() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 3: Task 1: Test word_count() function 


        test_dict2 = {}
        s_text = "when i am late getting home my goat doofus may make a mistake and eat my cat this keeps mee from getting home late all the time becuz i love my goat and dont want him to get a hairball from eating my cat"
        l_words = s_text.split(" ")
        for word in l_words:
            if word in test_dict2.keys():
                test_dict2[word] = test_dict2[word] + 1
                
            else:
                test_dict2[word] = 1
        try:  
            result = assistant.testFunction(sm.word_count, (s_text,))
            if(result[1]):
                result[0] = result[0] + " The text was 'when i am late getting home my goat doofus may make a mistake and eat my cat this keeps mee from getting home late all the time becuz i love my goat and dont want him to get a hairball from eating my cat'"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(compare_dicts(test_dict2, result[0]) == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: word_count() should return dictionary: \"" + str(test_dict2) + "\" with argument \"" + s_text + "\" but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function word_count() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 4: Task 1: Test output_fixed_text() function

        try:
            result = assistant.testFunction(sm.output_fixed_text, (s_text,))
            if(result[1]):
                result[0] = result[0] + " The text was 'when i am late getting home my goat doofus may make a mistake and eat my cat this keeps mee from getting home late all the time becuz i love my goat and dont want him to get a hairball from eating my cat'"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                inp_file_1 = open("fixed.txt", "r")
                s_data1 = inp_file_1.read()
                inp_file_1.close()
                inp_file_2 = open("fixed_example.txt", "r")
                s_data2 = inp_file_2.read()
                inp_file_2.close()
                if(s_data1.strip() == s_data2.strip()):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: output_fixed_text() writes an incorrect value to the file.  Look at the file fixed_example.txt to see what should have been written to the file fixed.txt.</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function output_fixed_text() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")


        # Test 5: Task 2: Test make_dictionary() function

        spanish_dict = {"amigo":"friend", "hola":"hello", "mi":"my", "donde":"where", "esta":"is", "diablo":"devil", "bano":"bathroom"}        
        try:
            result = assistant.testFunction(sm.make_dictionary)
            if(result[1]):
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(compare_dicts(result[0], spanish_dict) == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: make_dictionary() should return should return " + str(spanish_dict) + " but it returns " + str(result) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function make_dictionary() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 6: Task 2: Test get_text_to_translate() function
        try:
            result = assistant.testFunction(sm.get_text_to_translate)
            if(result[1]):
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "hola mi amigo donde esta la salle de de bano"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: get_text_to_translate() should return \"hola mi amigo donde esta la salle de de bano\" but it returns \"" + str(result[0]) + "\".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function get_text_to_translate() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 7: Task 2: Test translate() function
        s_translate_me = "hola mi amigo donde esta la salle de de bano"

        try:
            result = assistant.testFunction(sm.translate, (spanish_dict, s_translate_me))
            if(result[1]):
                error_msgs.append(result[0])
                passes.append(False)
            else:
                d_xlate_errors = result[0][1]
                result = result[0][0]
                d_answer = {"la":1, "salle":1, "de":2}
                if(result == "hello my friend where is ????? ????? ????? ????? bathroom" and compare_dicts(d_xlate_errors, d_answer) == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: translate() should return \"hello my friend where is ????? ????? ????? ????? bathroom\" and " + str(d_answer) + ", but it returns \"" + str(result) + "\" and " + str(d_xlate_errors) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function translate() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ########################################################################
        # End of tests
        ########################################################################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")
    return passes, error_msgs, assistant

## Edited from Dave Utilities

def compare_dicts(dict1, dict2):
    b_same = True
    d1_keys = dict1.keys()
    d2_keys = dict2.keys()
    if len(d1_keys) != len(d2_keys):
        return False
    for k in d1_keys:
        if dict1[k] != dict2[k]:
            return False
    for k in d2_keys:
        if dict1[k] != dict2[k]:
            return False
        
    return b_same

## End Dave Utilities

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

