# Environmental Data and Gaussian Processes

### Modelling Flow Data

##### Flow Field

<img src="https://ik.imagekit.io/haochen/Typora/image-20220802101309998.png" alt="image-20220802101309998" style="zoom:33%;" />

![image-20220802101521864](https://ik.imagekit.io/haochen/Typora/image-20220802101521864.png)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220802101552424.png" alt="image-20220802101552424" style="zoom:33%;" />

![image-20220802101653125](https://ik.imagekit.io/haochen/Typora/image-20220802101653125.png)

##### Local Correlation

![image-20220802102353963](https://ik.imagekit.io/haochen/Typora/image-20220802102353963.png)

##### Normal Distribution

![image-20220802102450351](https://ik.imagekit.io/haochen/Typora/image-20220802102450351.png)

![image-20220802104913866](https://ik.imagekit.io/haochen/Typora/image-20220802104913866.png)



What is positive semi-definite？

### Conditional Probability 

![image-20220802113015960](https://ik.imagekit.io/haochen/Typora/image-20220802113015960.png)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220802113435083.png" alt="image-20220802113435083" style="zoom:50%;" />

### Conditional Distribution of Multivariate Gaussian Random Variables

![image-20220802113607066](https://ik.imagekit.io/haochen/Typora/image-20220802113607066.png)

![image-20220802113636910](https://ik.imagekit.io/haochen/Typora/image-20220802113636910.png)

![img](https://ik.imagekit.io/haochen/Typora/images_conditional.svg)

How to understand Covariance

![image-20220802114221934](https://ik.imagekit.io/haochen/Typora/image-20220802114221934.png)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220802114316287.png" alt="image-20220802114316287" style="zoom: 45%;" />

### Uncertainty

![image-20220802115139221](https://ik.imagekit.io/haochen/Typora/image-20220802115139221.png)

### The Role of the Covariance Kernel

So first, why would we even want to use a kernel function

and not just define some fixed covariance?

<img src="https://ik.imagekit.io/haochen/Typora/image-20220802115940169.png" alt="image-20220802115940169" style="zoom:43%;" />

for this exponential or RBF kernel, Radial Basis Function



So basically the flexibility is that now I

can take any collection of xi to however many I want, xn,

and get a Gaussian distribution of the measurements

on these locations or over the labels on these locations.



### Gaussian Process

![image-20220802120154276](https://ik.imagekit.io/haochen/Typora/image-20220802120154276.png)

![image-20220802120253732](https://ik.imagekit.io/haochen/Typora/image-20220802120253732.png)

![image-20220802120349407](https://ik.imagekit.io/haochen/Typora/image-20220802120349407.png)

### isotropic kernel functions. 

![image-20220802120435682](https://ik.imagekit.io/haochen/Typora/image-20220802120435682-9518788.png)

### Effects of Parameters on Kernel Functions

![image-20220803101939654](https://ik.imagekit.io/haochen/Typora/image-20220803101939654.png)

![image-20220803102203788](https://ik.imagekit.io/haochen/Typora/image-20220803102203788.png)

![image-20220803102442514](https://ik.imagekit.io/haochen/Typora/image-20220803102442514.png)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220803102455274.png" alt="image-20220803102455274" style="zoom:200%;" />



### The Effects of Measurement Noise

Thus far, we have assumed that the kernel is the only contribution to  the covariance matrix of the data. Although is was not stated  explicitly, this means we took the data, or the observations, as exact. 



![image-20220803102955868](https://ik.imagekit.io/haochen/Typora/image-20220803102955868.png)

![img](https://ik.imagekit.io/haochen/Typora/images_taus.png)

## **How to select this kernel function**

One could create a countable number of models, such as Gaussian  processes with different kernels, or use the same kernel with a set of  different parameters. However, from these sets of kernels, how do we  specify and select **which model for the kernel is best**? 

![image-20220803103440475](https://ik.imagekit.io/haochen/Typora/image-20220803103440475.png)

![image-20220803103524552](https://ik.imagekit.io/haochen/Typora/image-20220803103524552.png)

![image-20220803103538448](https://ik.imagekit.io/haochen/Typora/image-20220803103538448.png)

![image-20220803104522667](https://ik.imagekit.io/haochen/Typora/image-20220803104522667.png)

![image-20220803110845136](https://ik.imagekit.io/haochen/Typora/image-20220803110845136.png)

### Graph

multiplicity of the maximum degree? That is: how many nodes share this maximum degree? 

# Beyond Linear Dependencies

### Mutual Information

![image-20220803112008317](https://ik.imagekit.io/haochen/Typora/image-20220803112008317.png)

![image-20220803112109546](https://ik.imagekit.io/haochen/Typora/image-20220803112109546.png)

![image-20220803112440767](https://ik.imagekit.io/haochen/Typora/image-20220803112440767.png)

### Mutual Infomation

![image-20220803112503391](https://ik.imagekit.io/haochen/Typora/image-20220803112503391.png)

![image-20220803112934132](https://ik.imagekit.io/haochen/Typora/image-20220803112934132.png)

![image-20220803112944977](https://ik.imagekit.io/haochen/Typora/image-20220803112944977.png)

![image-20220803113128158](https://ik.imagekit.io/haochen/Typora/image-20220803113128158.png)

n the two exercises above, we have seen that dependency and correlation  do not imply each other. In order to capture other forms of dependency,  we introduce the concept of **mutual information**. 



![image-20220803113148819](https://ik.imagekit.io/haochen/Typora/image-20220803113148819.png)

![image-20220803113257027](https://ik.imagekit.io/haochen/Typora/image-20220803113257027.png)

![image-20220803114556312](https://ik.imagekit.io/haochen/Typora/image-20220803114556312.png)

The **main idea** with the introduction of mutual information to quantify  non-linear relations among random variables. Thus, following the same  procedure as above, one can define edges in a graph if two nodes have  mutual information higher than some predefined threshold. 

The figure below shows the betweenness centrality for a network that was built based on mutual information between the temperature measurements  on the map. Red values indicate a higher centrality, while blue values  indicate lower centrality in the generated network. One can observe that the zones with high centrality approximately match the zones where  there are some ocean surface currents, as shown in the map. 

### Dipole Discovery

