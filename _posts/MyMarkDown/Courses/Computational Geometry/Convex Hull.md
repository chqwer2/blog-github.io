The link of OJ is http://dsa.cs.tsinghua.edu.cn/oj/

MIT OCW https://ocw.mit.edu/courses/2-158j-computational-geometry-spring-2003/

# **计算几何 | Computational Geometry**

## Convex Hull

**What is a convex combination**

<img src="../../../../img/Typora/Convex Hull/image-20230102145608561.png" alt="image-20230102145608561" style="zoom:30%;" />

### Extremity

如何构造凸包

<img src="../../../../img/Typora/Convex Hull/image-20230102150827177.png" alt="image-20230102150827177" style="zoom:50%;" />

如何确定极点

1. 判断每个点是否在任何三角形的内部， 但是$O(n^4)$ 

### To-left Test

3条有向直线

<img src="../../../../img/Typora/Convex Hull/image-20230102152525449.png" alt="image-20230102152525449" style="zoom: 50%;" />

问题是如何高效的处理？

<img src="../../../../img/Typora/Convex Hull/image-20230102152809580.png" alt="image-20230102152809580" style="zoom:50%;" />

### Extreme Edges (EE)

如何判断极边

所有的其他点都在 左侧

比极点快一个量级 $O(n^3)$

### Decrease and Conquer

新引入新的点，加入已有集合

Incremental Construction for generating convex hull

#### In-Convex-Polygon Test

二分法 $O(log_n)$

<img src="../../../../img/Typora/Convex Hull/image-20230102154524196.png" alt="image-20230102154524196" style="zoom:50%;" />

但是不能行的通，因为多边形一直在变，预处理是没有效力的

全遍历边$O(n^2)$

#### Support Line

### Selection Sorting and Jarvis March

<img src="../../../../img/Typora/Convex Hull/image-20230103093523014.png" alt="image-20230103093523014" style="zoom:35%;" />

#### Coherence

<img src="../../../../img/Typora/Convex Hull/image-20230103094302190.png" alt="image-20230103094302190" style="zoom:50%;" />

拐角最小的边就是EP, 但是太慢了

所以用To-left Test, 回避除法和函数运算

排序任务的特例，点在右边即更新

#### Degeneracy - 有平局情况，存在歧义

##### lowest-then-leftmost (LTL)

Output Sensitivity: GW Algo $O(nh)$

### Lower Bound

#### Reduction

![image-20230104091949963](../../../../img/Typora/Convex Hull/image-20230104091949963.png)

曹聪称象

$|A|$表达$A$问题的难度

Convex Hull is $O(nlog_n)$

Proof Case: **Sorting $\leq_N$ 2d-CH**, 即决定下界

![image-20230104093356173](../../../../img/Typora/Convex Hull/image-20230104093356173.png)

点在x轴上单调，即可以转换为排序问题

### Graham Scan - optimized algo

$O(nlog_n)$

1. Pre-sorting (To-left test)

   <img src="../../../../img/Typora/Convex Hull/image-20230104171748708.png" alt="image-20230104171748708" style="zoom:60%;" />

   OR

   <img src="../../../../img/Typora/Convex Hull/image-20230105093526248.png" alt="image-20230105093526248" style="zoom:33%;" />

   **How to pre-sorting?**

   To-left Test comparator (Polar Angle Order)

   If the array is already sorted in other way? 

   <img src="../../../../img/Typora/Convex Hull/image-20230105095454562.png" alt="image-20230105095454562" style="zoom:50%;" />

   以负无穷远为边界，即可以视为Polar Angle Order，Graham可以为上凸包。反之。

   

   

   

   

   

2. Two Stack: S and T

<img src="../../../../img/Typora/Convex Hull/image-20230105090843594.png" alt="image-20230105090843594" style="zoom:70%;" />

T 会耗尽， S 只包含了凸包的顶点，且是逆时针的

<img src="../../../../img/Typora/Convex Hull/image-20230105092009213.png" alt="image-20230105092009213" style="zoom:70%;" />

3-4-5 is right turn, pop out 4, push in 5.

make sure every thing is left-turn

###  Proof  Graham的上界紧密性

<img src="../../../../img/Typora/Convex Hull/image-20230105094125399.png" alt="image-20230105094125399" style="zoom:50%;" />

图论：According to Euler's formula, Vertices+Faces-Edges=2,

Amortization: 

![image-20230105094822235](../../../../img/Typora/Convex Hull/image-20230105094822235.png)



