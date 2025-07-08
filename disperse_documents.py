import os
import sys
import shutil

def disperse_documents():
    ## Place this document into a top level folder
    ## This script will copy overall files in the top level folder into all subfolders
    ## This script will not copy over itself.

    excludedDirs = ["Windows_Zips", "Mac_Zips", "Linux_Zips", "__pycache__", "lab_01", "lab_03",
                    "lab_16", "lab_19", "lab_20", "mastermind", ".git", "fish", "dice", "Solutions", "Zip_Files_Executables", "Zip_Files_Sources", ".gitignore"]
    checkAllSyntax = ["lab_01", "lab_03", "lab_16", "lab_19", "lab_20", "mastermind", "fish", "dice"]
    excludedFiles = ["notesForStudents.txt", "createExe.py", "disperse_documents.py", "README.md", "autograder_template.py", "lab_assistant_template.py", ".gitignore"]
    
    # Organize Files and Directories
    files = []
    dirs = []
    subdirs = []
    for name in os.listdir():
        if(os.path.isfile(name)):
            files.append(name)
        else:
            dirs.append(name)

    # Do the Copying

    for file in files:
        
        if(file not in excludedFiles):
        #if(file == "autograder.py"):
            for directory in dirs:
                matched = False
                print(file)
                if ((directory not in excludedDirs) and file != "check_all_syntax.py"):
                    shutil.copy(file, directory)
                    matched = True
                elif (directory == "Zip_Files_Executables" or directory == "Zip_Files_Sources"):
                    matched = True
                    os.chdir(directory)
                    for name in os.listdir():
                        if(os.path.isdir(name) and (name not in excludedDirs) and file != "check_all_syntax.py"):
                            shutil.copy(file, name)
                        elif (os.path.isdir(name) and (name in checkAllSyntax) and file == "check_all_syntax.py"):
                            shutil.copy(file, name)
                    os.chdir("../")
                elif ((directory in checkAllSyntax) and file == "check_all_syntax.py"):
                    matched = True
                    print("copying checkall")
                    shutil.copy(file, directory)
                #if matched == False:
                    #print("none matched", directory, file)

                    
def main():
    disperse_documents()

main()
