import os
import sys
import shutil

def disperse_documents():
    ## Place this document into a top level folder
    ## This script will copy overall files in the top level folder into all subfolders
    ## This script will not copy over itself.

    excludedDirs = ["Windows_Zips", "Mac_Zips", "Linux_Zips", ".gitattributes", "__pycache__", "lab_01", "lab_03", "lab_16", "lab_19", "lab_20", "mastermind", ".git", "fish", "dice", "Solutions"]
    excludedFiles = ["createExe.py", "disperse_documents.py", "README.md", "autograder_template.py"]
    
    # Organize Files and Directories
    cwd = os.getcwd()
    files = []
    dirs = []
    subdirs = []
    for name in os.listdir(cwd):
        if(os.path.isfile(name)):
            files.append(name)
        else:
            dirs.append(name)

    # Do the Copying
    for file in files:
        #if(file not in excludedFiles):
        if(file == "autograder.py"):
            for directory in dirs:
                if (directory not in excludedDirs):
                    shutil.copy(file, directory)
                if (directory == "Zip_Files_Executables" or directory == "Zip_Files_Sources"):
                    os.chdir(directory)
                    for name in os.listdir():
                        if(os.path.isdir(name)):
                            if (name not in excludedDirs):
                                shutil.copy(file, name)
                    os.chdir("../")

                    

disperse_documents()
