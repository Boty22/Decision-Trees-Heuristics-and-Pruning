# -*- coding: utf-8 -*-
"""
Created on Sat Jan  25 15:42:16 2018

@author: LUCIA
This program works with attributes and a class that cantake the values 0 or 1
"""
import sys
from math import log2
#import numpy as np

from random import randint

"""-------------------GETTING DATA FROM COMMAN LINE-------------------------"""

def copyData(filename):
    """Reads the data and retund a list with the data in the cvs"""
    data=[]
    #filename = "training_set.csv"
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
        #print(data)
    return data

#Copying the file to a list 
training_file = "training_set.csv"
testing_file = "test_set.csv"
validation_file = "validation_set.csv"

a = copyData(training_file)
b = copyData(testing_file)
c = copyData(validation_file)
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
testing_data= convert_list_s_int(b[1:])
validation_data = convert_list_s_int(c[1:])
#print(training_data)


"""-------------------------- GLOBAL VARIABLES----------------------------"""
current_node_id = 0
x=0

"""----------------------------------------------------------------"""

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
#strong, weak = partition(training_data,1)
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

def gain_e(left,right,current_entropy):
    """Information Gain.
    The entropy of the starting node, 
    minus the weight entropy of two child nodes
    """
    p = float(len(left))/(len(left)+len(right))
    return current_entropy - p *entropy(left) - (1-p) * entropy(right)

#print(gain(strong, weak,entropy(training_data)))

def varimp(rows):
    counts = class_counts(rows)
    p = float(counts['positives'])
    n = float(counts['negatives'])
    #print(p,n)
    if p == 0 or n == 0:
        return 0;
    else:
        return p*n/(p+n)**2
    
def gain_v(left,right,current_varimp):
    """Information Gain.
    The entropy of the starting node, 
    minus the weight entropy of two child nodes
    """
    p = float(len(left))/(len(left)+len(right))
    return current_varimp - p *varimp(left) - (1-p) * varimp(right)


#high,normal = partition(training_data,0)
#print(gain(high, normal,entropy(training_data)))

def find_best_att_entropy(rows):
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
        g = gain_e(true_rows,false_rows,current_entropy)
        if g >= best_gain:
            best_gain = g
            best_attribute = att
    return best_gain, best_attribute

#g,att = find_best_att_entropy(training_data)
#print(g,attribute_names[att])

def find_best_att_varimp(rows):
    """Look for the best attriute
    """
    best_gain = 0
    best_attribute = -1000
    current_varimp = varimp(rows)
    n_features = len(rows[0])-1
    for att in range(n_features):
        true_rows, false_rows = partition(rows, att)
        if len(true_rows) == 0 or len(false_rows)==0:
            continue # This avoid division by 0
        g = gain_v(true_rows,false_rows,current_varimp)
        if g >= best_gain:
            best_gain = g
            best_attribute = att
    return best_gain, best_attribute




class Leaf_stats(object):
    """
    """
    def __init__(self, prediction):
        self.prediction = prediction

class Leaf(object):
    """
    """
    def __init__(self,rows):
        self.stats = class_counts(rows)
        self.p = self.stats['positives']
        self.n = self.stats['negatives']
        self.prediction = 1 if (self.p > self.n ) else 0


class Decision_Node:
    """
    """
    def __init__(self,attribute, true_branch, false_branch, oracle):
        self.attribute = attribute
        self.true_branch = true_branch
        self.false_branch = false_branch
        global current_node_id
        current_node_id += 1
        self.node_id = current_node_id
        #The next is similar to prediction , but other name (oracle) is used because guessing
        self.oracle = oracle
        self.pruned = False
        
    def prune_myself(self):
        self.pruned = True
        

def join_lists(a,b):
    """Takes 2 lists of the same number of columns and returns concatenations of them
    """
    result = []
    for row in a:
        result.append(row)
    for row in b:
        result.append(row)
    return result
        
def build_tree_entropy(rows):
    """
    """
    stats = class_counts(rows)
    p = stats['positives']
    n = stats['negatives']
    prediction = 1 if (p > n) else 0

    g, att = find_best_att_entropy(rows)
    if g == 0:
        return Leaf_stats(prediction)
    true_rows, false_rows = partition(rows,att)
    
    true_branch = build_tree_entropy(true_rows)
    false_branch= build_tree_entropy(false_rows)
    
    return Decision_Node(att, true_branch, false_branch, prediction)

def build_tree_varimp(rows):
    """
    """
    #global current_node_id
    #current_node_id += 1
    stats = class_counts(rows)
    p = stats['positives']
    n = stats['negatives']
    prediction = 1 if (p > n) else 0

    g, att = find_best_att_varimp(rows)
    if g == 0:
        return Leaf_stats(prediction)
    
    true_rows, false_rows = partition(rows,att)
    
    true_branch = build_tree_varimp(true_rows)
    false_branch= build_tree_varimp(false_rows)
    
    return Decision_Node(att, true_branch, false_branch, prediction)

def print_tree(node, sbl = ""):
    """Prints the tree.
    """
    if isinstance(node.false_branch, Leaf_stats):
        print (sbl + attribute_names[node.attribute] + " = 0 :", node.false_branch.prediction)
        return
    print (sbl + attribute_names[node.attribute] + " = 0 :")
    print_tree(node.false_branch, sbl + "| ")

    if isinstance(node.true_branch, Leaf_stats):
        print (sbl + attribute_names[node.attribute] + " = 1 :", node.true_branch.prediction)
        return
    print (sbl + attribute_names[node.attribute] + " = 1 :")
    print_tree(node.true_branch, sbl + "| ")


def print_tree_node_id(node, sbl = ""):
    """Prints the tree.
    """
    if isinstance(node.false_branch, Leaf_stats):
        print (sbl + attribute_names[node.attribute] + ' ('+str(node.node_id) + ')'+ " = 0 :", node.false_branch.prediction)
        return
    print (sbl + attribute_names[node.attribute] + ' ('+str(node.node_id) + ')'+ " = 0 :")
    print_tree_node_id(node.false_branch, sbl + "| ")

    if isinstance(node.true_branch, Leaf_stats):
        print (sbl + attribute_names[node.attribute] + ' ('+str(node.node_id) + ')'+" = 1 :", node.true_branch.prediction)
        return
    print (sbl + attribute_names[node.attribute] + ' ('+str(node.node_id) + ')'+ " = 1 :")
    print_tree_node_id(node.true_branch, sbl + "| ")

def print_tree2(node, sbl = ""):
    """Prints the tree.
    """
    if isinstance(node, Leaf):
        print (sbl + ":", node.prediction)
        return
    print (sbl + attribute_names[node.attribute] + " = 0 :")
    print_tree(node.false_branch, sbl + "| ")
    print (sbl + attribute_names[node.attribute] + " = 1 :")
    print_tree(node.true_branch, sbl + "| ")

def classify(row, node):
    if isinstance(node, Leaf_stats):
        return node.prediction
    if row[node.attribute] == 1:
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)

def classify_pruned(row, node):
    if isinstance(node, Leaf_stats):
        return node.prediction
    if node.pruned == True:
        return node.oracle
    if row[node.attribute] == 1:
        return classify_pruned(row, node.true_branch)
    else:
        return classify_pruned(row, node.false_branch)


        
def accuracy(testing_data, node):
    """Gets the accuracy of the model
    testing data: set with the same number of columns that the training data
    node: decision tree built beforehand  
    """
    matches = 0 
    for row in testing_data:
        if classify(row, node) == row[-1]:
            matches += 1
    #print(len(testing_data))
    return float(matches)/len(testing_data)

def accuracy_pruned(validation_data, node):
    """Gets the accuracy of the model
    testing data: set with the same number of columns that the training data
    node: decision tree built beforehand  
    """
    matches = 0 
    for row in validation_data:
        if classify_pruned(row, node) == row[-1]:
            matches += 1
    #print(len(testing_data))
    return float(matches)/len(testing_data)

"""-------------------------- PRUNING FUNCTIONS----------------------------"""

def count_non_leaf(node):
    if isinstance(node, Leaf_stats):
        return 0
    else:
        return 1 + count_non_leaf(node.true_branch) + count_non_leaf(node.false_branch)

def count_all_nodes(node):
    if isinstance(node, Leaf_stats):
        return 1
    else:
        return 1+count_all_nodes(node.true_branch) + count_all_nodes(node.false_branch)

def restart_and_order(node):
    global x
    x=0
    return order(node)

def order(node):
    global x
    if isinstance(node, Leaf_stats):
        return
    order (node.true_branch)
    order (node.false_branch)
    x += 1
    node.node_id = x
    return


def restart_and_order_pruned(node):
    global x
    x=0
    return order_pruned(node)

def order_pruned(node):
    global x
    if isinstance(node, Leaf_stats):
        return
    elif node.pruned == True:
        return
    else:
        order_pruned (node.true_branch)
        order_pruned (node.false_branch)
        x += 1
        node.node_id = x
        return







def look_and_replace(node, number):
    if isinstance(node,Leaf_stats):
        return
    elif (node.node_id == number):
        v=node.oracle
        print(attribute_names[node.attribute],v)
        #node = Leaf_stats(v)
    else:
        look_and_replace(node.true_branch,number)
        look_and_replace(node.false_branch,number)
    return v

"""def look_node(node,number):
    if node.node_id == number:
        return node
    if ! isinstance(node.true_branch,Leaf_stats):
        look_node(node.true_branch,number)
    if ! isinstance(node.false_branch,Leaf_stats):
        look_node(node.false_branch, number)

del look_v2(node,number):
    if(node.true_branch. == )
    
    
"""

def search(start,n):
    if((not start) or (start.node_id==n)):
        ans = start
        print("EQUAL!")
        return ans
    else:
        print("found",start.node_id)
        ans= search(start.true_branch,n)
        if not (ans):
            ans= search(start.false_branch,n)
        return ans  

def search2(start,n):
    if( (start.node_id==n)):
        ans = start

        return ans
    else:
    
        ans= search2(start.true_branch,n)
        if not (ans):
            ans= search2(start.false_branch,n)
        return ans 
    

def prune_helper(root,nodelist):
    if isinstance(root, Leaf_stats):
        return
    if root.pruned == True:
        return
        #nodelist.append(root)
    prune_helper(root.true_branch,nodelist)
    prune_helper(root.false_branch,nodelist)
    nodelist.append(root)


def post_pruning_entropy(node,L,K):
    D = build_tree_entropy(training_data)
    Dbest = D
    for i in range(L):
        #build a copy of the original tree to prune
        Dprime = build_tree_entropy(training_data)
        M = randint(1,K)
        for j in range(M):
            restart_and_order_pruned(Dprime)
            node_list = []
            prune_helper(Dprime,node_list)
            N = len(node_list)
            if N <= 1 :
                break
            P = randint(1,N)
            node_list[P-1].prune_myself()
        accuracy_Dprime = accuracy_pruned(validation_data,Dprime)
        accuracy_Dbest = accuracy_pruned(validation_data,Dbest)
        if (accuracy_Dprime > accuracy_Dbest):
            Dbest = Dprime
    return Dbest
            
# Remember this is a prunned tree so workdd with accuracy_pruned            





    

"""---------------- Running the fucions-------------------"""

current_node_id = 0
my_tree_entropy = build_tree_entropy(training_data)
print_tree_node_id(my_tree_entropy)
print("\nThe accuracy with entropy is:")
print(accuracy(training_data, my_tree_entropy))
print("Number of non leaf nodes: ", count_non_leaf(my_tree_entropy))
print("Number of nodes in total: ", count_all_nodes(my_tree_entropy))

#current_node_id = 0
#my_tree_varimp = build_tree_varimp(training_data)
#current_node_id = 0
#my_tree_varimp2 = build_tree_varimp(training_data)
#print_tree(my_tree_varimp)
#print("\nThe accuracy with variance impurity is:")
#print(accuracy(training_data, my_tree_varimp))
#print("Number of non leaf nodes: ", count_non_leaf(my_tree_varimp))
#print("Number ofnodes in total: ", count_all_nodes(my_tree_varimp))
#print("Number of non leaf nodes: ", count_non_leaf(my_tree_varimp2))
#print("Number ofnodes in total: ", count_all_nodes(my_tree_varimp2))

#lista1 = []
#prune_helper(my_tree_entropy, lista1)
#print_tree_node_id(lista1[136-1])
#leaf_prueba = Leaf_stats(lista1[136-1].oracle)
#lista1[136-1].prune_myself()

#restart_and_order_pruned(my_tree_entropy)
#lista1[23-1].prune_myself()

#restart_and_order_pruned(my_tree_entropy)
#print(accuracy_pruned(validation_data,my_tree_entropy))
print(accuracy(testing_data,my_tree_entropy))
print(accuracy(validation_data,my_tree_entropy))
#lista2 = []
#prune_helper(my_tree_entropy, lista2)

pruned_tree = post_pruning_entropy(my_tree_entropy,10,15)
print(accuracy_pruned(testing_data,pruned_tree))
print(accuracy_pruned(validation_data,pruned_tree))
