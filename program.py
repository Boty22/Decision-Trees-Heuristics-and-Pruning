# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:24:49 2018
You have to give 6 values in the command line after the name of the program
<L> integer
<K> integer
<training-set> this is a cvs file
<validation-set> this is a cvs file
<test-set> this is a cvs file
<to print> write yes or no to indicate to the program it you ant to print the decision tree
@author: LUCIA
"""
import sys
print(sys.argv)
print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
L = int(sys.argv[1])
K = int(sys.argv[2])