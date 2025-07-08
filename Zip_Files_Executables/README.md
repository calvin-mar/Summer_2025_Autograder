This Repository contains files in the form, bolded points are folders:

<<<<<<< HEAD
-  <b>Solutions</b>
  
-  <b>Zip Files_Executables</b>
    - createExe.py
    - README.md
    - requirements.txt
   - <b>Lab_**</b>
       - Empty Student Submission
       - executable_autograder
       - Check
       - redX
       - Necessary testing files
   - <b>Linux_Zips</b>
       - Contains Zip files for each lab
   - <b>Mac_Zips</b>
       - Contains Zip files for each lab
   - <b>Windows_Zips</b>
       - Contains Zip files for each lab

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

- autogradert.py (file)  
- check_all_syntax.py (file)  
- disperse_documents.py (file)  
- input_override.py (file)  
- lab_assistant_template.py (file)  
- README.md (file)  
- test_all_submissions.py (file)
<br/><br/><br/><br/>

1. Each student may be given a copy of the appropriate zip file for the relevant lab. The executables are directly created from the source code as found in the mirroring zip file. All code is runnable directly from idle.
   
2. Create a folder in each lab folder for each student in the format firstname_lastname. When downloading student_submissions, download each student into the appropriate folder.

3. When grading all submissions, run test_all_submissions from idle. The program will disperse all necessary documents to all student folders.

4. Several labs do not have autograders. The autograder has been replaced in these folders with check_all_syntax, which merely checks for banned syntax.

5. If you wish to recompile the executables add whatever changed files are necessary to the folders in Zip_Files_Executables and run createExe.py. Running createExe.py will create the necessary executables, create a zip file without autograder.py or the lab_assistant, and places all zip files into the appropriate folders for the OS.

6. Further information regarding executables may be found in the README within Zip_Files_Exectuables
=======
createExe.py automatically detects what OS your system is on and attempts to compile the executables through 4 different commands (to minimize chances of failure) depending on the location of the pyinstaller package.


<i> Note that throughout the documentation some substitions might be necessary depending on OS: <br />
<b>python3</b>: <b>python</b> <br />
<b>pip</b>: <b>pip3</b> </i> <br />

<h2>Installation: </h2>

1. Install Python https://www.python.org/downloads/

2. Install requirements.txt from the github repository.

3. Run in the terminal: <i> python3 -m pip install -r requirements.txt</i>

To create the executables, place "createExe.py" in the folder that contains all the lab folders:

/Labs/ 

- createExe.py
- lab_02
  - Autograder.py
  -  lab_02_assistant.py
  -   lab_02_student_submission.py
  -   check.png
  -   redX.png
- lab_03
  - ...

- lab_04
  - ...

Then run createExe.py from IDLE or from the terminal. You can only run createExe.py on MAC from the terminal.

<h2>To manually compile:</h2>
<h3>Linux/Mac:</h3>
python3 -m PyInstaller --add-data "lab_xx_assistant.py:." --add-data "check.png:." --add-data "redX.png:." --hidden-import lab_xx_assistant.py:. --hidden-import trace --hidden-import multiprocessing --hidden-import PyQt6.QtWidgets --onefile --noupx --noconsole --distpath . --clean autograder.py

<h3>Windows:</h3>
python -m PyInstaller --add-data "lab_xx_assistant.py;." --add-data "check.png;." --add-data "redX.png;."  --hidden-import lab_xx_assistant.py:. --hidden-import trace --hidden-import multiprocessing --hidden-import PyQt6.QtWidgets --onefile --noupx --noconsole --distpath . --clean autograder.py

<h2>Issues that may occur:</h2>
  Pyinstaller throwing a MoudleNotFound error:
  add </b>--hidden-import MODULE</b> to the pyinstaller compilation command.
<br />
 No module named PyInstaller  
  
  1. Make sure that PyInstaller is installed by using <b>pip install pyinstaller</b>. <br />
  2. Add location of installation to the PATH variable.
>>>>>>> 6277c7d90622f76ff30d9eae9625338231333530
