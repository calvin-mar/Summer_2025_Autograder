import os
import sys
import shutil

def disperse_documents():
    ## Place this document into a top level folder
    ## This script will copy overall files in the top level folder into all subfolders
    ## This script will not copy over itself.

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
        if(file != "disperse_documents.py" and file != "README.md" and file != "createExe.py"):
            for directory in dirs:
                if(directory != "__pycache__" and directory != "lab_01" and directory != "lab_03" and directory != "lab_19" and directory != "lab_20" and directory != "dice"
                   and directory != "fish" and directory != "Zip_Files_Executables" and directory != "Zip_Files_Sources" and directory != "Solutions" and directory != "mastermind"):
                    shutil.copy(file, directory)

disperse_documents()
