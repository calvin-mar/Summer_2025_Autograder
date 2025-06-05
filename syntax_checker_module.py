# Python imports
import sys
import math
import ast
import astor
import re
import os
import multiprocessing
import time
import importlib.util

def syntax_checker(filename, TIMEOUT):
        print("Syntax checker starting...")

        ##################################################################################################
        ### new code
        ##################################################################################################
        #Student import infinite loop check
        def importLabs():
                print("PROCESS")
                dir_path = os.path.dirname(os.path.realpath(__file__))
                name = filename[:-3]
                specific_student = importlib.util.spec_from_file_location(name, os.path.join(dir_path, filename))
                sm = importlib.util.module_from_spec(specific_student)

                specific_student.loader.exec_module(sm)
                return
        p = multiprocessing.Process(target=importLabs)
        p.start()
        start = time.time()
        while time.time() - start <= 1:
                print(time.time())
                if not p.is_alive():
                        break
                time.sleep(.1)
        else:
                p.terminate()
                p.join()
                s_error_msg = ""
                s_error_msg = s_error_msg + "Your code contains an infinite loop which is not allowed.  "
                return False, s_error_msg

        # Check for triple quote and triple apostrophes
        s_triple_res = ""#check_for_triples()
        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            absolute_path = os.path.join(dir_path,filename)
            input_file = open(absolute_path, "r")
            s_text = input_file.read()
            if "'''" in s_text or '"""' in s_text:
                s_triple_res = "Contains Triples"
            else:
                s_triple_res = "No Triples"
            input_file.close()
        except:
            s_triple_res = "Error Reading File"
        
        # if no triples, remove comments and continue
        s_error_msg = ""
        if s_triple_res == "No Triples":
            b_proceed = True
            # remove comments


            # https://stackoverflow.com/questions/1769332/script-to-remove-python-comments-docstrings
            with open(absolute_path,"r") as f:
                code = f.read() 
            parsed = ast.parse(code)
            for node in ast.walk(parsed):
                #if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
                if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
                    # set value to empty string
                    node.value = ast.Constant(value='') 
            s_trimmed_code = astor.to_source(parsed)  
            pattern = r'^.*"""""".*$' # remove empty """"""
            s_trimmed_code = re.sub(pattern, '', s_trimmed_code, flags=re.MULTILINE) 

            
            # look for syntax that is not allowed
            if "join(" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b>join</b>() which is not allowed.  "
            if "zip(" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b>zip</b>() which is not allowed.  "
            if "exit(" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b><font color=purple>exit</font></b>() which is not allowed.  "
            if "quit(" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b><font color=purple>quit</font></b>() which is not allowed.  "
            if "break" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b><font color=orange>break</font></b> which is not allowed.  "
            if "continue" in s_trimmed_code:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains <b><font color=orange>continue</font></b> which is not allowed.  "

            # look for print(f or print(F
            if re.search("print\\s*\\(\\s*[fF]\\s*[\'\"]+", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains formatted print statement(s) like print(f... or print(F... which are not allowed.  "


            # look for naked return
            if re.search(".*\\s+return\\s*\\n", s_trimmed_code) != None or re.search(".*\\s+return(\\s*\\\\s*)*\\n", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a 'naked return' which is not allowed.  A naked return is a return that is not followed by a variable or literal.  "

            # look for with open(
            if re.search("with\\s+open\\s*\\(", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code uses a <b><font color=orange>with</font> <font color=purple>open</font></b> statement which is not allowed.  "
            
            
            # look for _ as a variable name
            if re.search(".*\\s+_\\s+=.*", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a variable named _ which is not allowed.  "
            
            # look for comprehensions
            if re.search("=\\s*\\[+\\s*\\w+\\s+for\\s+", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a list comprehension which is not allowed.  "
                
            if re.search("=\\s*\\[+.*for\\s+", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a list comprehension which is not allowed.  "
                
            if re.search("=\\s*\\{\\s*.*:\\s*.+\\s+for\\s+", s_trimmed_code) != None: 
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a dictionary comprehension which is not allowed.  "
          
            if re.search("=\\s*\\{+\\s*\\w+\\s+for\\s+", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a set comprehension which is not allowed.  "
            
            if re.search("=\\s*\\(+\\s*\\w+\\s+for\\s+", s_trimmed_code) != None:
                b_proceed = False
                s_error_msg = s_error_msg + "Your code contains a generator comprehension which is not allowed.  "
    

            
            
        else: # otherwise error message re triples and exit
            b_proceed = False
            if s_triple_res == "Contains Triples":
                s_error_msg = "Your code contains either triple quotes \"\"\" or triple apostrophes ''' which are not allowed."
            else:
                s_error_msg = "Your file could not be read.  Make sure it is named correctly.  "


        print("...Syntax checker completed.")
        print()
        print("You may close the syntax checker window to exit.")
        return b_proceed, s_error_msg
