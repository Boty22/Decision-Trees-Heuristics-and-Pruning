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
#this is the header of the data
attribute_names = a[0]
#print(attribute_names)
#this is the data converted to int
def convert_list_s_int(l_s):
    l_int = []
    for row in l_s:
        l_int.append(list(map(int,row)))
    return l_int

#print("Probando la data:\n")
#print(a[1:])
        
training_data= convert_list_s_int(a[1:])
print(training_data)

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

#print(class_counts(training_data))
    
def partition(rows, attribute):
    """Partitions a dataset.
    For each row in the dataset, chek if it matches the attributee.
    If so, add it to 'true_rows', otherwise, add it to 'false_rows'
    """
    true_rows, false_rows = [], []
    for row in rows:
        if row[attribute] == 1:
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows,false_rows

#print(partition(training_data,1))
strong, weak = partition(training_data,1)
#print("Strong")
#print(strong)
#print("Weak")
#print(weak)
def entropy(rows):
    """Computes the entropy of a list of rows
    """
    counts = class_counts(rows)
    p = float(counts['positives'])
    n = float(counts['negatives'])
    #print(p,n)
    if p == 0 or n == 0:
        return 0;
    else:
        pr = p/(p+n)
        nr = 1 - pr
        #print(pr,nr)
        result = -pr*log2(pr) - nr*log2(nr)
        #print(result)
        return result

#print(entropy(training_data))

def gain(left,right,current_entropy):
    """Information Gain.
    The entropy of the starting node, 
    minus the weight entropy of two child nodes
    """
    p = float(len(left))/(len(left)+len(right))
    return current_entropy - p *entropy(left) - (1-p) * entropy(right)

#print(gain(strong, weak,entropy(training_data)))

high,normal = partition(training_data,0)
#print(gain(high, normal,entropy(training_data)))

def find_best_att(rows):
    """Look for the best attriute
    """
    best_gain = 0
    best_attribute = -1000
    current_entropy = entropy(rows)
    n_features = len(rows[0])-1
    for att in range(n_features):
        true_rows, false_rows = partition(rows, att)
        if len(true_rows) == 0 or len(false_rows)==0:
            continue #The gain will be 0 anyway
        g = gain(true_rows,false_rows,current_entropy)
        if g >= best_gain:
            best_gain = g
            best_attribute = att
    return best_gain, best_attribute

g,att = find_best_att(training_data)
#print(g,attribute_names[att])

class Leaf(object):
    """
    """
    def __init__(self,rows):
        self.prediction = class_counts(rows)
        
class Decision_Node:
    """
    """
    def __init__(self,rows):
        