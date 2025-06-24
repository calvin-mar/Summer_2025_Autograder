try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

# Override Python's built in input() function so we can get test data fed into
# a program without having to use the command line to redirect input.
class InputException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def input(*args, **kwargs):    
    try:
        l_data = shm.ShareableList(sequence=None,name="l_data")
    except:
        l_data = [None]
    i_data = l_data[0]
    if(i_data == None):
        raise InputException("InputException")

    for i in range(len(l_data)-1):
        l_data[i] = l_data[i+1]
    # Set last input in list of inputs to None
    l_data[-1] = None
    
    print("\n====================\nYour input statement:", args[0])
    print("The value entered by the autograder:", str(i_data), "\n====================\n")
    
    l_data.shm.close()
    
    return i_data
