# Large-scale Opt

![image-20220322091525920](https://ik.imagekit.io/haochen/Typora/image-20220322091525920.png)

![image-20220322091534089](https://ik.imagekit.io/haochen/Typora/image-20220322091534089.png)

What is $\mathbb R_+ $?



![image-20220322092347888](https://ik.imagekit.io/haochen/Typora/image-20220322092347888.png)

![image-20220322092933419](https://ik.imagekit.io/haochen/Typora/image-20220322092933419.png)



**not loss function specified?**

### Classification

Its margin and sign

![image-20220322093314706](https://ik.imagekit.io/haochen/Typora/image-20220322093314706.png)



### Machine Learning and Large-scale Data

![image-20220322093501935](https://ik.imagekit.io/haochen/Typora/image-20220322093501935.png)

### SGD

![image-20220322094131498](https://ik.imagekit.io/haochen/Typora/image-20220322094131498.png)

How to imterprete this formula?

It only effect when $w_t$ is close to $w_{t+1}$, We need a stabilizer

![image-20220322094157114](https://ik.imagekit.io/haochen/Typora/image-20220322094157114.png)

By differentiation in the step 2, the first term is linear

### Iteration Complexity of GD

![image-20220322094921678](https://ik.imagekit.io/haochen/Typora/image-20220322094921678.png)

What is $inf$ Here?

![image-20220322095055547](https://ik.imagekit.io/haochen/Typora/image-20220322095055547.png)

![image-20220322095415361](https://ik.imagekit.io/haochen/Typora/image-20220322095415361.png)

Which will be time consuming to compute the gradient.

![image-20220322095524525](https://ik.imagekit.io/haochen/Typora/image-20220322095524525.png)

![image-20220322095900929](https://ik.imagekit.io/haochen/Typora/image-20220322095900929.png)

The **hinge loss** is used for "maximum-margin" classification.

![image-20220322100427756](https://ik.imagekit.io/haochen/Typora/image-20220322100427756.png)

### Convergence Rate

How fast it converge?

![image-20220322100736801](https://ik.imagekit.io/haochen/Typora/image-20220322100736801.png)



<img src="https://ik.imagekit.io/haochen/Typora/image-20220322101232193.png" alt="image-20220322101232193" style="zoom:50%;" />



### SVGD Stochastic Variance Reduction Gradient

![image-20220322101828969](https://ik.imagekit.io/haochen/Typora/image-20220322101828969.png)

It is a vector, so we use euclidean norm..



![image-20220322102207317](https://ik.imagekit.io/haochen/Typora/image-20220322102207317.png)

$\alpha$ too large..

![image-20220322102940746](https://ik.imagekit.io/haochen/Typora/image-20220322102940746.png)

![image-20220322103158354](https://ik.imagekit.io/haochen/Typora/image-20220322103158354.png)





![image-20220322103447487](https://ik.imagekit.io/haochen/Typora/image-20220322103447487.png)

But we don't know the $w^*$?

is not implementable...



![image-20220322104016801](https://ik.imagekit.io/haochen/Typora/image-20220322104016801.png)

F_s is the gradient, f is the stochatic gradient



![image-20220322104259003](https://ik.imagekit.io/haochen/Typora/image-20220322104259003.png)

The difference between this two methods is we use an estimator (reference point) for $w^*$.

But how to approximate?

![image-20220322104617038](https://ik.imagekit.io/haochen/Typora/image-20220322104617038.png)



does it similiar to use a weight average?

![image-20220322105402054](https://ik.imagekit.io/haochen/Typora/image-20220322105402054.png)

m is iteration per epoch.

How to derive the iteration complexity?







