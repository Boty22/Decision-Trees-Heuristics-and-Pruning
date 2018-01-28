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
Run $ py program.py 2 5 training_set.csv validation_set.csv test_set.csv yes
@author: Boty22
"""
import sys

def copyData(filename):
	"""Reads the data and retund a list with the data in the cvs"""
	data=[]
	filename = "probando.csv"
	try:
		fh = open(filename,'r')
	except IOError:
		print('cannot open', filename)
	else:
		for new in fh:
			if new !='\n':
				addIt =  new[:-1].split(',')
				data.append(addIt)
	finally:
		fh.close()
		print(data)
	return data

print(sys.argv)
print("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))

L = int(sys.argv[1])
K = int(sys.argv[2])
training_csv = sys.argv[3]
validation_csv = sys.argv[4]
test_csv = sys.argv[5]
printOrder = sys.argv[6]

a = copyData("probando.csv")

print(L,K,training_csv,validation_csv,test_csv,test_csv,printOrder)

print(a)