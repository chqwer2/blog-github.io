# Camera Model

![image-20220728095935070](https://ik.imagekit.io/haochen/Typora/image-20220728095935070.png)

![image-20220728100152245](https://ik.imagekit.io/haochen/Typora/image-20220728100152245.png)

Is the size of the aperture important?

<img src="https://ik.imagekit.io/haochen/Typora/image-20220728100422069.png" alt="image-20220728100422069" style="zoom:30%;" />

Out of Focus

<img src="https://ik.imagekit.io/haochen/Typora/image-20220728100542356.png" alt="image-20220728100542356" style="zoom:40%;" />

#### Radial Distortion

![image-20220728101004876](https://ik.imagekit.io/haochen/Typora/image-20220728101004876.png)

### Geometry

<img src="https://ik.imagekit.io/haochen/Typora/image-20220728101102806.png" alt="image-20220728101102806" style="zoom:33%;" />

Z is non-linear, how to treat it?

![image-20220728102714600](https://ik.imagekit.io/haochen/Typora/image-20220728102714600.png)

If omit Z, it can be linear, but it drops Z.

So we can use **Homogeneous Coordinates**

<img src="https://ik.imagekit.io/haochen/Typora/image-20220728103007051.png" alt="image-20220728103007051" style="zoom:20%;" />

有了齐次坐标后，我放了一个1，这样乘Z后恢复线性，而且Z被保留

对应到唯一的真实坐标。

<img src="https://ik.imagekit.io/haochen/Typora/image-20220728103212076.png" alt="image-20220728103212076" style="zoom:20%;" />

M Matrix 是相机的内参

<img src="https://ik.imagekit.io/haochen/Typora/image-20220728103425431.png" alt="image-20220728103425431" style="zoom:25%;" />

推导一边相机Skewness

![image-20220728103532276](https://ik.imagekit.io/haochen/Typora/image-20220728103532276.png)

![image-20220728103939131](https://ik.imagekit.io/haochen/Typora/image-20220728103939131.png)

### Extrinsic 

2维齐次变换

**Shift**

<img src="https://ik.imagekit.io/haochen/Typora/image-20220728104149736.png" alt="image-20220728104149736" style="zoom:25%;" />

**Rotation**

<img src="https://ik.imagekit.io/haochen/Typora/image-20220728104313265.png" alt="image-20220728104313265" style="zoom:25%;" />

3D Matrix

<img src="https://ik.imagekit.io/haochen/Typora/image-20220728105029045.png" alt="image-20220728105029045" style="zoom:25%;" />

![image-20220728105426995](https://ik.imagekit.io/haochen/Typora/image-20220728105426995.png)

Internal \* External

**w** for World Coordinate

![image-20220728110247628](https://ik.imagekit.io/haochen/Typora/image-20220728110247628.png)

自由度即需要求多少个变量..

<img src="https://ik.imagekit.io/haochen/Typora/image-20220728112050577.png" alt="image-20220728112050577" style="zoom:33%;" />

![image-20220728112125893](https://ik.imagekit.io/haochen/Typora/image-20220728112125893.png)

Can Check

![image-20220728113244530](https://ik.imagekit.io/haochen/Typora/image-20220728113244530.png)



![image-20220729094607458](https://ik.imagekit.io/haochen/Typora/image-20220729094607458.png)

Mathmatics 资源



### Three Types of Rotations

1. **Axis-Angle**

   Orientation in 2D (Axis) is like translation in 1D

   <img src="https://ik.imagekit.io/haochen/Typora/image-20220729173345056.png" alt="image-20220729173345056" style="zoom:20%;" />

   <img src="https://ik.imagekit.io/haochen/Typora/image-20220729173356699.png" alt="image-20220729173356699" style="zoom:25%;" />

   But we need to identify the axis!

2. **Euler**

   <img src="https://ik.imagekit.io/haochen/Typora/image-20220729174037915.png" alt="image-20220729174037915" style="zoom:20%;" />

   But    (a) it will change **axis**, it will no longer aligned with the world axises

   Then (b) it is Gimbal Lock, lost one freedoms

   <img src="https://ik.imagekit.io/haochen/Typora/image-20220729174517735.png" alt="image-20220729174517735" style="zoom:25%;" />

   <img src="https://ik.imagekit.io/haochen/Typora/image-20220729174718472.png" alt="image-20220729174718472" style="zoom:25%;" />

   连乘的时候先内部，Stay local与物体坐标系一致。Lock中间的axis尽量不要转90*k度

   Final (c) the order of rotations

3. Quaternion 四元数

   X= 2*W，旋转两倍

   <img src="https://ik.imagekit.io/haochen/Typora/image-20220729175401993.png" alt="image-20220729175401993" style="zoom:25%;" />

   <img src="https://ik.imagekit.io/haochen/Typora/image-20220729180838443.png" alt="image-20220729180838443" style="zoom:30%;" />

   <img src="https://ik.imagekit.io/haochen/Typora/image-20220729180614713.png" alt="image-20220729180614713" style="zoom:33%;" />

   不然会重合点，意义不一样了。

   But need to be on unit sphere.

   

   x^2 +y^2 +z^2 + w^2 = 1 的超球

   <img src="https://ik.imagekit.io/haochen/Typora/image-20220729181601666.png" alt="image-20220729181601666" style="zoom:25%;" /><img src="https://ik.imagekit.io/haochen/Typora/image-20220729181633726.png" alt="image-20220729181633726" style="zoom:25%;" />

   线性插值投影问题， 大angle影响大

   Can treated as Mixing orientation

   ![image-20220729181831054](https://ik.imagekit.io/haochen/Typora/image-20220729181831054.png)



