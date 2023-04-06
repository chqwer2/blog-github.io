# SMPL

![image-20220916130050882](https://ik.imagekit.io/haochen/Typora/image-20220916130050882.png)

动作 + 体型 (6890 Nodes) ，24个关节点

固定的拓扑结构

![image-20220916130210257](https://ik.imagekit.io/haochen/Typora/image-20220916130210257.png)

![image-20220916130411329](https://ik.imagekit.io/haochen/Typora/image-20220916130411329.png)

c是运动前非刚性变形

![image-20220916131048937](https://ik.imagekit.io/haochen/Typora/image-20220916131048937.png)

Related code

![image-20220916131750512](https://ik.imagekit.io/haochen/Typora/image-20220916131750512.png)

**Full SMPL code**

![image-20220916132241429](https://ik.imagekit.io/haochen/Typora/image-20220916132241429.png)

### 参数化模型pose和shape输入

![image-20220916132326719](https://ik.imagekit.io/haochen/Typora/image-20220916132326719.png)

李群的方法用exp表示R

因为R矩阵不具有求导性质，R+ΔR不再是旋转矩阵。就要用EXP的形式来求导

![image-20220916132841806](https://ik.imagekit.io/haochen/Typora/image-20220916132841806.png)

要先知道相机位姿

![image-20220916133051736](https://ik.imagekit.io/haochen/Typora/image-20220916133051736.png)

图片上的关节点….， 目标点…

![image-20220916133352238](https://ik.imagekit.io/haochen/Typora/image-20220916133352238.png)

### Transformer 解决遮挡

![image-20220916133900252](https://ik.imagekit.io/haochen/Typora/image-20220916133900252.png)

算关联性值

![image-20220916134030481](https://ik.imagekit.io/haochen/Typora/image-20220916134030481.png)

### Masked

![image-20220916134100126](https://ik.imagekit.io/haochen/Typora/image-20220916134100126.png)

Huawei‘s Noah ECCV 2022 Oral

### CLIFF: Carrying Location Information in Full Frames into Human Pose and Shape Estimation

透视

![image-20220916134235289](https://ik.imagekit.io/haochen/Typora/image-20220916134235289.png)

服装建模…

![image-20220916135429382](https://ik.imagekit.io/haochen/Typora/image-20220916135429382.png)

运动过程中的服装变形

![image-20220916140457710](https://ik.imagekit.io/haochen/Typora/image-20220916140457710.png)

![image-20220916140706743](https://ik.imagekit.io/haochen/Typora/image-20220916140706743.png)

![image-20220916141153581](https://ik.imagekit.io/haochen/Typora/image-20220916141153581.png)

![image-20220916141837613](https://ik.imagekit.io/haochen/Typora/image-20220916141837613.png)

PiFu + 透视

### 基于拟合的方法

拟合网格（MPI）和拟合多视角（ZJU）

![image-20220916142450542](https://ik.imagekit.io/haochen/Typora/image-20220916142450542.png)

![image-20220916142953808](https://ik.imagekit.io/haochen/Typora/image-20220916142953808.png)

投影到2D - 关键点检测

![image-20220916143231713](https://ik.imagekit.io/haochen/Typora/image-20220916143231713.png)

### Neural Boay 和人体参数

![image-20220916143422745](https://ik.imagekit.io/haochen/Typora/image-20220916143422745.png)

人体偏移出衣服

![image-20220916143612503](https://ik.imagekit.io/haochen/Typora/image-20220916143612503.png)

刚性和非刚性Registration

