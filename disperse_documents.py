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
<<<<<<< HEAD
        if(file != "disperse_documents.py" and file != "test_all_submissions.py" and file != "README.md"):
=======
        if(file != "disperse_documents.py" and file != "test_all_submissions.py"and file != "README.md"):
>>>>>>> 49a11712bf04e4605173f6384974b1ac28de508c
            for directory in dirs:
                if(directory != "__pycache__" and directory != "lab_01" and directory != "lab_03" and directory != "lab_19") and directory != "lab_20":
                    shutil.copy(file, directory)

disperse_documents()
