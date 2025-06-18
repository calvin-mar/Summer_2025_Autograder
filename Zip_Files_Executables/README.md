Requirements:
pip install pyinstaller

Additionally on mac:
pip3 install opencv-python-headless

To create the executables, place "createExecutables.py" in the folder that contains all the lab folders,along with autograder_assistant:

Labs 
-> createExecutables.py
-> autograder_assistant.py
-> lab_02
  -> lab_02_autograder.py
  -> autograder_assistant.py
  -> lab_02_student_submission.py
-> lab_03
  -> ...
-> lab_4
  -> ...

createExecutables is has 3 distinct functions for windows, linux, and mac. You can edit the parameters for each seperately.

if you would like to manually compile a file:
python -m PyInstaller --add-data "autograder_assistant.py:." --hidden-import autograder_assistant --hidden-import trace --hidden-import multiprocessing --hidden-import PyQt6.QtWidgets --onefile --noupx --noconsole --distpath . --clean lab_xx_autograder.py

Issues that may occur:
  Pyinstaller throwing a MoudleNotFound error:
  --hidden-import MODULE

  Stderr: /Library/Developer/CommandLineTools/usr/bin/python3: No module named PyInstaller  
  
  Make sure:
  pip install pyinstaller
  
  Try:
    python3 -m PyInstaller --version
  
  Or:
    Find location of pyinstaller with “which pyinstaller”
    Add to PATH variable
  
  Or if using homebrew (MAC):
    Brew install pyinstaller
