import os
import sys
import shutil
import subprocess


def createExecutables():
    ## Place this document into a top level folder
    ## This script will recreate compile all the executables using pyinstaller
    ## This script should be run from each OS to get the different versions

    # Organize Files and Directories
    cwd = os.getcwd()
    files = []
    dirs = []
    for name in os.listdir(cwd):
        if(os.path.isfile(name)):
            files.append(name)
        else:
            dirs.append(name)
            
    autograders = []
    # Do the Copying
    for folder in dirs:
        for name in os.listdir(folder):
            nameSplit = name.split("_")
            if "autograder.py" in nameSplit:
                autograder = folder + "/" + name
                assistant = folder + "/" + "autograder_assistant.py:."
                specFile = folder + "_autograder.spec"
                result = subprocess.run(["python3","-m","PyInstaller",autograder, "--add-data", assistant, "--hidden-import",
                                         "autograder_assistant.py", "--hidden-import","trace", "--hidden-import", "multiprocessing",
                                         "--hidden-import", "PyQt6.QtWidgets", "--onefile", "--noupx", "--noconsole", "--distpath", folder,
                                        "--clean"], capture_output=True, text=True)
                print("Stdout:", result.stdout)
                print("Stderr:", result.stderr)
                print("Exit Code:", result.returncode)
                result = subprocess.run(["rm",specFile], capture_output=True, text=True)
                print("Stdout:", result.stdout)
                print("Stderr:", result.stderr)
                print("Exit Code:", result.returncode)
    result = subprocess.run(["rm","-r","build"], capture_output=True, text=True)
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr)
    print("Exit Code:", result.returncode)
                        

createExecutables()
