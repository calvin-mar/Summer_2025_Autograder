import os
import sys
import shutil
import subprocess

def createExecutables(pyinstaller_path, osName, assistantEnd):
    if pyinstaller_path is None:
        print("Error: PyInstaller not found in PATH.")
        print("Please ensure the installation path exists in your PATH variable. 'which pyinstaller', 'echo $PATH'. You can also try running createExe from the terminal.")
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
                exeName = folder + "_"+ osName + "_Autograder"
                specFile = exeName + ".spec"
                assistant = folder + "/" + assistantEnd
                                    
                result = subprocess.run([
                    pyinstaller_path, autograder,
                    "--add-data", assistant,
                    "--hidden-import", "autograder_assistant.py",
                    "--hidden-import", "trace",
                    "--hidden-import", "multiprocessing",
                    "--hidden-import", "PyQt6.QtWidgets",
                    "--hidden-import", "csc170_lists_data",
                    "--onefile", "--noupx", "--noconsole",
                    "--distpath", folder,
                    "--clean", "-n", exeName
                ], capture_output=True, text=True)
                if result.returncode == 0:
                    print(exeName, "has been created!")
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

def main():
    ## Place this document into a top level folder
    ## This script will recreate compile all the executables using pyinstaller
    ## This script should be run from each OS to get the different versions

    # Organize Files and Directories
    if sys.platform == "win32":
        print("Starting on Windows...")
        pyinstaller_path = "python -m PyInstaller"
        osName = "Windows"
        assistantEnd = "autograder_assistant.py;."

        createExecutables(pyinstaller_path, osName, assistantEnd)
    elif sys.platform.startswith("linux"): 
        print("Starting on Linux...")
        
        pyinstaller_path = shutil.which("pyinstaller")
        osName = "Linux"
        assistantEnd = "autograder_assistant.py:."

        
        createExecutables(pyinstaller_path, osName, assistantEnd)
    elif sys.platform == "darwin":
        print("Starting on Mac...")
        
        pyinstaller_path = shutil.which("pyinstaller")
        osName = "Mac"
        assistantEnd = "autograder_assistant.py:."


        createExecutables(pyinstaller_path, osName, assistantEnd)
    else:
        print(f"Unsupported OS: {sys.platform}")

main()
