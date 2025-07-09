This README provides an overview of the files structure and a high level understanding of the files within the folder. 
For a more detailed description of how to use the autograder see the  "How_to_use.txt" file.

This Repository contains files in the form, bolded points are folders:

-  <b>Zip Files_Executables</b>
    - createExe.py
    - README.md
    - requirements.txt
   - <b>Lab_**</b>  
       - Empty Student Submission
       - autograder.py
       - lab_assistant
       - Check
       - redX
       - Necessary testing files
   - <b>Linux_Zips</b>
       - Contains Zip files for each lab with Linux executables
   - <b>Mac_Zips</b>
       - Contains Zip files for each lab with Mac executables
   - <b>Windows_Zips</b>
       - Contains Zip files for each lab with Windows executables

-  <b>Zip Files_Sources</b>
    - <b>lab_**</b>  
       - Empty Student Submission  
       - lab_assistant  
       - autograder.py  
       - Check  
       - redX  
       - Necessary testing files
    - Also contains Zip files for each lab 

-  <b>Lab Folders (each containing the following)</b>
   - lab_**_assistant
   - autograder.py
   - Check.png
   - redX.png
   - test_all_submissions
   - Necessary testing files
   - *Required: Folder for each student. Currently contains examples: student_name1 and student_name2*
     
- <b>development_tools</b>
   - autograder.py  
   - check_all_syntax.py   
   - disperse_documents.py 
   - input_override.py   
   - lab_assistant_template.py
   - lab_global_variables_assistant_template.py
   - test_all_submissions.py
   - <b>Solutions</b>
   - <b>json_autograder_development</b>
      - json_autograder.py
      - json_autograder_documentation.txt
      - json_test_all_submissions.py
      - lab_06_testFile.json
      - template.json
    
- README.md
- How_to_use.txt  

<br/><br/><br/>

<b>Short Usage Notes (see How_to_use.txt for more details)</b>
1. Each student may be given a copy of the appropriate zip file for the relevant lab. The executables are directly created from the source code as found in the mirroring zip file. All code is runnable directly from idle.
   
2. Create a folder in each lab folder for each student in the format firstname_lastname. When downloading student_submissions, download each student into the appropriate folder.

3. When grading all submissions, run test_all_submissions from idle. The program will disperse all necessary documents to all student folders.

4. Several labs do not have autograders. test_all_submissions has been replaced in these folders with check_all_syntax, which merely checks for banned syntax.

5. If you wish to recompile the executables add whatever changed files are necessary to the folders in Zip_Files_Executables and run createExe.py. Running createExe.py will create the necessary executables, create a zip file without autograder.py or the lab_assistant, and places all zip files into the appropriate folders for the OS.

6. Further information regarding executables may be found in the README within Zip_Files_Exectuables

<br/>
<b>Folder development_tools Notes</b>
   
8. The development_tools folder contains files useful for expanding the current set of labs. lab_function_assistant_template.py demonstrates how to create a new lab_assistant to test functions. lab_global_variables_assistant_template.py demonstrates how to create a new lab_assistant to test global variables. The fundamentals may be mixed and matched in both.
   
10. The development_tools folder also contains autograder.py, check_all_syntax.py, input_override.py, and test_all_submissions.py. These are the necessary files for most testing. If changes wish to be made, particularly to autograder.py, make them here. Use disperse_documents to send the file you wish to change everywhere, by moving the file to be dispersed and disperse_documents into the primary folder and running disperse_documents.
    
12. The development_tools folder contains the solutions for all labs with autograders.
    
14. The development_tools folder also contains work in progress regarding the implementation of an autograder using json files. This autograder would be more easily expandable to new labs and new tests, than the current version. It is incomplete and thorough explanations may be found in the json_autograder_documentation.txt document. 
