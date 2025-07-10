createExe.py automatically detects what OS your system is on and attempts to compile the executables through 4 different commands (to minimize chances of failure) depending on the location of the pyinstaller package.


<i> Note that throughout the documentation some substitions might be necessary depending on OS: <br />
<b>python3</b>: <b>python</b> <br />
<b>pip</b>: <b>pip3</b> </i> <br />

<h2>Installation: </h2>

1. Install Python https://www.python.org/downloads/

2. Download requirements.txt from the github repository.

3. Run in the terminal: <i> python3 -m pip install -r requirements.txt</i>

To create the executables, ensure that "createExe.py" is in the folder that contains all the lab folders, that is Zip_Files_Executables:

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
python3 -m PyInstaller --add-data "lab_xx_assistant.py:." --add-data "check.png:." --add-data "redX.png:." --hidden-import lab_xx_assistant.py:. --hidden-import trace --hidden-import multiprocessing --hidden-import PyQt6.QtWidgets --hidden-import input_override --onefile --noupx --noconsole --distpath . --clean autograder.py

<h3>Windows:</h3>
python -m PyInstaller --add-data "lab_xx_assistant.py;." --add-data "check.png;." --add-data "redX.png;."  --hidden-import lab_xx_assistant.py:. --hidden-import trace --hidden-import multiprocessing --hidden-import PyQt6.QtWidgets --hidden-import input_override --onefile --noupx --distpath . --clean autograder.py

<h2>Issues that may occur:</h2>
  Pyinstaller throwing a MoudleNotFound error:
  add </b>--hidden-import MODULE</b> to the pyinstaller compilation command.
<br />
 No module named PyInstaller  
  
  1. Make sure that PyInstaller is installed by using <b>pip install pyinstaller</b>. <br />
  2. Add location of installation to the PATH variable.
