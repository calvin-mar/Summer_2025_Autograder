import os
import sys
import shutil
import re
from zipfile import ZipFile, ZIP_DEFLATED

def create_zips():
    appendage = ""
    tag = "000000"
    if sys.platform == "win32":
        appendage = " (Windows)"
        tab = "Windows"
    elif sys.platform.startswith("linux"):
        appendage = " (Linux)"
        tag = "Linux"
    elif sys.platform == "darwin":
        appendage = " (Mac)"
        tag = "Mac"

    
    cwd = os.getcwd()
    files = []
    dirs = []
    for name in os.listdir(cwd):
        if(os.path.isfile(name)):
            if(len(re.findall("testCompile", name)) == 1):
                os.remove(os.path.join(cwd, name))
        else:
            if(len(re.findall("testCompile", name)) == 1 or name == "build" or name == "dist"):
                shutil.rmtree(os.path.join(cwd, name))
            else:
                dirs.append(name)

    for directory in dirs:
        print("Starting for " + directory)
        # Copy Directory
        copyName = str(directory + appendage)
        shutil.copytree(directory, copyName)

        # Remove executable from original
        for file in os.listdir(directory):
            if(tag in file):
                os.remove(os.path.join(cwd, directory, file))

        # Remove Autograder from copy
        for file in os.listdir(copyName):
            if(len(re.findall("lab_\\d\\d_autograder.py", file)) == 1):
                os.remove(os.path.join(cwd, copyName, file))

        # Create Zip File from copy
        with ZipFile(copyName + ".zip", "w", ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(copyName):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, start=copyName))

        shutil.rmtree(os.path.join(cwd, copyName))
    print("Successfully created all zip files")

create_zips()


            
