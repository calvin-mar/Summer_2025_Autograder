import os
import sys
import shutil

def replace_documents(cwd, filename):
    for name in os.listdir(cwd):
        if(os.path.isfile(name) and name == filename):
            shutil.copy(filename, cwd)
        elif(os.path.isdir(name)):
            replace_documents(os.path.join(cwd, name), filename)
            
def search_all(cwd, filename):
    for name in os.listdir(cwd):
        if(os.path.isdir(name)):
                replace_documents(os.path.join(cwd, name), filename)
                
def main():
    '''
    This file is the more powerful version of disperse_documents. This functions takes a file and finds all old versions in subfolders to replace them.

    For example, if autograder.py is updated, run this file in the primary folder with the new autograder.py. The new version of autograder will replace
    all versions of the fild in all subfolders.

    This file can be run either from IDLE or from the command line
    '''
    if(len(sys.argv) > 1):
        double_check = input("Are you sure you want to replace all files in this folder and subfolders with the name " + str(sys.argv[1]) + ". YES or NO: ")
        while(double_check != "YES" and double_check != "NO"):
            double_check = input("Are you sure you want to replace all files in this folder and subfolders with the name " + str(sys.argv[1]) + ". YES or NO: ")
        if(double_check == "YES"):
            search_all(os.getcwd(), sys.argv[1])
        else:
            sys.exit(1)
    else:
        filename = input("What file do you want to replace everywhere: ")
        double_check = input("Are you sure you want to replace all files in this folder and subfolders with the name " + str(filename) + ". YES or NO: ")
        while(double_check != "YES" and double_check != "NO"):
            double_check = input("Are you sure you want to replace all files in this folder and subfolders with the name " + str(filename) + ". YES or NO: ")
        if(double_check == "YES"):
            search_all(os.getcwd(), filename)
        else:
            sys.exit(1)

main()
