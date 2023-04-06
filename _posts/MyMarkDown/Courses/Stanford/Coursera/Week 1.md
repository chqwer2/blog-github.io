Supervised seen most rapid advancement





<img src="https://ik.imagekit.io/haochen/Typora/image-20220616212140172.png" alt="image-20220616212140172" style="zoom:33%;" />



![image-20220616212851399](https://ik.imagekit.io/haochen/Typora/image-20220616212851399.png)

### Visualization Example

![image-20220617164530660](https://ik.imagekit.io/haochen/Typora/image-20220617164530660.png)



Apply more relevant feature can reduce overfitting

### Gradient Descent

![image-20220618104212423](https://ik.imagekit.io/haochen/Typora/image-20220618104212423.png)

### Some Visualization

https://www.coursera.org/learn/advanced-learning-algorithms/ungradedLab/reSfw/coffee-roasting-in-tensorflow

![image-20220618181621653](https://ik.imagekit.io/haochen/Typora/image-20220618181621653.png)

![image-20220618181629995](https://ik.imagekit.io/haochen/Typora/image-20220618181629995.png)

![image-20220618181636507](https://ik.imagekit.io/haochen/Typora/image-20220618181636507.png)

lab_coffee_utils.py

# Is there a path to AGI? (General)

Ever since I was a teenager 

starting to play around with neural networks, 

I just felt that the dream of maybe 

someday building an AI system 

that's as intelligent as myself 

or as intelligent as a typical human, 

that that was one of the most inspiring dreams of AI. 

I still hold that dream alive today. 

But I think that the path to get there is 

not clear and could be very difficult. 

I don't know whether it would take us mere 

decades and whether we'll 

see breakthroughs within our lifetimes, 





# Why do we need activation functions?

Not learning any more complex than linear model.



```
loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
```

![image-20220619102816016](https://ik.imagekit.io/haochen/Typora/image-20220619102816016.png)





# Diagnosing bias and variance

Help you decide what to try next.

![image-20220619103244681](https://ik.imagekit.io/haochen/Typora/image-20220619103244681.png)







![image-20220619105449419](https://ik.imagekit.io/haochen/Typora/image-20220619105449419.png)





### Decision trees

![image-20220619112051516](https://ik.imagekit.io/haochen/Typora/image-20220619112051516.png)

![image-20220619112200415](https://ik.imagekit.io/haochen/Typora/image-20220619112200415.png)

### Measuring purity

![image-20220619113039743](https://ik.imagekit.io/haochen/Typora/image-20220619113039743.png)

![image-20220619113107058](https://ik.imagekit.io/haochen/Typora/image-20220619113107058.png)

### Choosing a split: Information Gain

We need to combine these two numbers into one single number

![image-20220619113609003](https://ik.imagekit.io/haochen/Typora/image-20220619113609003.png)

But here we reduction in entropy like below to obtain **Info gain**:

![image-20220619113724317](https://ik.imagekit.io/haochen/Typora/image-20220619113724317.png)

![image-20220619113940937](https://ik.imagekit.io/haochen/Typora/image-20220619113940937.png)





### Tree Ensemble

One single decision tree can be sensitive to some changes in data

![image-20220619150339422](https://ik.imagekit.io/haochen/Typora/image-20220619150339422.png)

With sampling with replacement, we can build new training set for trees



### Random forest algorithm

B too larger will be computationally significant w/o meaningfully increase the performance

**Random choose $k$ features**

![image-20220619151056544](https://ik.imagekit.io/haochen/Typora/image-20220619151056544.png)



### XGBoost

an album called XGBoost

When doing second time through the loop, instead picking all samples with same probability, 

we are more like picking the sample the previous tree misclassified or do poor on.



That’s similar idea called: **deliberate practice**



### When to use decision trees

tabular data or structural data



![image-20220619152457506](https://ik.imagekit.io/haochen/Typora/image-20220619152457506.png)



![image-20220619152845023](https://ik.imagekit.io/haochen/Typora/image-20220619152845023.png)



