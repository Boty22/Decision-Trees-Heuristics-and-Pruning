    
# Decision Trees Heuristics and Prunning
## 1. Heuristics in a Decision Tree
How do we decide which attribute should be tested at each node in the tree? Heuritics are quantitative measurements on how useful would be an attribute to split data acccorfing to it (classification).

Here we analize the two heuristics: information gain and variance impurity.

### 1.1 Information Gain Heuristic
Lets define Entropy of the set of samples S as a measurement of the homogeneity of the samples in binary data.

Entropy(S) = -pp * log<sub>2</sub>(pp) - pn * log<sub>2</sub>(pn)
is the
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
