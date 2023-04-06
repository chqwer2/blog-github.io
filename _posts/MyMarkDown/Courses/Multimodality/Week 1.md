# Multimodality

1. Visual (Video or Image), Such as Openface (OpenCV) 

2. Audio (Speech or Sound), Such as Opensml

   FO, MFCC, Zero-crossing rate, Spectrogram, power/mel_Spec

3. Text (Bert, Bart, Word2Vec)

### Flow

Feature Extraction $\to$ Model

Single Model $\to$ How to **Fusion** (V, A, T)

Multi-Model $\to$ 3 Input $\to$ **Co-training**

**Problem**

模态缺失：情感识别

语义对齐：(不同模态 z 在同一分布/语义下)

​	如视频生成 DALLE 和 CLIP

Alignment：feature-level

​	时序，每秒对应的feature

### Text2Face

Image (Face) = 抽象人脸 (Seg) + Description (Latent)

**Problem**

同一语义下的解释不一样， 需要相关的数据集….

人脸的控制，如gender无法顺滑过度

### Face2Text

解耦

### Dataset

FFHQ-Text, 

CelebA + 10 Annotation

1-to-n annotation

### TediGAN

![image-20220829104108582](https://ik.imagekit.io/haochen/Typora/image-20220829104108582.png)

语义进去做描述 （**Image Caption**）

+ Diffusion
+ 生成 + 编辑

我的模型是预测高斯

高维的

**Face2Text**好做一些， 控制Style （）

眼睛，嘴巴分布间转换

<img src="https://ik.imagekit.io/haochen/Typora/image-20220829104703816.png" alt="image-20220829104703816" style="zoom:33%;" />

CycleGAN， 语义的Augmentation

Implicit and Nerf

怎么结合…

CLIP **做不到**细微和语义特征
