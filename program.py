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

Run $ python program.py 2 5 training_set.csv validation_set.csv test_set.csv yes

@author: Boty22
"""
#import sys
from math import log2
import numpy as np

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

def entropy(n,p):
    """Computes entropy
    p and n are the number of positive and negative examples in the resulting class"""
    if p == 0 or n == 0:
        return 0;
    else:
        pr = p/(p+n)
        nr = n/(p+n)
        result = -pr*log2(pr) - nr*log2(nr)
        print(result)
        return result

def gain(cn,cp,a0n,a0p,a1n,a1p):
    total = cn + cp
    result = entropy(cn,cp)-(a0n+a0p)/total*entropy(a0n,a0p)-(a1n+a1p)/total*entropy(a1n,a1p)
    #print(result)
    return result

#tHE FOLLOWING PART IS TO READ FROM COMMAND LINE
"""
print(sys.argv)
print("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
#Testing which values we have in the command line
L = int(sys.argv[1])
K = int(sys.argv[2])
training_csv = sys.argv[3]
validation_csv = sys.argv[4]
test_csv = sys.argv[5]
print_order = sys.argv[6]
print(L,K,training_csv,validation_csv,test_csv,test_csv,print_order)
"""

#Copying the file to a list 
training_file = "probando.csv"
a = copyData(training_file)
#print(a)
#keep the attribute names and the data in different structures
attribute_names = a[0]
print(attribute_names)
training_data= np.array(a[1:-1],np.int8)
print (training_data)

print(training_data.shape)
num_columns=training_data.shape[1]
num_rows=training_data.shape[0]
#itereate in columns
for i in range(num_columns-1):
    #iterate in rows
    att_0n = 0 #Attribute with value "0" results negative
    att_0p = 0 #Attribute with value "0" results positive
    att_1n = 0 #Attribute with value "1" results negative
    att_1p = 0 #Attribute with value "1" results positive
    class_n = 0
    class_p = 0
    best_gain = -10.000000
    selected_att = -1000
    for j in range(num_rows):
        if training_data[j,i] == 0:
            if training_data[j,-1] == 0: #the class is negative
                att_0n = att_0n + 1
                class_n = class_n + 1
            else: #the class is positive
                att_0p = att_0p + 1
                class_p = class_p + 1
        else:# value of the attribute is 1
            if training_data[j,-1] == 0: #the class is negative
                att_1n = att_1n + 1
                class_n = class_n + 1
            else: #the class is positive
                att_1p = att_1p + 1
                class_p = class_p + 1
    print("For the attribute ",i,":")
    print(class_n, class_p, att_0n, att_0p, att_1n,att_1p)
    #Compute information gain
    g = gain(class_n, class_p, att_0n, att_0p, att_1n,att_1p)
    print("The gain for attribute ",i," is: ",g)
    if g >= best_gain:
        best_gain = g
        selected_att= i
print(best_gain,i)