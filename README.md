    
# Decision Trees Heuristics and Prunning
## 1. Heuristics in a Decision Tree
How do we decide which attribute should be tested at each node in the tree? Heuritics are quantitative measurements on how useful is an attribute for classification.

### 1.1 Information Gain Heuristic
Lets define Entropy, a measurement of the homogeneity of the samples in binary data:

Entropy(S) = -pp * log<sub>2</sub>(pp) - pn * log<sub>2</sub>(pn)

Where:
* pn :(# negative samples)/(# total of samples)
* pp :(# positive samples)/(# total of samples)
The 
![eq_info_gain](/images/infogain_eq.png)
### 1.2 Variance Impurity Heuristic
lalall
![eq_VI](/images/vi_eq.png) 
lalala
![eq_VI_heuristic](/images/vi_gain_eq.png)
## Regularization with Prunnig
Prunning is a method to regularize a deciion tree, therefore avoid overfitting. As a result the model will generalize better

## Printing a Decision tree

## Key points
* The implementation is recursive because of the nature of the problem. 

## Acknowlegments:
* Tom Mitchell (Chapter 3)
* Vibhav Gogate's [Advanced Machine Learning Course] (https://www.hlt.utdallas.edu/~vgogate/ml/2018s/resources.html)
