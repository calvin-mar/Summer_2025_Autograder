# Python imports
import sys
import ast
import astor
import re
import os
import importlib.util

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
    b_proceed, s_error_msg = assistant.syntax_checker(student_submission, TIMEOUT)
    if b_proceed == False:
        passes.append(False)
        error_msgs.append("There is a problem with your file.")
    else:
        specific_student.loader.exec_module(sm)
        ########################################################################
        # Start of tests #######################################################
        ########################################################################
        i_test_num = 1
        # Test 1: Task 1: Test biggest_number() function with biggest in 1st position
        error_calling_function = False
        try:
            assert len(sm.l_cities) == 0
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_cities is not empty or does not exist. </font>")

        
        i_test_num = i_test_num + 1

        # Test 2: 
        
        
        
        try:
            assert len(sm.l_miles) == 4
            assert sm.l_miles[0] == 3.1
            assert sm.l_miles[1] == 6.2
            assert sm.l_miles[2] == 13.1
            assert sm.l_miles[3] == 26.2
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_miles does not contain precisely 3.1, 6.2, 13.1, 26.2 in that order or else it also contains additional values.</font>")

        
        i_test_num = i_test_num + 1

        # Test 3: 
        
        
        
        try:
            assert sm.f_third == 26.2
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: Variable f_third doesn't hold the value 26.2. </font>")

        
        i_test_num = i_test_num + 1

        # Test 4: 
        
        
        
        try:
            assert len(sm.l_states) == 4
            assert sm.l_states[0] == "MA"
            assert sm.l_states[1] == "IN"
            assert sm.l_states[2] == "TN"
            assert sm.l_states[3] == "WV"
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_states does not contain precisely \"MA\", \"IN\", \"TN\", and \"WV\" in that order or else it also contains additional values. </font>")

        
        i_test_num = i_test_num + 1

        # Test 5: 
        
        
        
        try:
            assert sm.s_state == "IN"
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: Variable s_state doesn't hold the value \"IN\". </font>")

        
        i_test_num = i_test_num + 1

        # Test 6: 
        
        
        
        try:
            assert len(sm.l_countries) == 5
            assert sm.l_countries[0] == "US"
            assert sm.l_countries[1] == "Japan"
            assert sm.l_countries[2] == "Brazil"
            assert sm.l_countries[3] == "Mexico"
            assert sm.l_countries[4] == "Canada"
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_countries does not contain precisely \"US\", \"Japan\", \"Brazil\", \"Mexico\", \"Canada\" in that order or else it also contains additional values. </font>")

        
        i_test_num = i_test_num + 1

        # Test 7: 
        
        
        
        try:
            assert len(sm.l_cars) == 6
            assert sm.l_cars[0] == "Ferrari"
            assert sm.l_cars[1] == "Sonata"
            assert sm.l_cars[2] == "Bug"
            assert sm.l_cars[3] == "Rio"
            assert sm.l_cars[4] == "Corolla"
            assert sm.l_cars[5] == "Maserati"
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_cars does not contain precisely \"Ferrari\", \"Sonata\", \"Bug\", \"Rio\", \"Corolla\", \"Maserati\" in that order or else it also contains additional values. </font>")

        
        i_test_num = i_test_num + 1

        # Test 8: 
        
        
        
        try:
            assert len(sm.l_names) == 8
            assert sm.l_names[0] == "Suzanne"
            assert sm.l_names[1] == "Alvin"
            assert sm.l_names[2] == "Simon"
            assert sm.l_names[3] == "Theodore"
            assert sm.l_names[4] == "Dave"
            assert sm.l_names[5] == "Brittany"
            assert sm.l_names[6] == "Jeanette"
            assert sm.l_names[7] == "Eleanor"
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_names does not contain the correct number of items or the correct items. </font>")

        
        i_test_num = i_test_num + 1

        # Test 9: 
        
        
        
        try:
            assert len(sm.l_names2) == 8
            assert sm.l_names2[0] == "Suzanne"
            assert sm.l_names2[1] == "Billy"
            assert sm.l_names2[2] == "Alvin"
            assert sm.l_names2[3] == "Simon"
            assert sm.l_names2[4] == "Dave"
            assert sm.l_names2[5] == "Brittany"
            assert sm.l_names2[6] == "Jeanette"
            assert sm.l_names2[7] == "Eleanor"
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_names does not contain the correct number of items or the correct items. </font>")

        
        i_test_num = i_test_num + 1

        # Test 10: 
        
        
        
        try:
            assert len(sm.l_names2) == 8
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: The value of i_num_names is not correct. </font>")

        
        i_test_num = i_test_num + 1

        # Test 11: 
        
        
        
        try:
            assert sm.b_camry_present == False
            assert sm.b_sonata_present == True
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: b_camry_present and/or b_sonata_present is incorrect. </font>")

        
        i_test_num = i_test_num + 1

        # Test 12: 
        
        
        
        try:
            assert sm.i_suzy_location == -1
            assert sm.i_dave_location == 4
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: i_suzy_location and/or i_dave_location is incorrect. </font>")

        
        i_test_num = i_test_num + 1

        # Test 13: 
        
        
        
        try:
            assert len(sm.l_grades) == 4
            assert sm.l_grades[0] == 102
            assert sm.l_grades[1] == 52
            assert sm.l_grades[2] == 79
            assert sm.l_grades[3] == 34
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_grades does not contain precisely the values returned by the function call all increased by 2. </font>")

        
        i_test_num = i_test_num + 1

        # Test 14: 
        
        
        
        try:
            assert len(sm.l_grades2) == 4
            assert sm.l_grades2[0] == 32
            assert sm.l_grades2[1] == 50
            assert sm.l_grades2[2] == 77
            assert sm.l_grades2[3] == 100
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_grades2 is not sorted from low to high or contains the wrong number of grades (should be 4). </font>")

        
        i_test_num = i_test_num + 1

        # Test 15: 
        
        
        
        try:
            assert len(sm.l_grades3) == 4
            assert sm.l_grades3[0] == 100
            assert sm.l_grades3[1] == 77
            assert sm.l_grades3[2] == 50
            assert sm.l_grades3[3] == 32
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: List l_grades3 is not sorted from high to low or contains the wrong number of grades (should be 4). </font>")

        
        i_test_num = i_test_num + 1

        # Test 16: 
        
        
        
        try:
            assert sm.i_biggest == 100
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: i_biggest is not the biggest value in the list l_grades. </font>")

        
        i_test_num = i_test_num + 1

        # Test 17: 
        
        
        
        try:
            assert sm.i_smallest == 32
            passes.append(True)
        except:
            passes.append(False)
            error_msgs.append(" Failed: i_smallest is not the smallest value in the list l_grades. </font>")


        ########################################################################
        # End of tests
        ########################################################################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")
    
    return passes, error_msgs, assistant

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_09_student_submission.py")
	ret = queue.get()
	ret["result"] = passes
	queue.put(ret)
	return

def main():
	passes, error_msgs,assistant = autoGrader("lab_09_student_submission.py")
	assistant.displayWindow(passes, error_msgs)
	
if __name__ == "__main__":
    main()
