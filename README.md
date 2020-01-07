    
# Decision Trees Heuristics and Pruning
We can define a decision tree as a computational tree where each node contains a question about an attribute, each branch of the node contains an answer to this question. Which question/attribute should be placed in each node is determined by the decision tree learning algorithm.
As stated in Mitchel, most algorithms that have been developed for learning decision trees are variations on a core algorithm that employs a top-down, greedy search through the space of possible decision trees.

## When are decision trees suitable?
- For supervised learning: The algorithm needs labeled data is available
- For classification: The target has discrete values
- When we have noisy data: The training data might contain errors

## Algorithm:
```
ID3 (Examples, Target_Attribute, Attributes)
    Create a root node for the tree
    If all examples are positive, Return the single-node tree Root, with label = +.
    If all examples are negative, Return the single-node tree Root, with label = -.
    If number of predicting attributes is empty, then Return the single node tree Root, with label = most common value of the target attribute in the examples.
    Otherwise Begin
        A ← The Attribute that "best" classifies examples.
        Decision Tree attribute for Root = A.
        For each possible value, vi, of A,
            Add a new tree branch below Root, corresponding to the test A = vi.
            Let Examples(vi) be the subset of examples that have the value vi for A
            If Examples(vi) is empty
                Then below this new branch add a leaf node with label = most common target value in the examples
            Else below this new branch add the subtree ID3 (Examples(vi), Target_Attribute, Attributes – {A})
    End
    Return Root
```

## Our Data

- Possible values of the target: 0, 1
- Possible values of attributes: 0, 1
- Number of attributes: (number of columns in the .csv file) - 1
- Target location: last column in the .csv file
- We assume that we have a dataset splited in :
	- training data
	- validation data
	- testig data

## Our Tree
Naturally the learning algorithm for the decision tree will be implmented using recursion


## 1. Heuristics in a Decision Tree
How do we decide which attribute should be tested at each node in the tree? Heuritics are quantitative measurements on how useful would be an attribute to split data acccorfing to it (classification).

Here we analize the two heuristics: information gain and variance impurity.

### 1.1 Information Gain Heuristic
Lets define Entropy of the set of samples S as a measurement of the homogeneity of the samples in binary data.

Entropy(S) = -pp * log<sub>2</sub>(pp) - pn * log<sub>2</sub>(pn)

Where:
* pn :(# negative samples)/(# total of samples)
* pp :(# positive samples)/(# total of samples)
The Information Gain is the defined by the following equation:

![eq_info_gain](/images/infogain_eq.png)

Where:
* A : attribute
* S<sub>v</sub> : subset of S for which attribute A has value v

### 1.2 Variance Impurity Heuristic
The variance impurity of the training set S is defined as:

![eq_VI](/images/vi_eq.png) 

Where:
* K : the number of examples in the training set
* K<sub>0</sub> : the number of training examples that have class = 0
* K<sub>1</sub> : the number of training examples that have class = 1

The gain for this impurity is defined as

![eq_VI_heuristic](/images/vi_gain_eq.png)

Where:
X : attribute
S<sub>x</sub> : set of training examples that have X = x
Pr(x) : fraction of the training examples that have X = x

## 2. Regularization with Prunnig
Prunning is a method to regularize (reduce overfitting) a deciion tree. As a result the model will generalize better.
The algorith will try to improve the accuracy of the tree "L" times, prunning M nodes. Where M is a random between 1 and K. We have to provide the L and K values to the algorithm 

## 3. Printing a Decision tree
The implementation is recursive because of the nature of the problem. 
## 4. How to run the program
Clone the repository
```sh
$ python tree.py 4 10 training_set.csv validation_set.csv test_set.csv yes
```

## Acknowlegments:
* Tom Mitchell (Chapter 3)
* Vibhav Gogate's [Advanced Machine Learning Course](https://www.hlt.utdallas.edu/~vgogate/ml/2018s/resources.html)
* https://github.com/random-forests/tutorials/blob/master/decision_tree.ipynb
