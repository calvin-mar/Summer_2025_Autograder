import threading
from multiprocessing.shared_memory import SharedMemory
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
    print("Before")
    shared_mem = SharedMemory(name="shm", create=False)
    #i_data = l_data[0]
    #del l_data[0]
    i_data = shared_mem[0]
    print(i_data)
    print("\n====================\nYour input statement:", args[0])
    print("The value entered by the autograder:", str(i_data), "\n====================\n")
    #__builtin__.input(args[0])
    return i_data

def wrapper(function, parameter_list, result):
    try:
        function(*parameter_list)
        result[0] = "All Good"
    except Exception as e:
        result[0] = "Error"
        
def is_inf(function, parameter_list=(), input_list=[]):
    # Return either Infinite, Error, or All Good
    #global l_data
    #l_data = []
    #l_data = input_list
    shared_mem = SharedMemory(name="shm", size = 1024)
    shared_mem.buf[0] = 1
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

