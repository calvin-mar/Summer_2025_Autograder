# Python imports
import sys
import ast
import astor
import re
import os
import importlib.util
from multiprocessing import shared_memory as shm


def autoGrader(student_submission):
    passes = []
    error_msgs = []

    l_data = shm.ShareableList([50,10,15], name="l_data")
    i_test_num = 1
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
    l_data.shm.close()
    l_data.shm.unlink()
    if b_proceed == False:
        passes.append(False)
        if s_error_msg != "":
            error_msgs.append(s_error_msg)
        else:
            error_msgs.append("There is a problem with your file.")
    else:
        l_data = shm.ShareableList([50,10,15], name="l_data")
        specific_student.loader.exec_module(sm)
        #l_data.shm.close()
        #l_data.shm.unlink()
        


        ########################################################################
        # Start of tests #######################################################
        ########################################################################
        # Test 1:
        
        try:
            assert sm.f_temp_fahr == (9/5) * sm.f_celsius + 32
            passes.append(True)
        except:
            passes.append(False)
            try:
                error_msgs.append(" Temperature Conversions Failed: " + str(sm.f_celsius) + " degrees Celsius should equal " + str(((9/5) * sm.f_celsius + 32)) + " degrees Fahrenheit but your code has it equal " + str(sm.f_temp_fahr) + " degrees Fahrenheit.  Make sure your variables are named correctly if your value is correct.</font>")
            except:
                error_msgs.append(" Temperature Conversions Failed: variables are not named correctly or have incorrect values.</font>")


        
        i_test_num = i_test_num + 1

        # Test 2: 



        try:
            assert sm.f_distance_km == (sm.f_miles / 3.1) * 5
            passes.append(True)
        except:
            passes.append(False)
            try:
                error_msgs.append(" Distance Conversions Failed: " + str(sm.f_miles) + " miles should equal " + str((sm.f_miles / 3.1) * 5) + " kilometers but your code has it equal " + str(sm.f_distance_km) + " kilometers.  Make sure your variables are named correctly if your value is correct.</font>")
            except:
                error_msgs.append(" Distance Conversions Failed: variables are not named correctly or have incorrect values.</font>")
                

        
        i_test_num = i_test_num + 1

        # Test 3: 



        try:
            f_small_area = 3.14 * 6 ** 2
            f_med_area = 3.14 * 8 ** 2
            f_large_area = 3.14 * 9 ** 2
            f_small_cost = 8 / f_small_area
            f_med_cost = 12 / f_med_area
            f_large_cost = 16 / f_large_area

            assert sm.f_small_area == f_small_area
            assert sm.f_med_area == f_med_area
            assert sm.f_large_area == f_large_area
            assert sm.f_small_cost == f_small_cost
            assert sm.f_med_cost == f_med_cost
            assert sm.f_large_cost == f_large_cost
            passes.append(True)
        except:
            passes.append(False)
            try:
                error_msgs.append(" Pizza Data Failed: Areas should be S: " + str(f_small_area) + ", M: " + str(f_med_area) + ", L: " + str(f_large_area) + " and costs should be S: " + str(f_small_cost) + ", M: " + str(f_med_cost) + ", L: " + str(f_large_cost) + ". Make sure your variables are named correctly if your values are correct.</font>")
            except:
                error_msgs.append(" Pizza Data Failed: variables are not named correctly or have incorrect values.</font>")

        
        i_test_num = i_test_num + 1

        # Test 4: 



        try:

            i_roll_packs = i_people // 12 + 1
            i_soda_packs = (2 * i_people) // 12 + 1
            i_hot_dog_packs = i_people // 8 + 1
            i_chip_boxes = i_people // 16 + 1

            i_rem_rolls = (i_roll_packs * 12) - i_people
            i_rem_sodas = (i_soda_packs * 12) - (i_people * 2)
            i_rem_hot_dogs = (i_hot_dog_packs * 8) - i_people
            i_rem_chips = (i_chip_boxes * 16) - i_people
            
            assert sm.i_roll_packs == i_roll_packs
            assert sm.i_soda_packs == i_soda_packs
            assert sm.i_hot_dog_packs == i_hot_dog_packs
            assert sm.i_chip_boxes == i_chip_boxes
            assert sm.i_rem_rolls == i_rem_rolls
            assert sm.i_rem_sodas == i_rem_sodas
            assert sm.i_rem_hot_dogs == i_rem_hot_dogs
            assert sm.i_rem_chips == i_rem_chips
            passes.append(True)
        except:
            try:
                error_msgs.append(" Olympics Party Failed: For " + str(sm.i_people) + " people, the values should be " + str(i_roll_packs) + " roll packs, "  + str(i_soda_packs) + " soda packs, "  + str(i_hot_dog_packs) + " hot dog packs, "  + str(i_chip_boxes) + " chip boxes.  There should be the following items left over: "  + str(i_rem_rolls) + " rolls, "  + str(i_rem_sodas) + " sodas, "  + str(i_rem_hot_dogs) + " hot dogs, and "  + str(i_rem_chips) + " bags of chips.  Make sure your variables are named correctly if your values are correct.</font>")
            except:
                error_msgs.append(" Olympics Party Failed: variables are not named correctly or have incorrect values.</font>")

        ########################################################################
        # End of tests
        ########################################################################
        l_data.shm.close()
        l_data.shm.unlink()

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")
    
    return passes, error_msgs, assistant

def testing():
	passes, error_msgs,assistant = autoGrader("lab_02_student_submission.py")
	return passes

def main():
	passes, error_msgs,assistant = autoGrader("lab_02_student_submission.py")
	assistant.displayWindow(passes, error_msgs)
	
if __name__ == "__main__":
    main()
