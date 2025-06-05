# Dave Toth

# This module overrides Python's built in input() function so we can get test
# data fed into a program without having to use the command line to redirect
# input.

# Modified from
# https://stackoverflow.com/questions/73250160/how-to-override-the-builtin-method-print

# The list l_data contains the values that will be fed when the user calls
# Python's input function.  Change the list below for each program to have the
# appropriate data.
l_data = [0, -9, 5, 77, -1, 5, 6, 2, -1, 5, 6, 2, -1, 8, 100, 50, 60, 40, 70, 100, 5, 60, 5, 70, 1, 6, 5, 4, 77, 2.5]


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

