import os
import sys
import shutil
import subprocess

def linuxFunction():
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
        for name in os.listdir(folder):
            nameSplit = name.split("_")
            if "autograder.py" in nameSplit:
                autograder = folder + "/" + name
                assistant = folder + "/" + "autograder_assistant.py:."
                exeName = folder + "_Linux_Autograder"
                specFile = exeName + ".spec"
                result = subprocess.run(["python3","-m","PyInstaller",autograder, "--add-data", assistant, "--hidden-import",
                                         "autograder_assistant.py", "--hidden-import","trace", "--hidden-import", "multiprocessing",
                                         "--hidden-import", "PyQt6.QtWidgets", "--onefile", "--noupx", "--noconsole", "--distpath", folder,
                                        "--clean", "-n", exeName], capture_output=True, text=True)
                if result.returncode == 0:
                    print(exeName, "has been created! Cleaning up excess files...")
                else:
                    print("An error may have occurred")
                    print("Stdout:", result.stdout)
                    print("Stderr:", result.stderr)
                    print("Exit Code:", result.returncode)                    
                result = subprocess.run(["rm",specFile], capture_output=True, text=True)
                if result.returncode != 0:
                    print("An error may have occurred")
                    print("Stdout:", result.stdout)
                    print("Stderr:", result.stderr)
                    print("Exit Code:", result.returncode)    
    result = subprocess.run(["rm","-r","build"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Success! All executables are ready for use.")
    else:
        print("An error may have occurred")
        print("Stdout:", result.stdout)
        print("Stderr:", result.stderr)
        print("Exit Code:", result.returncode)    

def windowsFunction():

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
        for name in os.listdir(folder):
            nameSplit = name.split("_")
            if "autograder.py" in nameSplit:
                autograder = folder + "/" + name
                assistant = folder + "/" + "autograder_assistant.py:."
                exeName = folder + "_Windows_Autograder"
                specFile = exeName + ".spec"
                result = subprocess.run(["python","-m","PyInstaller",autograder, "--add-data", assistant, "--hidden-import",
                                         "autograder_assistant.py", "--hidden-import","trace", "--hidden-import", "multiprocessing",
                                         "--hidden-import", "PyQt6.QtWidgets", "--onefile", "--noupx", "--noconsole", "--distpath", folder,
                                        "--clean", "-n", exeName], capture_output=True, text=True)

                if result.returncode == 0:
                    print(exeName, "has been created! Cleaning up excess files...")
                else:
                    print("An error may have occurred")
                    print("Stdout:", result.stdout)
                    print("Stderr:", result.stderr)
                    print("Exit Code:", result.returncode)                    
                try:
                    os.remove(specFile)
                except OSError as error:
                    print("An error may have occurred")
                    print(error)
    try:
        result = shutil.rmtree("build")
    except OSError as error:
        print("An error may have occurred")
        print(error)

def macFunction():
    pyinstaller_path = shutil.which("pyinstaller")

    if pyinstaller_path is None:
        print("Error: PyInstaller not found in PATH.")
        print("Please ensure it is installed via `pipx install pyinstaller` or available in your environment.")
        sys.exit(1)

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
        for name in os.listdir(folder):
            nameSplit = name.split("_")
            if "autograder.py" in nameSplit:
                autograder = folder + "/" + name
                assistant = folder + "/" + "autograder_assistant.py:."
                exeName = folder + "_Mac_Autograder"
                specFile = exeName + ".spec"

                result = subprocess.run([
                    pyinstaller_path, autograder,
                    "--add-data", assistant,
                    "--hidden-import", "autograder_assistant.py",
                    "--hidden-import", "trace",
                    "--hidden-import", "multiprocessing",
                    "--hidden-import", "PyQt6.QtWidgets",
                    "--onefile", "--noupx", "--noconsole",
                    "--distpath", folder,
                    "--clean", "-n", exeName
                ], capture_output=True, text=True)

                if result.returncode == 0:
                    print(exeName, "has been created! Cleaning up excess files...")
                else:
                    print("An error may have occurred")
                    print("Stdout:", result.stdout)
                    print("Stderr:", result.stderr)
                    print("Exit Code:", result.returncode)                    
                result = subprocess.run(["rm",specFile], capture_output=True, text=True)
                if result.returncode != 0:
                    print("An error may have occurred")
                    print("Stdout:", result.stdout)
                    print("Stderr:", result.stderr)
                    print("Exit Code:", result.returncode)    
    result = subprocess.run(["rm","-r","build"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Success! All executables are ready for use.")
    else:
        print("An error may have occurred")
        print("Stdout:", result.stdout)
        print("Stderr:", result.stderr)
        print("Exit Code:", result.returncode)    

def createExecutables():
    ## Place this document into a top level folder
    ## This script will recreate compile all the executables using pyinstaller
    ## This script should be run from each OS to get the different versions

    # Organize Files and Directories
    if sys.platform == "win32":
        print("Starting on Windows...")
        windowsFunction()
    elif sys.platform.startswith("linux"): 
        print("Starting on Linux...")
        linuxFunction()
    elif sys.platform == "darwin":
        print("Starting on Mac...")
        macFunction()
    else:
        print(f"Unsupported OS: {sys.platform}")

createExecutables()
