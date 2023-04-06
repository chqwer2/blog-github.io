# Linear Regression

![image-20220610093511350](https://ik.imagekit.io/haochen/Typora/image-20220610093511350.png)



### Empirical Risk

So typically, these objectives are called empirical risk. Or loss function.

**Hinge Loss**

![image-20220610093752477](https://ik.imagekit.io/haochen/Typora/image-20220610093752477.png)



**Geometrically Identifying Error**

Structural error: None linear

Estimation error: Not enough data.



### **Error decomposition and the bias-variance trade-off**

![image-20220610094521192](https://ik.imagekit.io/haochen/Typora/image-20220610094521192.png)

![image-20220610094543711](https://ik.imagekit.io/haochen/Typora/image-20220610094543711.png)

you will see how regularization can be used to restrict the complexity  for linear regression so that we will be able to search for a sweet spot where the total error from variance and bias is the minimum. 

### Closed Form Solution

you can not do closed form solution.

But it happened to be because our loss function,

our empirical risk is actually happened

to be convex function, that's why we can actually solve it

### Motivation for Regularization

**Ridge Regression**

![image-20220610095442343](https://ik.imagekit.io/haochen/Typora/image-20220610095442343.png)

![image-20220610095650146](https://ik.imagekit.io/haochen/Typora/image-20220610095650146.png)

### **Equivalance of regularization to a Gaussian Prior on Weights**

![image-20220610095900916](https://ik.imagekit.io/haochen/Typora/image-20220610095900916.png)

![image-20220610095914002](https://ik.imagekit.io/haochen/Typora/image-20220610095914002.png)

# Nonlinear Classification

<img src="https://ik.imagekit.io/haochen/Typora/image-20220610100321314.png" alt="image-20220610100321314" style="zoom:33%;" />

Expanding feature maps into very high dimensional ones

carries a computational disadvantage.

And we'll show how you can avoid that

by using something called kernel functions.

And we will then generalize our linear methods

### Feature Coordinate

<img src="https://ik.imagekit.io/haochen/Typora/image-20220610100708516.png" alt="image-20220610100708516" style="zoom:33%;" />

Map x into a feature vector $\phi(x)$

coordinates lie on this little parabola (抛物线).

<img src="https://ik.imagekit.io/haochen/Typora/image-20220610100901428.png" alt="image-20220610100901428" style="zoom:50%;" />

All the examples, as they are mapped to feature coordinates,

they now include more information

about x that's more explicitly linearly accessible.



So this, as an estimate, would correctly

classify those examples now in the higher dimensional feature



### Non-Linear (Polynomial)

$x^2, x^2,\cdots$

<img src="https://ik.imagekit.io/haochen/Typora/image-20220610121039758.png" alt="image-20220610121039758" style="zoom:30%;" />

**How to select $k$ unique things**

![image-20220610124749527](https://ik.imagekit.io/haochen/Typora/image-20220610124749527.png)

![image-20220610124727765](https://ik.imagekit.io/haochen/Typora/image-20220610124727765.png)

### Motivation for Kernels: Computational Efficiency

The idea is that you can take inner products

between high dimensional feature vectors

and evaluate that inner product very cheaply.



If I have two feature vectors here,

corresponding to two different examples-- x and x prime

<img src="https://ik.imagekit.io/haochen/Typora/image-20220610125830509.png" alt="image-20220610125830509" style="zoom:50%;" />

And what we saw here is that sometimes, depending

on the feature transformation, the kernel

can be evaluated very cheaply, even though we

would have to explicitly construct

very high dimensional feature vectors.

![image-20220610130231572](https://ik.imagekit.io/haochen/Typora/image-20220610130231572.png)



### Kernel Perceptron

![](https://ik.imagekit.io/haochen/Typora/image-20220610155636617.png)

Do need the origin theta, but a $\alpha$ to capture how many times we make mistakes 



![image-20220610155645721](https://ik.imagekit.io/haochen/Typora/image-20220610155645721.png)

![image-20220610160510980](https://ik.imagekit.io/haochen/Typora/image-20220610160510980.png)



we take an inner product with each of the training examples

and that new example x i.

![image-20220610161159929](https://ik.imagekit.io/haochen/Typora/image-20220610161159929.png)

So you can think of the kernel function

here as a kind of similarity measure.

How similar the j-th example is to the i-th example.

So our predicted value here is now

how important the j-th example is.

##### How is updated now

![image-20220610161759148](https://ik.imagekit.io/haochen/Typora/image-20220610161759148.png)

### Kernel Composition Rules

![image-20220610163241787](https://ik.imagekit.io/haochen/Typora/image-20220610163241787.png)

![image-20220610164758751](https://ik.imagekit.io/haochen/Typora/image-20220610164758751.png)

### Other: Random Forest

Decision tree

![image-20220610165128091](https://ik.imagekit.io/haochen/Typora/image-20220610165128091.png)

### Recommender System

<img src="https://ik.imagekit.io/haochen/Typora/image-20220610165625613.png" alt="image-20220610165625613" style="zoom:50%;" />

Is very Sparse matrix

We want to fill out the matrix

But we don’t have huge feature vector



##### Why Not Regression?

Not full feature vector.



### K-Nearest Neighbor Method

I am going to go now through all the users b

which are my K nearest neighbors of me--

of user a-- who did watch movie i.

**How to define similarity:** Consine, Euclidean Distance

![image-20220610171324424](https://ik.imagekit.io/haochen/Typora/image-20220610171324424.png)

 

But this doesn’t count the data structure.

### Collaborative Filtering: the Naive Approach

The goal is to build another matrix.

![image-20220610173702929](https://ik.imagekit.io/haochen/Typora/image-20220610173702929.png)



But for everything you don’t know, you put $x_i=0$.

Clearly, it just corrupt the $y_i$, it must be wrong somewhere.



And the **answer** comes from the fact that what I've done here--

and you remember when I start taking the derivatives--

I told you we are going to take it for each entry

independently.



And it is not surprising that since we're not

modeling dependency in any way, we're

really losing important connection

### Collaborative Filtering with Matrix Factorization

So what you remember from linear algebra,

that, intuitively speaking, **rank** captures how much dependency

do you see between the entries of the matrix.



**Make very strong assumption that the preference of users are related**

Rank = 1

<img src="https://ik.imagekit.io/haochen/Typora/image-20220611091452077.png" alt="image-20220611091452077" style="zoom:50%;" />

But it must oversimplify the problem: we only use one number to mark users and movies

So we can use for higher rank matrix…. for better representation

![image-20220611091948865](https://ik.imagekit.io/haochen/Typora/image-20220611091948865.png)



### Alternating Minimization

![image-20220611092537295](https://ik.imagekit.io/haochen/Typora/image-20220611092537295.png)

If rank = 1, the U and V will be reduced to a vectors $u$ and $v$.



![image-20220611093443516](https://ik.imagekit.io/haochen/Typora/image-20220611093443516.png)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220611094233519.png" alt="image-20220611094233519" style="zoom:50%;" />

### Python

![image-20220615095025017](https://ik.imagekit.io/haochen/Typora/image-20220615095025017.png)

### SVM

![image-20220615095604047](https://ik.imagekit.io/haochen/Typora/image-20220615095604047.png)

The C parameter **tells the SVM optimization how much you want to avoid misclassifying each training example**. For large values of C, the optimization will choose a smaller-margin  hyperplane if that hyperplane does a better job of getting all the  training points classified correctly.

### Softmax

![image-20220615100356342](https://ik.imagekit.io/haochen/Typora/image-20220615100356342.png)

![image-20220615100416237](https://ik.imagekit.io/haochen/Typora/image-20220615100416237.png)

![image-20220615101033091](https://ik.imagekit.io/haochen/Typora/image-20220615101033091.png)



![image-20220615100705098](https://ik.imagekit.io/haochen/Typora/image-20220615100705098.png)

remember to clip

 temp = np.clip(compute_probabilities(X,  theta, temp_parameter),1e-15, 1-1e-15)

### Gradient Descent

![image-20220615102858077](https://ik.imagekit.io/haochen/Typora/image-20220615102858077.png)

Write a function `run_gradient_descent_iteration` that runs one step of the gradient descent algorithm. 

**Available Functions:**  You have access to the NumPy python library as `np`, `compute_probabilities` which you previously implemented and `scipy.sparse` as `sparse`. 

You should use [`sparse.coo_matrix`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_matrix.html#scipy.sparse.coo_matrix) so that your function can handle larger matrices efficiently (and not  time out for the online graders). The sparse matrix representation can  handle sparse matrices efficiently. 



Explain how the temperature parameter affects the probability of a sample x(i) 
        being assigned a label that has a large θ. What about a small θ?
Smaller temperature leads to less variance



np.mod(x, 3)

mod(x1/x2)

@ is matmul?

![image-20220615111437303](https://ik.imagekit.io/haochen/Typora/image-20220615111437303.png)

### Cube Feature

will perform better than pca feature

https://github.com/Machine-Learning-Course-ITM/Project-2-Classifiers/blob/master/features.py

![image-20220615115717606](https://ik.imagekit.io/haochen/Typora/image-20220615115717606.png)

### RBF, Poly kernel

*Radial Basis Function* (*RBF*) *kernel* 

https://github.com/Machine-Learning-Course-ITM/Project-2-Classifiers/blob/master/kernel.py#L62

 Compute the Gaussian RBF kernel between two matrices X and Y::
            K(x, y) = exp(-gamma ||x-y||^2)
        for each pair of rows x in X and y in Y.
