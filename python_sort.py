#!/usr/bin/python

#  python_sort.py
#  This is a simple Python program that sorts a user's input in numerical or alphabetic order.
#  Created by Daniel on 9/30/18
#  The purpose of this program was to demonstrate the differences and similarites between Perl and Python by writing the same program written in perl, but in python.
#  To run this program simply type "python python_sort.py" and at least two words or numbers of your choice seperated by spaces.

import sys

# assign variable input with varguments from command line.
input = sys.argv

# remove argument with file name from variable 'input'.
input.remove('danielbutton_sort.py')

# sort the values in variable 'input' in alphabetical or numeric order.
input.sort()

# if else statement that determines a different output to be printed if the number of arguments in the 'input' variable is less than 2.
if len(input) < 2:
    print ("\nInvalid command line arguments to program. Please supply two or more strings to sort.\n")
else:
    print("\n")
    
# Remove brackets and seperate arguments in the 'input' variable with a space, then print results.
    print(" ".join(input))
    print("\n")

# End program
