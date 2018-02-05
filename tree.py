# -*- coding: utf-8 -*-
"""
Created on Sat Jan  25 15:42:16 2018

@author: LUCIA
This program works with attributes and a class that cantake the values 0 or 1
"""
import sys
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

#Copying the file to a list 
training_file = "probando.csv"
a = copyData(training_file)
#print(a)
#keep the attribute names and the data in different structures
attribute_names = a[0]
print(attribute_names)
training_data= np.array(a[1:-1],np.int8)
print (training_data)

def class_counts(rows):
    """ Counts how many positives and negatives a class has
    """
    counts = {'positives':0, 'negatives':0}
    for row in rows:
        if row[-1]==1:
            counts['positives'] += 1
        else:
            counts['negatives'] += 1
    return counts

# print(class_counts(training_data))
    
def partition(rows, attribute):
    """Partitions a dataset.
    For each row in the dataset, chek if it matches the attributee.
    If so, add it to 'true_rows', otherwise, add it to 'false_rows'
    """
    true_rows, false_rows = [], []
    for row in rows:
        if row[attribute] == 1:
            