<h1>Executables:</h1>

createExe.py automatically detects what OS your system is on and attempts to compile the executables through 4 different commands (to minimize chances of failure) depending on the location of the pyinstaller package.

<h2>Installation: </h2>

pip install -r requirements.txt
<b>or</b>
pip3 install -r requirements.txt

To create the executables, place "createExecutables.py" in the folder that contains all the lab folders:

/Labs/ 

- createExecutables.py
- lab_02
  - lab_02_autograder.py
  -  autograder_assistant.py
  -   lab_02_student_submission.py
- lab_03
  - ...

- lab_04
  - ...

<h2>To manually compile:</h2>
python -m PyInstaller --add-data "autograder_assistant.py:." --hidden-import autograder_assistant --hidden-import trace --hidden-import multiprocessing --hidden-import PyQt6.QtWidgets --onefile --noupx --noconsole --distpath . --clean lab_xx_autograder.py

<h2>Issues that may occur:</h2>
  Pyinstaller throwing a MoudleNotFound error:
  --hidden-import MODULE

  Stderr: /Library/Developer/CommandLineTools/usr/bin/python3: No module named PyInstaller  
  
  Make sure:
  pip install pyinstaller
  <br /> <br />
  Find location of pyinstaller with “which pyinstaller” then add to PATH variable
