# Dave Toth

# This module overrides Python's built in input() function so we can get test
# data fed into a program without having to use the command line to redirect
# input.

# Modified from
# https://stackoverflow.com/questions/73250160/how-to-override-the-builtin-method-print

# The list l_data contains the values that will be fed when the user calls
# Python's input function.  Change the list below for each program to have the
# appropriate data.
l_data = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 4, 0, 1, 1, 1, 0, 1, 1, 1, 0]


try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

# Override Python's built in input() function so we can get test data fed into
# a program without having to use the command line to redirect input.
def input(*args, **kwargs):
    i_data = l_data[0]
    del l_data[0]
    print("\n====================\nYour input statement:", args[0])
    print("The value entered by the autograder:", str(i_data), "\n====================\n")
    #__builtin__.input(args[0])
    return i_data

