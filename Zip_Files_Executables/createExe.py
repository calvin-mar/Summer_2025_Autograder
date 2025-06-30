import os
import sys
import shutil
import subprocess
import re
from zipfile import ZipFile, ZIP_DEFLATED

def create_zips():
    appendage = ""
    tag = "000000"
    if sys.platform == "win32":
<<<<<<< HEAD
        appendage = " (Windows)"
        tab = "Windows"
    elif sys.platform.startswith("linux"):
        appendage = " (Linux)"
        tag = "Linux"
    elif sys.platform == "darwin":
        appendage = " (Mac)"
=======
        appendage = "_Windows"
        tag = "Windows"
    elif sys.platform.startswith("linux"):
        appendage = "_Linux"
        tag = "Linux"
    elif sys.platform == "darwin":
        appendage = "_Mac"
>>>>>>> e971ec8bb20612eb932956391a85ad97181fe9f4
        tag = "Mac"

    
    cwd = os.getcwd()
    files = []
    dirs = []
    for name in os.listdir(cwd):
        if(os.path.isfile(name)):
            pass
        else:
            dirs.append(name)

    for directory in dirs:
<<<<<<< HEAD
        print("Starting for " + directory)
=======
        if directory == "Mac_Zips" or directory == "Linux_Zips" or directory == "Windows_Zips":
            continue
        print("Creating ZIP for " + directory)
>>>>>>> e971ec8bb20612eb932956391a85ad97181fe9f4
        # Copy Directory
        copyName = str(directory + appendage)
        shutil.copytree(directory, copyName)

        # Remove executable from original
        for file in os.listdir(directory):
            if(tag in file):
                if sys.platform == "darwin":
<<<<<<< HEAD
                    subprocess.run = ("rm", "-r", os.path.join(cwd, directory, file))
=======
                    result = subprocess.run(["rm", os.path.join(cwd, directory, file)])
>>>>>>> e971ec8bb20612eb932956391a85ad97181fe9f4
                else:
                    os.remove(os.path.join(cwd, directory, file))

        # Remove Autograder from copy
        for file in os.listdir(copyName):
<<<<<<< HEAD
            if(len(re.findall("lab_\\d\\d_assistant.py", file)) == 1):
=======
            if(len(re.findall("lab_\\d\\d_assistant.py", file)) == 1 or file=="autograder.py"):
>>>>>>> e971ec8bb20612eb932956391a85ad97181fe9f4
                os.remove(os.path.join(cwd, copyName, file))

        # Create Zip File from copy
        with ZipFile(copyName + ".zip", "w", ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(copyName):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, start=copyName))

        shutil.rmtree(os.path.join(cwd, copyName))
<<<<<<< HEAD
=======

        os.replace(os.path.join(cwd, copyName + ".zip"), os.path.join(cwd, tag + "_Zips", copyName + ".zip"))
>>>>>>> e971ec8bb20612eb932956391a85ad97181fe9f4
    print("Successfully created all zip files")

def testExe(pyinstaller_path):
    b_success = False
    with open("testCompile.py", "w") as f:
      f.write("print('hello world')")
    
    try:
        result = subprocess.run([
        *pyinstaller_path, "testCompile.py"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            b_success = True
    except:
        pass

    cwd = os.getcwd()
    for name in os.listdir(cwd):
        if(os.path.isfile(name)):
            if(len(re.findall("testCompile", name)) == 1):
                os.remove(os.path.join(cwd, name))
        else:
            if(len(re.findall("testCompile", name)) == 1 or name == "build" or name == "dist"):
                shutil.rmtree(os.path.join(cwd, name))
    
    return b_success

def createExecutables(osName, addDataEnd):

        
    pyinstaller_path = [shutil.which("pyinstaller"),]
    if pyinstaller_path == None:
        exePasses = False
    else:
        exePasses = testExe(pyinstaller_path)
    if exePasses == False:
        pyinstaller_path = ["pyinstaller",]
        exePasses = testExe(pyinstaller_path)
    if exePasses == False:
        pyinstaller_path = ["python", "-m", "PyInstaller"]
        exePasses = testExe(pyinstaller_path)
    if exePasses == False:
        pyinstaller_path = ["python3", "-m", "PyInstaller"]
        exePasses = testExe(pyinstaller_path)
    print("Pyinstaller path found?", exePasses, ";using", pyinstaller_path)
    cwd = os.getcwd()
    files = []
    dirs = []

    for name in os.listdir(cwd):
        if(os.path.isfile(name)):
            files.append(name)
        else:
            dirs.append(name)
    
    # Do the Copying
    for folder in dirs:
        if folder == "Mac_Zips" or folder == "Linux_Zips" or folder == "Windows_Zips":
            continue
        for name in os.listdir(folder):
            nameSplit = name.split("_")
            if "autograder.py" in nameSplit:
                autograder = folder + "/" + name
                exeName = folder + "_"+ osName + "_Autograder"
                specFile = exeName + ".spec"
                appName = folder + "/" + exeName + ".app"
                assistant = folder + "/" + folder + "_assistant.py" + addDataEnd
                assistantImport = folder + "_assistant"
                print(assistant, assistantImport)
                check = folder + "/check.png" + addDataEnd
                redX = folder + "/redX.png" + addDataEnd
                                    
                result = subprocess.run([
                    *pyinstaller_path, autograder,
                    "--add-data", assistant,
                    "--add-data", check,
                    "--add-data", redX,
                    "--hidden-import", assistantImport,
                    "--hidden-import", "astor",
                    "--hidden-import", "trace",
                    "--hidden-import", "multiprocessing",
                    "--hidden-import", "PyQt6.QtWidgets",
                    "--hidden-import", "csc170_lists_data",
                    "--hidden-import", "input_override",
                    "--onefile",
                    "--noupx", "--noconsole",
                    "--distpath", folder,
                    "--clean", "-n",
                    exeName,
                    #"--debug", "all"
                ], capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(exeName, "has been created!")
                else:
                    print("An error may have occurred")
                    print("Stdout:", result.stdout)
                    print("Stderr:", result.stderr)
                    sys.exit(result.returncode)
                os.remove(specFile)
                if sys.platform == "darwin":
                    shutil.rmtree(appName)
    try:
        shutil.rmtree("build")
        print("Success! All executables are ready for use.")
    except:
        print("An error may have occurred while attempting to delete 'build'")
        sys.exit(1)

def main():
    ## Place this document into a top level folder
    ## This script will recreate compile all the executables using pyinstaller
    ## This script should be run from each OS to get the different versions

    # Organize Files and Directories
    if sys.platform == "win32":
        print("Starting on Windows...")
        
        osName = "Windows"
        addDataEnd = ";."

        createExecutables(osName, addDataEnd)
    elif sys.platform.startswith("linux"): 
        print("Starting on Linux...")
        
        osName = "Linux"
        addDataEnd = ":."

        
        createExecutables(osName, addDataEnd)
    elif sys.platform == "darwin":
        print("Starting on Mac...")
        
        osName = "Mac"
        addDataEnd = ":."


        createExecutables(osName, addDataEnd)
    else:
        print(f"Unsupported OS: {sys.platform}")

    create_zips()


main()
