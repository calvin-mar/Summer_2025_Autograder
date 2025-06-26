<h1>Executables:</h1>

createExe.py automatically detects what OS your system is on and attempts to compile the executables through 4 different commands (to minimize chances of failure) depending on the location of the pyinstaller package.

<h2>Installation: </h2>

pip install -r requirements.txt
<b>or</b>
pip3 install -r requirements.txt

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
python3 -m PyInstaller --add-data "lab_xx_assistant.py:." --add-data "check.png" --add-data "redX.png" --hidden-import lab_xx_assistant.py:. --hidden-import trace --hidden-import multiprocessing --hidden-import PyQt6.QtWidgets --onefile --noupx --noconsole --distpath . --clean Autograder.py

<h3>Windows:</h3>
python -m PyInstaller --add-data "lab_xx_assistant.py;." --add-data "check.png" --add-data "redX.png"  --hidden-import lab_xx_assistant.py:. --hidden-import trace --hidden-import multiprocessing --hidden-import PyQt6.QtWidgets --onefile --noupx --noconsole --distpath . --clean Autograder.py

<h2>Issues that may occur:</h2>
  Pyinstaller throwing a MoudleNotFound error:
  --hidden-import MODULE

  Stderr: /Library/Developer/CommandLineTools/usr/bin/python3: No module named PyInstaller  
  
  Make sure:
  pip install pyinstaller
  <br /> <br />
  Find location of pyinstaller with <b>which pyinstaller</b> or by retrying <b>pip install pyinstaller</b> then add to PATH variable
