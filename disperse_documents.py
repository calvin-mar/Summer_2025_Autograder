import os
import sys
import shutil

def disperse_documents():
    ## Place this document into a top level folder
    ## This script will copy overall files in the top level folder into all subfolders
    ## This script will not copy over itself.

    excludedDirs = ["__pycache__", "lab_01", "lab_03", "lab_19", "lab_20", "mastermind", ".git", "fish", "dice","Zip_Files_Executables", "Zip_Files_Sources", "Solutions"]
    excludedFiles = ["createExe.py", "disperse_documents.py", "README.md"]
    
    # Organize Files and Directories
    cwd = os.getcwd()
    files = []
    dirs = []
    for name in os.listdir(cwd):
        if(os.path.isfile(name)):
            files.append(name)
        else:
            dirs.append(name)

    # Do the Copying
    for file in files:
        if(file not in excludedFiles):
            for directory in dirs:
                if (directory not in excludedDirs):
                    shutil.copy(file, directory)

disperse_documents()
