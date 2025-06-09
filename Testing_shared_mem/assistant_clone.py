import threading
from multiprocessing.shared_memory import SharedMemory
from multiprocessing.shared_memory import ShareableList

import sys
import os
'''
def eat():
    while(True):
        s = input("4: ")
    return 1
'''
l_data = []


try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

# Override Python's built in input() function so we can get test data fed into
# a program without having to use the command line to redirect input.
def input(*args, **kwargs):
    #i_data = l_data[0]
    #del l_data[0]
    try:
        l_data = ShareableList(name="mySharedList")
    except Exception as e:
        l_data = ShareableList(name="myNewSharedList")
        print("INPUT ASSIGNING l_data", e)
    #print("SHARED INPUT LIST", l_data)
    i_data = l_data[0]
    if l_data[0] == None:
        l_data[0] = None
        #print(l_data[0])
        #print("hi?")
    i=0
    new_data = []
    for item in l_data:
        if i==0:
            #print("don't append")
            i+=1
        else:
            new_data.append(item)
        
    #print("NEW DATA", new_data)
    try:
        index = 0
        for item in new_data:
            l_data[index] = item
            index+=1
        l_data[index] = None
    except Exception as e:
        print(e)
    l_data.shm.close()
    
    #print("NEW DATA", new_data)

    #print("SHARED INPUT LIST", l_data)
    
    #print(i_data)
    #print("\n====================\nYour input statement:", args[0])
    #print("The value entered by the autograder:", str(i_data), "\n====================\n")
    #__builtin__.input(args[0])
    return i_data

def wrapper(function, parameter_list, result):
    try:
        function(*parameter_list)
        #result[0] = "All Good"
    except Exception as e:
        print("WRAPPER CAUGHT", e)
        #result[0] = "Error"
        
def is_inf(function, parameter_list=(), input_list=[]):
    # Return either Infinite, Error, or All Good
    #global l_data
    #l_data = ShareableList(name="mySharedList")
    #l_data = input_list
    result =["Error"]
    #print(l_data)
    p = threading.Thread(target=wrapper, args=(function,parameter_list, result), daemon=True)
    p.start()
    p.join(3)
    if result[0] == "Error":
        return "Error"
    elif p.is_alive():
        return "Infinite"
    else:
        return "All Good"

