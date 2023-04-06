# Mask AutoEncoder



ViT crop img into many 16x16 patches 

MAE - Self-supervision

![image-20220611174048565](https://ik.imagekit.io/haochen/Typora/image-20220611174048565.png)

快 - Efficient

大 - Scalable

Auto模型 意思是 y和x 是同一个东西

Title： What is What， 什么是一个好同志 (客观)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220611174723140.png" alt="image-20220611174723140" style="zoom:33%;" />

位置编码？ Position， 

Bert 扩展到 MAE

![image-20220611175124014](https://ik.imagekit.io/haochen/Typora/image-20220611175124014.png)

![image-20220611175145768](https://ik.imagekit.io/haochen/Typora/image-20220611175145768.png)



Patch 并不是一个独立的单元，和语言不一样。



### 对社区的影响

![image-20220611175224282](https://ik.imagekit.io/haochen/Typora/image-20220611175224282.png)

落后于NLP

![image-20220611175325488](https://ik.imagekit.io/haochen/Typora/image-20220611175325488.png)





卷积 平滑 汇聚信息和识别， 不好加mask..

NLP中是一个词，卷积无法区分边界，在后面还原不出。

但是卷积是自带位置信息的。。

信息密度不一样 (完形填空)， 但是img中是可能的。

MAE把块去掉，这样信息就不是那么冗余，因此创造了一个很难的任务。

怎么不被 插值影响

并不能插值，而是学一个全局的信息

做成一个词进去 （Mask Token ）



计算开销， 快一点



结论写为什么要把算法设计成这个样子讲清楚

为什么要这么做



![image-20220611180114990](https://ik.imagekit.io/haochen/Typora/image-20220611180114990.png)



带掩码

<img src="https://ik.imagekit.io/haochen/Typora/image-20220611180153259.png" alt="image-20220611180153259" style="zoom:30%;" />

IGPT和BeIT



<img src="https://ik.imagekit.io/haochen/Typora/image-20220611180206347.png" alt="image-20220611180206347" style="zoom:33%;" />



特别相关的工作，不一样的地方写出来

<img src="https://ik.imagekit.io/haochen/Typora/image-20220611180257894.png" alt="image-20220611180257894" style="zoom:33%;" />

### 怎样reconstruct

<img src="https://ik.imagekit.io/haochen/Typora/image-20220611180553679.png" alt="image-20220611180553679" style="zoom:33%;" />

没被盖住的就不做损失了

shuffle and unshuffle



Strong Reg 