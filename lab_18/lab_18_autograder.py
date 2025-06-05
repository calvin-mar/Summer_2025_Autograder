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
from layout_colorwidget import Color


from dave_utilities import *
import dave_utilities


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
    ##################################################################################################
    ###end new code
    ##################################################################################################

        ########################################################################
        # Start of tests #######################################################
        ########################################################################
        i_test_num = 1
        # Test 1: Task 1: Test get_data() function



        error_calling_function = False
        l2d_solution = [['3 MUSKETEERS (M)', '1 bar (51g)', '212', '6.5g', '3.5g', '1.5g', '39g', '99mg', '43mg'],
            ['5TH AVENUE (H)', '1 bar (60g)', '279.5', '12.5g', '3.5g', '4.5g', '41g', '111.5mg', '42mg'],
            ['100 GRAND BAR (N)', '1 bar (43g)', '200.5', '8g', '5g', '2g', '30.5g', '89mg', '49mg'],
            ['AFTER EIGHT MINTS (N)', '5 pieces (41g)', '147', '5.5g', '3.5g', '1g', '31.5g', '5mg', '9.5mg'],
            ['ALMOND JOY (H)', '1 bar (50g)', '232', '14g', '8.5g', '2.5g', '29g', '67mg', '39.5mg'],
            ['BABY RUTH (N)', '1 bar (60g)', '288.5', '12.5g', '7.5g', '4.5g', '39g', '135.5mg', '24.5mg'],
            ['BAR NONE (H)', '1 piece (43g)', '224', '14.5g', '9.5g', '3.5g', '22.5g', '44.5mg', '62.5mg'],
            ['BUTTERFINGER (N)', '1 bar (45g)', '216', '8.5g', '4.5g', '5.5g', '29.5g', '89mg', '12mg'],
            ["CADBURY'S CARAMELLO (H)", '1 bar (45g)', '220', '11.5g', 'n/a', '2.5g', '29.5g', '55.5mg', '89mg'],
            ['CHUNKIE (N)', '1 bar (35g)', '173.5', '10g', '8g', '3g', '20g', '18.5mg', '50mg'],
            ["DEMET'S TURTLES (N)", '1 piece (17g)', '82.5', '4.5g', '2g', '1g', '10g', '16mg', '27mg'],
            ['GOLDEN III (H)', '1 bar (91g)', '471.5', '30g', 'n/a', '6g', '60g', '79mg', '275mg'],
            ['GOLDEN ALMOND', '1 bar (85g)', '466', '32g', 'n/a', '9g', '41.5g', '53.5mg', '279mg'],
            ['GOLDEN ALMOND SOLITAIRES (H)', '1 pkg. (85g)', '455', '31.5g', '13.5g', '10g', '40g', '46mg', '305mg'],
            ['GOOBERS (N)', '1 pkg (39g)', '200', '13g', '5g', '5.5g', '19g', '16mg', '49.5mg'],
            ['KIT KAT (H)', '1 bar (43g)', '220.5', '12.5g', '7.5g', '3g', '26.5g', '43.5mg', '77.5mg'],
            ['KRACKEL (H)', '1 bar (47g)', '236', '13g', '5.5g', '3g', '29g', '64mg', '84mg'],
            ["M&M'S - PEANUT (M)", '1 pkg. (47g)', '242.5', '12.5g', '5g', '4.5g', '28.5g', '22.5mg', '47.5mg'],
            ["M&M'S - PLAIN (M)", '1 pkg. (48g)', '236', '10g', '6.5g', '2g', '34g', '29.5mg', '50.5mg'],
            ['MARS ALMOND BAR (M)', '1 bar (50g)', '233.5', '11.5g', '2.5g', '4g', '31.5g', '85mg', '84mg'],
            ['MILK WAY (M)', '1 bar (54g)', '228.5', '8.5g', '4g', '2.5g', '38.5g', '129.5mg', '70mg'],
            ['MOUNDS (H)', '1 pkg. (54g)', '195', '11.5g', '6g', '2g', '31.5g', '67.5mg', '12.5mg'],
            ['MR. GOODBAR (H)', '1 bar (50g)', '257', '16g', '9g', '6.5g', '25.5g', '17mg', '55.5mg'],
            ['NESTLE CRUNCH (N)', '1 bar (44g)', '229.5', '11.5g', '6.5g', '2.5g', '28.5g', '58.5mg', '74.5mg'],
            ['NIBS CHERRY (H)', '1 oz. (28.5g)', '106', '0.5g', 'n/a', '1g', '26.5g', '67mg', '18.5mg'],
            ['OH HENRY! (N)', '1 bar (57g)', '245.5', '9.5g', '4g', '6g', '37g', '135mg', '62mg'],
            ['RAISINETS (N)', '1 bar (45g)', '185.5', '7g', '3.5g', '2g', '32g', '16mg', '48.5mg'],
            ["REESE'S P-BUTTER CUPS (H)", '1 pkg. 2 cups (45g)', '222', '14.5g', '6.5g', '5g', '22g', '130.5mg', '35mg'],
            ["REESE'S PIECES (H)", '1 bar (55g)', '258', '11.5g', '7.5g', '7g', '34g', '82.5mg', '73mg'],
            ['ROLO (H)', '1 roll (49g)', '233', '10.5g', '5.5g', '2.5g', '34g', '83.5mg', '65.5mg'],
            ['SKITTLES (M)', '1 pkg. (57g)', '231', '2.5g', '0.5g', '0', '51.5g', '9mg', '0'],
            ['SKOR TOFFEE (H)', '1 bar (40g)', '211', '14g', 'n/a', '2g', '22g', '92mg', '45mg'],
            ['SNICKERS (M)', '1 bar (57g)', '273', '14g', '5g', '4.5g', '34g', '151.5mg', '53.5mg'],
            ['SPECIAL DARK (H)', '1 bar (41g)', '195', '12.5g', '7g', '2g', '25.5g', '4mg', '8mg'],
            ['STARBURST (M)', '1 pkg. (59g)', '233.5', '5g', '0.5g', '0', '50g', '33mg', '2.5mg'],
            ['SYMPHONY (H)', '1 bar (40g)', '209', '13g', 'n/a', '3g', '22.5g', '34.5mg', '94mg'],
            ['TWIX CARAMEL (M)', '1 pkg. (57g)', '284.5', '14g', '5g', '2.5g', '37.5g', '110mg', '51.5mg'],
            ['TWIX P-BUTTER (M)', '1 pkg. (58g)', '307.5', '18.5g', '6.5g', '6g', '30.5g', '158mg', '44.5mg'],
            ['TWIZZLERS STRAWBERRY (H)', '1 pkg (71g)', '262.5', '1g', 'n/a', '2.5g', '66g', '196.5mg', '25mg'],
            ['WHATCHAMACALLIT (H)', '1 bar (51g)', '256.5', '13g', '5.5g', '4.5g', '30g', '116.5mg', '62mg'],
            ['YORK PEPPERMINT PATTIE (H)', '1 lg. pattie (43g)', '149', '4g', 'n/a', '1.5g', '33.5g', '16.5mg', '7.5mg']]
        try:
            try:
                result = sm.get_data()
            except:
                result = '"Function get_data() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert dave_utilities.compare_lists_2d(l2d_solution, result) == True
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function get_data() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: get_data() returns an incorrect result.  Try to compare the data file to the list your function returned to see where things went wrong.</font>")


        i_test_num = i_test_num + 1


        # Test 2: Task 2: Test get_avg_sat_fat() function 



        s_text = ""
        error_calling_function = False
        try:
            try:
                result = sm.get_avg_sat_fat(l2d_solution)
            except:
                result = '"Function get_avg_sat_fat() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert math.isclose(result, 5.5606060606060606)
            s_text = result          
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function get_avg_sat_fat() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: get_avg_sat_fat() should return roughly 5.5606060606060606, but it returns \"" + str(result) + "\".</font>")


        i_test_num = i_test_num + 1

        
        # Test 3: Task 3: Test add_allergy_info() function 

        


        l2d_solution2 = [['3 MUSKETEERS (M)', '1 bar (51g)', '212', '6.5g', '3.5g', '1.5g', '39g', '99mg', '43mg', False, True], ['5TH AVENUE (H)', '1 bar (60g)', '279.5', '12.5g', '3.5g', '4.5g', '41g', '111.5mg', '42mg', True, True], ['100 GRAND BAR (N)', '1 bar (43g)', '200.5', '8g', '5g', '2g', '30.5g', '89mg', '49mg', True, True], ['AFTER EIGHT MINTS (N)', '5 pieces (41g)', '147', '5.5g', '3.5g', '1g', '31.5g', '5mg', '9.5mg', False, False], ['ALMOND JOY (H)', '1 bar (50g)', '232', '14g', '8.5g', '2.5g', '29g', '67mg', '39.5mg', True, True], ['BABY RUTH (N)', '1 bar (60g)', '288.5', '12.5g', '7.5g', '4.5g', '39g', '135.5mg', '24.5mg', True, True], ['BAR NONE (H)', '1 piece (43g)', '224', '14.5g', '9.5g', '3.5g', '22.5g', '44.5mg', '62.5mg', True, True], ['BUTTERFINGER (N)', '1 bar (45g)', '216', '8.5g', '4.5g', '5.5g', '29.5g', '89mg', '12mg', True, True], ["CADBURY'S CARAMELLO (H)", '1 bar (45g)', '220', '11.5g', 'n/a', '2.5g', '29.5g', '55.5mg', '89mg', False, True], ['CHUNKIE (N)', '1 bar (35g)', '173.5', '10g', '8g', '3g', '20g', '18.5mg', '50mg', True, True], ["DEMET'S TURTLES (N)", '1 piece (17g)', '82.5', '4.5g', '2g', '1g', '10g', '16mg', '27mg', True, True], ['GOLDEN III (H)', '1 bar (91g)', '471.5', '30g', 'n/a', '6g', '60g', '79mg', '275mg', True, True], ['GOLDEN ALMOND', '1 bar (85g)', '466', '32g', 'n/a', '9g', '41.5g', '53.5mg', '279mg', True, True], ['GOLDEN ALMOND SOLITAIRES (H)', '1 pkg. (85g)', '455', '31.5g', '13.5g', '10g', '40g', '46mg', '305mg', True, True], ['GOOBERS (N)', '1 pkg (39g)', '200', '13g', '5g', '5.5g', '19g', '16mg', '49.5mg', True, True], ['KIT KAT (H)', '1 bar (43g)', '220.5', '12.5g', '7.5g', '3g', '26.5g', '43.5mg', '77.5mg', False, True], ['KRACKEL (H)', '1 bar (47g)', '236', '13g', '5.5g', '3g', '29g', '64mg', '84mg', False, True], ["M&M'S - PEANUT (M)", '1 pkg. (47g)', '242.5', '12.5g', '5g', '4.5g', '28.5g', '22.5mg', '47.5mg', True, True], ["M&M'S - PLAIN (M)", '1 pkg. (48g)', '236', '10g', '6.5g', '2g', '34g', '29.5mg', '50.5mg', True, True], ['MARS ALMOND BAR (M)', '1 bar (50g)', '233.5', '11.5g', '2.5g', '4g', '31.5g', '85mg', '84mg', True, True], ['MILK WAY (M)', '1 bar (54g)', '228.5', '8.5g', '4g', '2.5g', '38.5g', '129.5mg', '70mg', False, True], ['MOUNDS (H)', '1 pkg. (54g)', '195', '11.5g', '6g', '2g', '31.5g', '67.5mg', '12.5mg', True, True], ['MR. GOODBAR (H)', '1 bar (50g)', '257', '16g', '9g', '6.5g', '25.5g', '17mg', '55.5mg', True, True], ['NESTLE CRUNCH (N)', '1 bar (44g)', '229.5', '11.5g', '6.5g', '2.5g', '28.5g', '58.5mg', '74.5mg', False, True], ['NIBS CHERRY (H)', '1 oz. (28.5g)', '106', '0.5g', 'n/a', '1g', '26.5g', '67mg', '18.5mg', False, False], ['OH HENRY! (N)', '1 bar (57g)', '245.5', '9.5g', '4g', '6g', '37g', '135mg', '62mg', True, True], ['RAISINETS (N)', '1 bar (45g)', '185.5', '7g', '3.5g', '2g', '32g', '16mg', '48.5mg', False, True], ["REESE'S P-BUTTER CUPS (H)", '1 pkg. 2 cups (45g)', '222', '14.5g', '6.5g', '5g', '22g', '130.5mg', '35mg', True, True], ["REESE'S PIECES (H)", '1 bar (55g)', '258', '11.5g', '7.5g', '7g', '34g', '82.5mg', '73mg', True, True], ['ROLO (H)', '1 roll (49g)', '233', '10.5g', '5.5g', '2.5g', '34g', '83.5mg', '65.5mg', False, True], ['SKITTLES (M)', '1 pkg. (57g)', '231', '2.5g', '0.5g', '0', '51.5g', '9mg', '0', False, False], ['SKOR TOFFEE (H)', '1 bar (40g)', '211', '14g', 'n/a', '2g', '22g', '92mg', '45mg', True, True], ['SNICKERS (M)', '1 bar (57g)', '273', '14g', '5g', '4.5g', '34g', '151.5mg', '53.5mg', True, True], ['SPECIAL DARK (H)', '1 bar (41g)', '195', '12.5g', '7g', '2g', '25.5g', '4mg', '8mg', False, True], ['STARBURST (M)', '1 pkg. (59g)', '233.5', '5g', '0.5g', '0', '50g', '33mg', '2.5mg', False, False], ['SYMPHONY (H)', '1 bar (40g)', '209', '13g', 'n/a', '3g', '22.5g', '34.5mg', '94mg', True, True], ['TWIX CARAMEL (M)', '1 pkg. (57g)', '284.5', '14g', '5g', '2.5g', '37.5g', '110mg', '51.5mg', False, True], ['TWIX P-BUTTER (M)', '1 pkg. (58g)', '307.5', '18.5g', '6.5g', '6g', '30.5g', '158mg', '44.5mg', True, True], ['TWIZZLERS STRAWBERRY (H)', '1 pkg (71g)', '262.5', '1g', 'n/a', '2.5g', '66g', '196.5mg', '25mg', False, False], ['WHATCHAMACALLIT (H)', '1 bar (51g)', '256.5', '13g', '5.5g', '4.5g', '30g', '116.5mg', '62mg', True, True], ['YORK PEPPERMINT PATTIE (H)', '1 lg. pattie (43g)', '149', '4g', 'n/a', '1.5g', '33.5g', '16.5mg', '7.5mg', False, True]]
        error_calling_function = False
        try:
            try:
                result = sm.add_allergy_info(l2d_solution)
            except:
                result = '"Function add_allergy_info() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            assert dave_utilities.compare_lists_2d(l2d_solution2, result) == True
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function add_allergy_info() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: add_allergy_info() returns an incorrect result.  Try to compare the data file to the list your function returned to see where things went wrong.</font>")


        i_test_num = i_test_num + 1

        
        # Test 4: Task 4: Test write_safe_candies() function 

        


        error_calling_function = False
        try:
            try:
                sm.write_safe_candies(l2d_solution2)
            except:
                result = '"Function write_safe_candies() caused an error.  Try adding some print statements to it to see what is happening!"'
                error_calling_function = True
            inp_file_1 = open("safe.csv", "r")
            s_data1 = inp_file_1.read()
            inp_file_1.close()
            inp_file_2 = open("correct.csv", "r")
            s_data2 = inp_file_2.read()
            inp_file_2.close()
            assert s_data1.strip() == s_data2.strip()
            passes.append(True)
        except:
            passes.append(False)
            if error_calling_function == True:
                error_msgs.append(" Failed: Function write_safe_candies() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
            else:
                error_msgs.append(" Failed: write_safe_candies() writes an incorrect value to the file.  Look at the file correct.csv to see what should have been written to the file safe.csv.</font>")


        i_test_num = i_test_num + 1

        

        
        ########################################################################
        # End of tests
        ########################################################################

    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")
    return passes, error_msgs, assistant
    

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_18_student_submission.py")
	ret = queue.get()
	ret["result"] = passes
	queue.put(ret)
	return

def main():
	passes, error_msgs,assistant = autoGrader("lab_18_student_submission.py")
	assistant.displayWindow(passes, error_msgs)
if __name__ == "__main__":
    main()

