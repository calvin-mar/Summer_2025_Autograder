# Python imports
import sys
import ast
import astor
import re
import importlib.util
import os
from multiprocessing import shared_memory as shm

# Graphics/PyQt imports
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
#from layout_colorwidget import Color


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

        
        # Test 1: Task 1: Test my_len() function

        try:
            result = assistant.is_inf(sm.my_len, ("",))
            if(result[1]):
                result[0] = result[0] + " The parameter was an empty string: \"\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 0):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_len() should return 0 with argument \"\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_len() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 2: Task 1: Test my_len() function

        try:
            result = assistant.is_inf(sm.my_len, ("1",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"1\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 1):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_len() should return 1 with argument \"1\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_len() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 3: Task 1: Test my_len() function

        try:
            result = assistant.is_inf(sm.my_len, ("ab",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"ab\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 2):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_len() should return 2 with argument \"ab\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_len() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")


     # Test 4: Task 1: Test my_len() function

        try:
            result = assistant.is_inf(sm.my_len, ("12345678",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"12345678\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 8):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_len() should return 8 with argument \"12345678\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_len() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ######################

        # Test 5: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, ("abc",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"abc\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "abc"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"abc\" with argument \"abc\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 6: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, ("  d  ",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"space space d space space\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "d"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"d\" with argument \"space space d space space\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 7: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, ("\t\n abc",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"tab new_line space abc\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "abc"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"abc\" with argument \"tab new_line space abc\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 8: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, ("abc\t\t\t\n ",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"abc tab tab tab new_line space\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "abc"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"abc\" with argument \"abc tab tab tab new_line space\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 9: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, ("\n\n\n\t   x    \n\n\t",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"new_line new_line new_line tab space space space x space space space space new_line new_line tab\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "x"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"x\" with argument \"new_line new_line new_line tab space space space x space space space space new_line new_line tab\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

       # Test 10: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, ("  abc  def  ",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"space space abc space space def space space\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "abc  def"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"abc  def\" with argument \"space space abc space space def space space\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 11: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, ("  abc \n\t def  ",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"space space abc space space def space space\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "abc \n\t def"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"abc \n\t def\" with argument \"space space abc space new_line tab space def space space\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 12: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, ("abc\t\n def",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"abc tab new_line space def\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "abc\t\n def"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"abc\t\n def\" with argument \"abc tab new_line space def\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 13: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, (" \t\n \t\n ",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"space tab new_line space tab new_line space\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == ""):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"\" with argument \"space tab new_line space tab new_line space\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 14: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, ("\n\n\n\n",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"new_line new_line new_line new_line\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == ""):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"\" with argument \"new_line new_line new_line new_line\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 15: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, ("\t\t\t",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"tab tab tab\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == ""):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"\" with argument \"tab tab tab\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 16: Task 2: Test my_strip() function

        try:
            result = assistant.is_inf(sm.my_strip, ("     ",))
            if(result[1]):
                result[0] = result[0] + " The parameter was \"space space space space space\". </font>"
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == ""):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_strip() should return \"\" with argument \"space space space space space\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_strip() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ######################

        # Test 17: Task 3: Test my_in() function

        try:
            result = assistant.is_inf(sm.my_in, ("abc", "abcdefg"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "abc", "abcdefg". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_in() should return True with arguments abc and abcdefg, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_in() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 18: Task 3: Test my_in() function

        try:
            result = assistant.is_inf(sm.my_in, ("cdefg", "abcdefg"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "cdefg", "abcdefg". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_in() should return True with arguments cdefg and abcdefg, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_in() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 19: Task 3: Test my_in() function

        try:
            result = assistant.is_inf(sm.my_in, ("ef", "abcdefg"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "ef", "abcdefg". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == True):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_in() should return True with arguments ef and abcdefg, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_in() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 20: Task 3: Test my_in() function

        try:
            result = assistant.is_inf(sm.my_in, ("ce", "abcdefg"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "ce", "abcdefg". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_in() should return False with arguments ce and abcdefg, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_in() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 21: Task 3: Test my_in() function

        try:
            result = assistant.is_inf(sm.my_in, ("xab", "abcdefg"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "xab", "abcdefg". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_in() should return False with arguments xab and abcdefg, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_in() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 22: Task 3: Test my_in() function

        try:
            result = assistant.is_inf(sm.my_in, ("fgh", "abcdefg"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "fgh", "abcdefg". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_in() should return False with arguments fgh and abcdefg, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_in() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 23: Task 3: Test my_in() function

        try:
            result = assistant.is_inf(sm.my_in, ("x", "abcdefg"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "x", "abcdefg". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_in() should return False with arguments x and abcdefg, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_in() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 24: Task 3: Test my_in() function

        try:
            result = assistant.is_inf(sm.my_in, ("abcdefgx", "abcdefg"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "abcdefgx", "abcdefg". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == False):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_in() should return False with arguments abcdefgx and abcdefg, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_in() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ######################

        # Test 25: Task 4: Test my_find() function

        try:
            result = assistant.is_inf(sm.my_find, ("abc", "abcdefghi"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "abc", "abcdefghi". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 0):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_find() should return 0 with arguments abc and abcdefghi, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_find() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 26: Task 4: Test my_find() function

        try:
            result = assistant.is_inf(sm.my_find, ("ghi", "abcdefghi"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "ghi", "abcdefghi". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 6):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_find() should return 6 with arguments ghi and abcdefghi, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_find() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 27: Task 4: Test my_find() function

        try:
            result = assistant.is_inf(sm.my_find, ("cde", "abcdefghi"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "cde", "abcdefghi". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == 2):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_find() should return 2 with arguments cde and abcdefghi, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_find() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 28: Task 4: Test my_find() function

        try:
            result = assistant.is_inf(sm.my_find, ("abd", "abcdefghi"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "abd", "abcdefghi". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == -1):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_find() should return -1 with arguments abd and abcdefghi, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_find() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 29: Task 4: Test my_find() function

        try:
            result = assistant.is_inf(sm.my_find, ("xyz", "abcdefghi"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "xyz", "abcdefghi". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == -1):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_find() should return -1 with arguments xyz and abcdefghi, but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_find() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ######################

        # Test 30: Task 5: Test my_replace() function

        try:
            result = assistant.is_inf(sm.my_replace, ("fish is good", "fish", "xyz"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "fish is good", "fish", "xyz". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "xyz is good"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_replace() should return \"xyz is good\" with arguments \"fish is good\", \"fish\", and \"xyz\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_replace() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 31: Task 5: Test my_replace() function

        try:
            result = assistant.is_inf(sm.my_replace, ("fish is good", " i", "xyz"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "fish is good", " i", "xyz". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "fishxyzs good"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_replace() should return \"fishxyzs good\" with arguments \"fish is good\", \" i\", and \"xyz\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_replace() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 32: Task 5: Test my_replace() function
    
        try:
            result = assistant.is_inf(sm.my_replace, ("fish is good", "goo", "xyz"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "fish is good", "goo", "xyz". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "fish is xyzd"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_replace() should return \"fish is xyzd\" with arguments \"fish is good\", \"goo\", and \"xyz\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_replace() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 33: Task 5: Test my_replace() function

        try:
            result = assistant.is_inf(sm.my_replace, ("fish is good", "od", "axyz"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "fish is good", "od", "axyz". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "fish is goaxyz"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_replace() should return \"fish is goaxyz\" with arguments \"fish is good\", \"od\", and \"axyz\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_replace() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 34: Task 5: Test my_replace() function

        try:
            result = assistant.is_inf(sm.my_replace, ("fish is good", "h i", "xyz"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "fish is good", "h i", "xyz". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "fisxyzs good"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_replace() should return \"fisxyzs good\" with arguments \"fish is good\", \"h i\", and \"xyz\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_replace() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 35: Task 5: Test my_replace() function

        try:
            result = assistant.is_inf(sm.my_replace, ("fish is good", "x", "xyz"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "fish is good", "x", "xyz". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "fish is good"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_replace() should return \"fish is good\" with arguments \"fish is good\", \"x\", and \"xyz\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_replace() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 36: Task 5: Test my_replace() function

        try:
            result = assistant.is_inf(sm.my_replace, ("fish is good", " ", "xyz"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "fish is good", " ", "xyz". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "fishxyzis good"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_replace() should return \"fishxyzis good\" with arguments \"fish is good\", \" \", and \"xyz\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_replace() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 37: Task 5: Test my_replace() function

        try:
            result = assistant.is_inf(sm.my_replace, ("fish is fish", "ish", "xyz"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "fish is good", "ish", "xyz". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == "fxyz is fish"):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_replace() should return \"fxyz is fish\" with arguments \"fish is fish\", \"ish\", and \"xyz\", but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_replace() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        ######################

        # Test 38: Task 6: Test my_simple_split() function

        try:
            result = assistant.is_inf(sm.my_simple_split, ("a", "banana"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "a", "banana". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == ["b", "n", "n", ""]):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_simple_split(\"a\", \"banana\") should return the list [\"b\", \"n\", \"n\", \"\"], but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_simple_split() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 39: Task 6: Test my_simple_split() function

        try:
            result = assistant.is_inf(sm.my_simple_split, ("a", "anna"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "a", "anna". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == ["", "nn", ""]):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_simple_split(\"a\", \"anna\") should return the list [\"\", \"nn\", \"\"], but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_simple_split() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 40: Task 6: Test my_simple_split() function

        try:
            result = assistant.is_inf(sm.my_simple_split, ("a", "xaax"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "a", "xaax". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == ["x", "", "x"]):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_simple_split(\"a\", \"xaax\") should return the list [\"x\", \"\", \"x\"], but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_simple_split() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 41: Task 6: Test my_simple_split() function

        try:
            result = assistant.is_inf(sm.my_simple_split, ("a", "xaaax"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "a", "xaaax". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == ["x", "", "", "x"]):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_simple_split(\"a\", \"xaaax\") should return the list [\"x\", \"\", \"\", \"x\"], but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_simple_split() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")

        # Test 42: Task 6: Test my_simple_split() function

        try:
            result = assistant.is_inf(sm.my_simple_split, ("a", "a"))
            if(result[1]):
                result[0] = result[0] + ' The parameters were "a", "a". </font>'
                error_msgs.append(result[0])
                passes.append(False)
            else:
                if(result[0] == ["", ""]):
                    passes.append(True)
                else:
                    passes.append(False)
                    error_msgs.append(" Failed: my_simple_split(\"a\", \"a\") should return the list [\"\", \"\"], but it returns " + str(result[0]) + ".</font>")
        except:
            passes.append(False)
            error_msgs.append(" Failed: Function my_simple_split() caused an error. The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
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

