# Dave Toth

# This module overrides Python's built in input() function so we can get test
# data fed into a program without having to use the command line to redirect
# input.

# Modified from
# https://stackoverflow.com/questions/73250160/how-to-override-the-builtin-method-print

# The list l_data contains the values that will be fed when the user calls
# Python's input function.  Change the list below for each program to have the
# appropriate data.
l_data = [100, 80, 30, 90, 20, 10, 50, 40, 70, 60, 10, 20, 80, 40, 50, 70, 90, 60, 30, 100, 40, 70, 30, 80, 100, 90, 60, 50, 20, 10, -50, -80, -100, -30, -10, -20, -70, -90, -60, -40, 1, 2, 3, 4, 2, 9, 8, 3, 1, 1, 1, 4, 4, 5, 6, 5]


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

