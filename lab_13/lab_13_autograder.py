# Python imports
import sys
import math
import ast
import astor
import re
import os
from multiprocessing import shared_memory as shm
import importlib.util

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
        i_test_num = 1
        # Test 1: Test read_data() function with shark file: AAACCCGGGTTTACTTAGCGA\n

        try:
            result = assistant.is_inf(sm.read_data, ("shark.txt",))
        except:
            result = "Error"
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: Function read_data() caused an error.  The function might contain an infinite loop or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append(" Failed: Function read_data() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        else:
            if(result == "AAACCCGGGTTTACTTAGCGA"):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: read_data(\"shark.txt\") should return AAACCCGGGTTTACTTAGCGA, but it returns " + str(result) + ".</font>")

        # Test 2: Test read_data() function with elephant file: ACGACGTTTAAACCR

        try:
            result = assistant.is_inf(sm.read_data, ("elephant.txt",))
        except:
            result = "Error"
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: Function read_data() caused an error.  The function might contain an infinite loop or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append(" Failed: Function read_data() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        else:
            if(result == "ACGACGTTTAAACCR"):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: read_data(\"elephant.txt\") should return ACGACGTTTAAACCR, but it returns " + str(result) + ".</font>")

        ##### Task2: is_valid_strand() #####

        # Test 3: Test is_valid_strand() function with valid strand

        try:
            result = assistant.is_inf(sm.is_valid_strand, ("ACGCGTGTATACAAATTT",))
        except:
            result = "Error"
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: Function is_valid_strand() caused an error.  The function might contain an infinite loop or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append(" Failed: Function is_valid_strand() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        else:
            if(result == True):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: is_valid_strand() with strand \"ACGCGTGTATACAAATTT\" should return True, but it returns " + str(result) + ".</font>")

        # Test 4: Test is_valid_strand() function with invalid strands

        results = []
        testCases = ["BCGCGTGTATACAAATTT", "ADGCGTGTATACAAATTT", "ACECGTGTATACAAATTT", "ACGFGTGTATACAAATTT", "ACGCHTGTATACAAATTT",
                     "ACGCGIGTATACAAATTT", "ACGCGTJTATACAAATTT", "ACGCGTGKATACAAATTT", "ACGCGTGTLTACAAATTT", "ACGCGTGTMTACAAATTT",
                     "ACGCGTGTANACAAATTT", "ACGCGTGTATOCAAATTT", "ACGCGTGTATAPAAATTT", "ACGCGTGTATACQAATTT", "ACGCGTGTATACARATTT",
                     "ACGCGTGTATACAASTTT", "ACGCGTGTATACAAAUTT", "ACGCGTGTATACAAATVT", "ACGCGTGTATACAAATTW", "XCGCGTGTATACAAATTT",
                     "AYGCGTGTATACAAATTT", "ACZCGTGTATACAAATTT"]
        try:
            for case in testCases:
                output = assistant.is_inf(sm.is_valid_strand,(case,))
                if "infinite" in output[0]:
                    raise Exception
                else:
                    results.append(output)
        except:
            results = ["Error"]
        if("Infinite" in results):
            passes.append(False)
            error_msgs.append(" Failed: Function is_valid_strand() caused an error.  The function might contain an infinite loop or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        elif("Error" in results):
            passes.append(False)
            error_msgs.append(" Failed: Function is_valid_strand() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        else:
            print(results)
            cumulative = True
            for test in results:
                if test:
                    cumulative = False
            if(cumulative):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: is_valid_strand() with an invalid strand should return False, but it returns " + str(result) + ".</font>")

        ##### Task 3: num_differences #####
        
        # Test 5: Test num_differences() function with 2 strands that have no differences

        try:
            result = assistant.is_inf(sm.num_differences, ("AAACCCGGGTTTACT", "AAACCCGGGTTTACT"))
        except:
            result = "Error"
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: Function num_differences() caused an error.  The function might contain an infinite loop or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append(" Failed: Function num_differences() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
        else:
            if(result == 0):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: num_differences() with 2 identical strands should return 0, but it returns " + str(result) + ".</font>")

        # Test 6: Test num_differences() function with 2 strands that have 5 differences including one on each end

        try:
            result = assistant.is_inf(sm.num_differences, ("TAACGCTGGTGTACA", "AAACCCGGGTTTACT"))
        except:
            result = "Error"
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: Function num_differences() caused an error.  The function might contain an infinite loop or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append(" Failed: Function num_differences() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
        else:
            if(result == 5):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: num_differences() with these strands \"TAACGCTGGTGTACA\" and \"AAACCCGGGTTTACT\" should return 5, but it returns " + str(result) + ".</font>")

        ##### Task 4: complement #####
        
        # Test 7: Test complement() function 

        try:
            result = assistant.is_inf(sm.complement, ("AAACCCGGGTTTACT",))
        except:
            result = "Error"
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: Function complement() caused an error.  The function might contain an infinite loop or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append(" Failed: Function complement() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
        else:
            if(result == "TTTGGGCCCAAATGA"):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: complement() with strand \"AAACCCGGGTTTACT\" should return \"TTTGGGCCCAAATGA\", but it returns " + str(result) + ".</font>")

        ##### Task 5: get_triplets() #####
        
        # Test 8: Test get_triplets() function 

        try:
            result = assistant.is_inf(sm.get_triplets,("ACGCGTGTATACAAATTT",))
        except:
            result = "Error"
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: Function get_triplets() caused an error.  The function might contain an infinite loop or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append(" Failed: Function get_triplets() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
        else:
            if(result == ["ACG", "CGT", "GTA", "TAC", "AAA", "TTT"]):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: get_triplets() with strand \"ACGCGTGTATACAAATTT\" should return [\"ACG\", \"CGT\", \"GTA\", \"TAC\", \"AAA\", \"TTT\"], but it returns " + str(result) + ".</font>")

        ##### Task 6: get_amino_acids() #####
        
        # Test 9: Test get_amino_acids() function 

        try:
            result = assistant.is_inf(sm.get_amino_acids,(["ACG", "CGT", "GTA", "TAC", "AAA", "TTT"],))
        except:
            result = "Error"
        if(result == "Infinite"):
            passes.append(False)
            error_msgs.append(" Failed: Function get_amino_acids() caused an error.  The function might contain an infinite loop or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        elif(result == "Error"):
            passes.append(False)
            error_msgs.append(" Failed: Function get_amino_acids() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
        else:
            if(result == "TRVYKF"):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: get_amino_acids() with argument [\"ACG\", \"CGT\", \"GTA\", \"TAC\", \"AAA\", \"TTT\"] should return \"TRVYKF\", but it returns " + str(result) + ".</font>")

        ##### Task 7: get_acid() #####

        # Test 10: Test get_acid() function 
        results = []
        testCases = ["TTT", "TTC","TTA","TTG","TCT","TCC","TCA","TCG","TAT","TAC","TAA","TAG","TGT","TGC","TGA","TGG","CTT","CTC","CTA","CTG",
                     "CCT","CCC","CCA","CCG","CAT","CAC","CAA","CAG","CGT","CGC","CGA","CGG","ATT","ATC","ATA","ATG","ACT","ACC","ACA","ACG",
                     "AAT","AAC","AAA","AAG","AGT","AGC","AGA","AGG","GTT","GTC","GTA","GTG","GCT", "GCC","GCA","GCG","GAT","GAC","GAA",
                     "GAG","GGT","GGC","GGA","GGG"]
        acids = ["F","F","L","L","S","S","S","S","Y","Y","*","*","C","C","*","W","L","L","L","L","P","P","P","P","H","H","Q","Q","R","R","R","R","I","I","I","M","T","T","T","T","N","N","K","K","S","S","R","R","V","V","V","V","A","A","A","A","D","D","D","D","G","G","G","G"]
        try:
            for case in testCases:
                output = assistant.is_inf(sm.get_acid,(case,))
                if "infinite" in output[0]:
                    raise Exception
                else:
                    results.append(output)
        except:
            results = ["Error"]

        if("Infinite" in results):
            passes.append(False)
            error_msgs.append(" Failed: Function get_acid() caused an error.  The function might contain an infinite loop or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening!</font>")
        elif("Error" in results):
            passes.append(False)
            error_msgs.append(" Failed: Function get_acid() caused an error.  The function might not be defined (perhaps you made a typo in the name) or it may contain code inside it that causes Python to crash.  Try adding some print statements to it to see what is happening! </font>")
        else:
            if(results == acids):
                passes.append(True)
            else:
                passes.append(False)
                error_msgs.append(" Failed: get_acid() returns an incorrect value for one of the 64 inputs! Which one?  Happy debugging! </font>")
   
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
    testSets = []
    passes, error_msgs,assistant = autoGrader("lab_13_student_submission.py")
    assistant.displayWindow(passes, error_msgs, testSets)
if __name__ == "__main__":
    main()
