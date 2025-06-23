import os
import sys
import shutil
import subprocess

def testExe(pyinstaller_path):
    with open("testCompile.py", "w") as f:
      f.write("print('hello world')")
    if pyinstaller_path[0] == None:
        try:
            result = subprocess.run([
            *pyinstaller_path, "testCompile.py",
            "--onefile", "--noupx", "--noconsole",
            "--clean"
            ], capture_output=True, text=True)
        except:
            return False
    else:
        return True
    if result.returncode == 0:
        return True
    else:
        return False

def createExecutables(osName, assistantEnd):

        
    pyinstaller_path = [shutil.which("pyinstaller"),]
    if pyinstaller_path != None:
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
    print(exePasses, pyinstaller_path)
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
                appName = folder + "/" + exeName + ".app"
                assistant = folder + "/" + assistantEnd
                                    
                result = subprocess.run([
                    *pyinstaller_path, autograder,
                    "--add-data", assistant,
                    "--hidden-import", "autograder_assistant",
                    "--hidden-import", "astor",
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
                if sys.platform != "win32":
                    result = subprocess.run(["rm",specFile], capture_output=True, text=True)
                    if result.returncode != 0:
                        print("An error may have occurred")
                        print("Stdout:", result.stdout)
                        print("Stderr:", result.stderr)
                        print("Exit Code:", result.returncode)
                    if sys.platform == "darwin":
                        result = subprocess.run(["rm", "-r",appName], capture_output=True, text=True)
                        if result.returncode != 0:
                            print("An error may have occurred")
                            print("Stdout:", result.stdout)
                            print("Stderr:", result.stderr)
                            print("Exit Code:", result.returncode)
                else:
                    os.remove(specFile)
    if sys.platform != "win32":
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
        
        osName = "Windows"
        assistantEnd = "autograder_assistant.py;."

        createExecutables(osName, assistantEnd)
    elif sys.platform.startswith("linux"): 
        print("Starting on Linux...")
        
        osName = "Linux"
        assistantEnd = "autograder_assistant.py:."

        
        createExecutables(osName, assistantEnd)
    elif sys.platform == "darwin":
        print("Starting on Mac...")
        
        osName = "Mac"
        assistantEnd = "autograder_assistant.py:."


        createExecutables(osName, assistantEnd)
    else:
        print(f"Unsupported OS: {sys.platform}")

main()
