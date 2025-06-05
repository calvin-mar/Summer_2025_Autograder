# Python imports
import sys
import math
import ast
import astor
import re
import os
import importlib.util

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
        # Test 1: Test read_data() function with shark file: AAACCCGGGTTTACTTAGCGA\n



        error = ""
        error_code = "none"
        try:

            try:
                result = sm.read_data("shark.txt")
            except:
                result = '"Function read_data() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function read_data() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == "AAACCCGGGTTTACTTAGCGA"
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: read_data(\"shark.txt\") should return AAACCCGGGTTTACTTAGCGA, but it returns " + str(result) + ".</font>")


        i_test_num = i_test_num + 1

        # Test 2: Test read_data() function with elephant file: ACGACGTTTAAACCR



        error = ""
        error_code = "none"
        try:

            try:
                result = sm.read_data("elephant.txt")
            except:
                result = '"Function read_data() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function read_data() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == "ACGACGTTTAAACCR"
            passes.append(True)
        except:
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: read_data(\"elephant.txt\") should return ACGACGTTTAAACCR, but it returns " + str(result) + ".</font>")


        i_test_num = i_test_num + 1

        # is_valid_strand()

        # Test 3: Test is_valid_strand() function with valid strand



        error = ""
        error_code = "none"
        try:

            try:
                result = sm.is_valid_strand("ACGCGTGTATACAAATTT")
            except:
                result = '"Function is_valid_strand() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function is_valid_strand() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == True
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: is_valid_strand() with strand \"ACGCGTGTATACAAATTT\" should return True, but it returns " + str(result) + ".</font>")


        i_test_num = i_test_num + 1


        # Test 4: Test is_valid_strand() function with invalid strands



        error = ""
        error_code = "none"
        try:

            try:
                result1 = sm.is_valid_strand("BCGCGTGTATACAAATTT")
                result2 = sm.is_valid_strand("ADGCGTGTATACAAATTT")
                result3 = sm.is_valid_strand("ACECGTGTATACAAATTT")
                result4 = sm.is_valid_strand("ACGFGTGTATACAAATTT")
                result5 = sm.is_valid_strand("ACGCHTGTATACAAATTT")
                result6 = sm.is_valid_strand("ACGCGIGTATACAAATTT")
                result7 = sm.is_valid_strand("ACGCGTJTATACAAATTT")
                result8 = sm.is_valid_strand("ACGCGTGKATACAAATTT")
                result9 = sm.is_valid_strand("ACGCGTGTLTACAAATTT")
                result10 = sm.is_valid_strand("ACGCGTGTMTACAAATTT")
                result11 = sm.is_valid_strand("ACGCGTGTANACAAATTT")
                result12 = sm.is_valid_strand("ACGCGTGTATOCAAATTT")
                result13 = sm.is_valid_strand("ACGCGTGTATAPAAATTT")
                result14 = sm.is_valid_strand("ACGCGTGTATACQAATTT")
                result15 = sm.is_valid_strand("ACGCGTGTATACARATTT")
                result16 = sm.is_valid_strand("ACGCGTGTATACAASTTT")
                result17 = sm.is_valid_strand("ACGCGTGTATACAAAUTT")
                result18 = sm.is_valid_strand("ACGCGTGTATACAAATVT")
                result19 = sm.is_valid_strand("ACGCGTGTATACAAATTW")
                result20 = sm.is_valid_strand("XCGCGTGTATACAAATTT")
                result21 = sm.is_valid_strand("AYGCGTGTATACAAATTT")
                result22 = sm.is_valid_strand("ACZCGTGTATACAAATTT")
            except:
                passes.append(False)
                result = '"Function is_valid_strand() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function is_valid_strand() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result1 == False
            assert result2 == False
            assert result3 == False
            assert result4 == False
            assert result5 == False
            assert result6 == False
            assert result7 == False
            assert result8 == False
            assert result9 == False
            assert result10 == False
            assert result11 == False
            assert result12 == False
            assert result13 == False
            assert result14 == False
            assert result15 == False
            assert result16 == False
            assert result17 == False
            assert result18 == False
            assert result19 == False
            assert result20 == False
            assert result21 == False
            assert result22 == False
            passes.append(True)
        except:
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: is_valid_strand() with an invalid strand should return False, but it returns " + str(result) + ".</font>")


        i_test_num = i_test_num + 1
        


        # num_differences
        
        # Test 5: Test num_differences() function with 2 strands that have no differences



        error = ""
        error_code = "none"
        try:

            try:
                result = sm.num_differences("AAACCCGGGTTTACT", "AAACCCGGGTTTACT")
            except:
                result = '"Function num_differences() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function num_differences() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == 0
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: num_differences() with 2 identical strands should return 0, but it returns " + str(result) + ".</font>")


        i_test_num = i_test_num + 1


        # Test 6: Test num_differences() function with 2 strands that have 5 differences including one on each end



        error = ""
        error_code = "none"
        try:

            try:
                result = sm.num_differences("TAACGCTGGTGTACA", "AAACCCGGGTTTACT")
            except:
                result = '"Function num_differences() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function num_differences() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == 5
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: num_differences() with these strands \"TAACGCTGGTGTACA\" and \"AAACCCGGGTTTACT\" should return 5, but it returns " + str(result) + ".</font>")


        i_test_num = i_test_num + 1


        # complement
        
        # Test 7: Test complement() function 



        error = ""
        error_code = "none"
        try:

            try:
                result = sm.complement("AAACCCGGGTTTACT")
            except:
                result = '"Function complement() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function complement() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == "TTTGGGCCCAAATGA"
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: complement() with strand \"AAACCCGGGTTTACT\" should return \"TTTGGGCCCAAATGA\", but it returns " + str(result) + ".</font>")


        i_test_num = i_test_num + 1
        

        # get_triplets()
        
        # Test 8: Test get_triplets() function 



        error = ""
        error_code = "none"
        try:

            try:
                result = sm.get_triplets("ACGCGTGTATACAAATTT")
            except:
                result = '"Function get_triplets() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function get_triplets() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == ["ACG", "CGT", "GTA", "TAC", "AAA", "TTT"]
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: get_triplets() with strand \"ACGCGTGTATACAAATTT\" should return [\"ACG\", \"CGT\", \"GTA\", \"TAC\", \"AAA\", \"TTT\"], but it returns " + str(result) + ".</font>")


        i_test_num = i_test_num + 1



        # get_amino_acids()
        
        # Test 9: Test get_amino_acids() function 



        error = ""
        error_code = "none"
        try:

            try:
                result = sm.get_amino_acids(["ACG", "CGT", "GTA", "TAC", "AAA", "TTT"])
            except:
                result = '"Function get_amino_acids() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function get_amino_acids() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result == "TRVYKF"
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: get_amino_acids() with argument [\"ACG\", \"CGT\", \"GTA\", \"TAC\", \"AAA\", \"TTT\"] should return \"TRVYKF\", but it returns " + str(result) + ".</font>")


        i_test_num = i_test_num + 1

        

        # get_acid()

        # Test 10: Test get_acid() function 



        error = ""
        error_code = "none"
        try:
           
            try:
                result1 = sm.get_acid("TTT")
                result2 = sm.get_acid("TTC")
                result3 = sm.get_acid("TTA")
                result4 = sm.get_acid("TTG")
                result5 = sm.get_acid("TCT")
                result6 = sm.get_acid("TCC")
                result7 = sm.get_acid("TCA")
                result8 = sm.get_acid("TCG")
                result9 = sm.get_acid("TAT")
                result10 = sm.get_acid("TAC")
                result11 = sm.get_acid("TAA")
                result12 = sm.get_acid("TAG")
                result13 = sm.get_acid("TGT")
                result14 = sm.get_acid("TGC")
                result15 = sm.get_acid("TGA")
                result16 = sm.get_acid("TGG")
                result17 = sm.get_acid("CTT")
                result18 = sm.get_acid("CTC")
                result19 = sm.get_acid("CTA")
                result20 = sm.get_acid("CTG")
                result21 = sm.get_acid("CCT")
                result22 = sm.get_acid("CCC")
                result23 = sm.get_acid("CCA")
                result24 = sm.get_acid("CCG")
                result25 = sm.get_acid("CAT")
                result26 = sm.get_acid("CAC")
                result27 = sm.get_acid("CAA")
                result28 = sm.get_acid("CAG")
                result29 = sm.get_acid("CGT")
                result30 = sm.get_acid("CGC")
                result31 = sm.get_acid("CGA")
                result32 = sm.get_acid("CGG")
                result33 = sm.get_acid("ATT")
                result34 = sm.get_acid("ATC")
                result35 = sm.get_acid("ATA")
                result36 = sm.get_acid("ATG")
                result37 = sm.get_acid("ACT")
                result38 = sm.get_acid("ACC")
                result39 = sm.get_acid("ACA")
                result40 = sm.get_acid("ACG")
                result41 = sm.get_acid("AAT")
                result42 = sm.get_acid("AAC")
                result43 = sm.get_acid("AAA")
                result44 = sm.get_acid("AAG")
                result45 = sm.get_acid("AGT")
                result46 = sm.get_acid("AGC")
                result47 = sm.get_acid("AGA")
                result48 = sm.get_acid("AGG")
                result49 = sm.get_acid("GTT")
                result50 = sm.get_acid("GTC")
                result51 = sm.get_acid("GTA")
                result52 = sm.get_acid("GTG")
                result53 = sm.get_acid("GCT")
                result54 = sm.get_acid("GCC")
                result55 = sm.get_acid("GCA")
                result56 = sm.get_acid("GCG")
                result57 = sm.get_acid("GAT")
                result58 = sm.get_acid("GAC")
                result59 = sm.get_acid("GAA")
                result60 = sm.get_acid("GAG")
                result61 = sm.get_acid("GGT")
                result62 = sm.get_acid("GGC")
                result63 = sm.get_acid("GGA")
                result64 = sm.get_acid("GGG")
            except:
                result = '"Function my_sort() crashed with an error!"'
                error_code = "crash"
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: Function get_acid() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
            assert result1 == "F"
            assert result2 == "F"
            assert result3 == "L"
            assert result4 == "L"
            assert result5 == "S"
            assert result6 == "S"
            assert result7 == "S"
            assert result8 == "S" 
            assert result9 == "Y"
            assert result10 == "Y" 
            assert result11 == "*"
            assert result12 == "*" 
            assert result13 == "C"
            assert result14 == "C" 
            assert result15 == "*"
            assert result16 == "W" 
            assert result17 == "L"
            assert result18 == "L" 
            assert result19 == "L"
            assert result20 == "L" 
            assert result21 == "P"
            assert result22 == "P" 
            assert result23 == "P"
            assert result24 == "P" 
            assert result25 == "H"
            assert result26 == "H" 
            assert result27 == "Q"
            assert result28 == "Q" 
            assert result29 == "R"
            assert result30 == "R"
            assert result31 == "R"
            assert result32 == "R"
            assert result33 == "I"
            assert result34 == "I"
            assert result35 == "I"
            assert result36 == "M"
            assert result37 == "T"
            assert result38 == "T"
            assert result39 == "T"
            assert result40 == "T"
            assert result41 == "N"
            assert result42 == "N"
            assert result43 == "K"
            assert result44 == "K"
            assert result45 == "S"
            assert result46 == "S"
            assert result47 == "R"
            assert result48 == "R"
            assert result49 == "V"
            assert result50 == "V"
            assert result51 == "V"
            assert result52 == "V"
            assert result53 == "A"
            assert result54 == "A"
            assert result55 == "A"
            assert result56 == "A"
            assert result57 == "D"
            assert result58 == "D"
            assert result59 == "D"
            assert result60 == "D"
            assert result61 == "G"
            assert result62 == "G"
            assert result63 == "G"
            assert result64 == "G"
            passes.append(True)
        except:
            passes.append(False)
            if error_code != "crash":
                error_msgs.append("<font color=black>Test " + str(i_test_num) + " Failed: get_acid() returns an incorrect value for one of the 64 inputs! Which one?  Happy debugging! </font>")


        i_test_num = i_test_num + 1






        
        ########################################################################
        # End of tests
        ########################################################################
    print("...Autograder completed.")
    print()
    print("You may close the Autograder window to exit.")

    return passes, error_msgs, assistant

def testing(queue):
	passes, error_msgs,assistant = autoGrader("lab_13_student_submission.py")
	ret = queue.get()
	ret["result"] = passes
	queue.put(ret)
	return

def main():
	passes, error_msgs,assistant = autoGrader("lab_13_student_submission.py")
	assistant.displayWindow(passes, error_msgs)
if __name__ == "__main__":
    main()
