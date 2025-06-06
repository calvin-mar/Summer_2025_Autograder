# Python imports
import sys
import ast
import astor
import re
import importlib.util
import os

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
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
    b_proceed, s_error_msg = assistant.syntax_checker(os.path.join(dir_path, student_submission), TIMEOUT)
    if b_proceed == False:
        passes.append(False)
        error_msgs.append("There is a problem with your file.")
    else:
        specific_student.loader.exec_module(sm)

        ########################################################################
        # Start of tests #######################################################
        ########################################################################
        i_test_num = 1
        ########################################################################
        # Start of tests #######################################################
        ########################################################################

        
        # Test 1: Task 1: Test my_len() function



        error_calling_function = False
        try:
            try:
                result = sm.my_len("")
            except:
                result = '"Function my_len() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 0
            
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_len() should return 0 with argument \"\", but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 2: Task 1: Test my_len() function



        error_calling_function = False
        try:
            try:
                result = sm.my_len("1")
            except:
                result = '"Function my_len() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 1
            passes.append(True)

            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_len() should return 1 with argument \"1\", but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 3: Task 1: Test my_len() function



        error_calling_function = False
        try:
            try:
                result = sm.my_len("ab")
            except:
                result = '"Function my_len() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 2
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_len() should return 2 with argument \"ab\", but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 4: Task 1: Test my_len() function



        error_calling_function = False
        try:
            try:
                result = sm.my_len("12345678")
            except:
                result = '"Function my_len() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 8
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_len() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_len() should return 8 with argument \"12345678\", but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ######################

        # Test 5: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip("abc")
            except:
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "abc"
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"abc\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 6: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip("  d  ")
            except:
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "d"
            passes.append(True)
            
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"space space d space space\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 7: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip("\t\n abc")
            except:
                passes.append(False)
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "abc"
            passes.append(True)
            
        except:
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"tab new_line space abc\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 8: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip("abc\t\t\t\n ")
            except:
                passes.append(False)
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "abc"
            passes.append(True)
        except:
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"abc tab tab tab new_line space\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 9: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip("\n\n\n\t   x    \n\n\t")
            except:
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "x"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"new_line new_line new_line tab space space space x space space space space new_line new_line tab\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 10: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip("  abc  def  ")
            except:
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "abc  def"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"space space abc space space def space space\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 11: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip("  abc \n\t def  ")
            except:
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "abc \n\t def"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"space space abc space new_line tab space def space space\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 12: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip("abc\t\n def")
            except:
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "abc\t\n def"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"abc tab new_line space def\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 13: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip(" \t\n \t\n ")
            except:
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == ""
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"space tab new_line space tab new_line space\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 14: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip("\n\n\n\n")
            except:
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == ""
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"new_line new_line new_line new_line\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 15: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip("\t\t\t")
            except:
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == ""
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"tab tab tab\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 16: Task 2: Test my_strip() function



        error_calling_function = False
        try:
            try:
                result = sm.my_strip("     ")
            except:
                result = '"Function my_strip() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == ""
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_strip() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_strip() fails for argument \"space space space space space\".</font>")

        
        i_test_num = i_test_num + 1

        ######################

        # Test 17: Task 3: Test my_in() function



        error_calling_function = False
        try:
            try:
                result = sm.my_in("abc", "abcdefg")
            except:
                result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == True
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_in() should return True with arguments abc and abcdefg, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 18: Task 3: Test my_in() function



        error_calling_function = False
        try:
            try:
                result = sm.my_in("cdefg", "abcdefg")
            except:
                result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == True
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_in() should return True with arguments abcdefg and cdefg, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1



        # Test 19: Task 3: Test my_in() function



        error_calling_function = False
        try:
            try:
                result = sm.my_in("ef", "abcdefg")
            except:
                result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == True
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_in() should return True with arguments ef and abcdefg, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        

        # Test 20: Task 3: Test my_in() function



        error_calling_function = False
        try:
            try:
                result = sm.my_in("ce", "abcdefg")
            except:
                result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == False
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_in() should return False with arguments ce and abcdefg, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        

        # Test 21: Task 3: Test my_in() function



        error_calling_function = False
        try:
            try:
                result = sm.my_in("xab", "abcdefg")
            except:
                result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == False
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_in() should return False with arguments xab and abcdefg, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 22: Task 3: Test my_in() function



        error_calling_function = False
        try:
            try:
                result = sm.my_in("fgh", "abcdefg")
            except:
                result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == False
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_in() should return False with arguments fgh and abcdefg, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1



        # Test 23: Task 3: Test my_in() function



        error_calling_function = False
        try:
            try:
                result = sm.my_in("x", "abcdefg")
            except:
                result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == False
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_in() should return False with arguments x and abcdefg, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 24: Task 3: Test my_in() function



        error_calling_function = False
        try:
            try:
                result = sm.my_in("abcdefgx", "abcdefg")
            except:
                result = '"Function my_in() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == False
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_in() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_in() should return False with arguments abcdefgx and abcdefg, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1



        ######################

        # Test 25: Task 4: Test my_find() function



        error_calling_function = False
        try:
            try:
                result = sm.my_find("abc", "abcdefghi")
            except:
                result = '"Function my_find() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 0
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_find() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_find() should return 0 with arguments abc and abcdefghi, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 26: Task 4: Test my_find() function



        error_calling_function = False
        try:
            try:
                result = sm.my_find("ghi", "abcdefghi")
            except:
                result = '"Function my_find() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 6
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_find() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_find() should return 6 with arguments ghi and abcdefghi, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 27: Task 4: Test my_find() function



        error_calling_function = False
        try:
            try:
                result = sm.my_find("cde", "abcdefghi")
            except:
                result = '"Function my_find() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == 2
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_find() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_find() should return 2 with arguments cde and abcdefghi, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 28: Task 4: Test my_find() function



        error_calling_function = False
        try:
            try:
                result = sm.my_find("abd", "abcdefghi")
            except:
                result = '"Function my_find() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == -1
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_find() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_find() should return -1 with arguments abd and abcdefghi, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1


        # Test 29: Task 4: Test my_find() function



        error_calling_function = False
        try:
            try:
                result = sm.my_find("xyz", "abcdefghi")
            except:
                result = '"Function my_find() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == -1
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_find() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_find() should return -1 with arguments xyz and abcdefghi, but it returns " + str(result) + ".</font>")

        
        i_test_num = i_test_num + 1

        ######################

        # Test 30: Task 5: Test my_replace() function



        error_calling_function = False
        try:
            try:
                result = sm.my_replace("fish is good", "fish", "xyz")
            except:
                result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "xyz is good"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_replace() should return \"xyz is good\" with arguments \"fish is good\", \"fish\", and \"xyz\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 31: Task 5: Test my_replace() function



        error_calling_function = False
        try:
            try:
                result = sm.my_replace("fish is good", " i", "xyz")
            except:
                result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "fishxyzs good"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_replace() should return \"fishxyzs good\" with arguments \"fish is good\", \" i\", and \"xyz\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 32: Task 5: Test my_replace() function



        error_calling_function = False
        try:
            try:
                result = sm.my_replace("fish is good", "goo", "xyz")
            except:
                result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "fish is xyzd"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_replace() should return \"fish is xyzd\" with arguments \"fish is good\", \"goo\", and \"xyz\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 33: Task 5: Test my_replace() function



        error_calling_function = False
        try:
            try:
                result = sm.my_replace("fish is good", "od", "axyz")
            except:
                result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "fish is goaxyz"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_replace() should return \"fish is goaxyz\" with arguments \"fish is good\", \"od\", and \"axyz\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 34: Task 5: Test my_replace() function



        error_calling_function = False
        try:
            try:
                result = sm.my_replace("fish is good", "h i", "xyz")
            except:
                result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "fisxyzs good"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_replace() should return \"fisxyzs good\" with arguments \"fish is good\", \"h i\", and \"xyz\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 35: Task 5: Test my_replace() function



        error_calling_function = False
        try:
            try:
                result = sm.my_replace("fish is good", "x", "xyz")
            except:
                result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "fish is good"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_replace() should return \"fish is good\" with arguments \"fish is good\", \"x\", and \"xyz\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 36: Task 5: Test my_replace() function



        error_calling_function = False
        try:
            try:
                result = sm.my_replace("fish is good", " ", "xyz")
            except:
                result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "fishxyzis good"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_replace() should return \"fishxyzis good\" with arguments \"fish is good\", \" \", and \"xyz\".</font>")

        
        i_test_num = i_test_num + 1


        # Test 37: Task 5: Test my_replace() function



        error_calling_function = False
        try:
            try:
                result = sm.my_replace("fish is fish", "ish", "xyz")
            except:
                result = '"Function my_replace() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == "fxyz is fish"
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_replace() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_replace() should return \"fxyz is fish\" with arguments \"fish is fish\", \"ish\", and \"xyz\".</font>")

        
        i_test_num = i_test_num + 1

        ######################

        # Test 38: Task 6: Test my_simple_split() function



        error_calling_function = False
        try:
            try:
                result = sm.my_simple_split("a", "banana")
            except:
                result = '"Function my_simple_split() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == ["b", "n", "n", ""]
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_simple_split() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_simple_split(\"a\", \"banana\") should return the list [\"b\", \"n\", \"n\", \"\"].</font>")

        
        i_test_num = i_test_num + 1


        # Test 39: Task 6: Test my_simple_split() function



        error_calling_function = False
        try:
            try:
                result = sm.my_simple_split("a", "anna")
            except:
                result = '"Function my_simple_split() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == ["", "nn", ""]
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_simple_split() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_simple_split(\"a\", \"anna\") should return the list [\"\", \"nn\", \"\"].</font>")

        
        i_test_num = i_test_num + 1


        # Test 40: Task 6: Test my_simple_split() function



        error_calling_function = False
        try:
            try:
                result = sm.my_simple_split("a", "xaax")
            except:
                result = '"Function my_simple_split() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == ["x", "", "x"]
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_simple_split() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_simple_split(\"a\", \"xaax\") should return the list [\"x\", \"\", \"x\"].</font>")

        
        i_test_num = i_test_num + 1


        # Test 41: Task 6: Test my_simple_split() function



        error_calling_function = False
        try:
            try:
                result = sm.my_simple_split("a", "xaaax")
            except:
                result = '"Function my_simple_split() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == ["x", "", "", "x"]
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_simple_split() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_simple_split(\"a\", \"xaaax\") should return the list [\"x\", \"\", \"\", \"x\"].</font>")

        
        i_test_num = i_test_num + 1


        # Test 42: Task 6: Test my_simple_split() function



        error_calling_function = False
        try:
            try:
                result = sm.my_simple_split("a", "a")
            except:
                result = '"Function my_simple_split() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True                
            assert result == ["", ""]
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function my_simple_split() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: my_simple_split(\"a\", \"a\") should return the list [\"\", \"\"].</font>")

        
        i_test_num = i_test_num + 1

        ######################



        
        ########################################################################
        # End of tests
        ########################################################################
    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")

    return passes, error_msgs, assistant

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_14_student_submission.py")
	ret = queue.get()
	ret["result"] = passes
	queue.put(ret)
	return

def main():
    testSets = [4, 12, 8, 5, 8, 5]
    passes, error_msgs,assistant = autoGrader("lab_14_student_submission.py")
    assistant.displayWindow(passes, error_msgs, testSets)
if __name__ == "__main__":
    main()

