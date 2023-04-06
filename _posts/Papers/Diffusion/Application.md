# Diffusion Application

### Application 1

### *Image Synthesis, Controllable Generation,* *Text-to-Image*

*Conditional generation: given a text prompt c, generate high-res images x.*

![image-20221210170553110](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210170553110.png)

![image-20221210171006906](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210171006906.png)

![image-20221210171140507](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210171140507.png)

![image-20221210171329668](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210171329668.png)

the second gives better performance

![image-20221210171430901](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210171430901.png)

Noise Condition is for decoder..

![image-20221210171530475](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210171530475.png)



##### Variation Visualization

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210171638121.png" alt="image-20221210171638121" style="zoom: 50%;" />

![image-20221210171708562](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210171708562.png)

![image-20221210171735776](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210171735776.png)



### Imagen - also diffusion

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210171937145.png" alt="image-20221210171937145" style="zoom:33%;" />

![image-20221210171952555](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210171952555.png)

![image-20221210172033838](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210172033838.png)

### Diffusion AE

![image-20221210172338906](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210172338906.png)







### *Applications (2):*

### *Image Editing, Image-to-Image,* *Super-resolution, Segmentation*

### Super-Resolution via Repeated Refinement (SR3)

![image-20221210172558617](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210172558617.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210185437377.png" alt="image-20221210185437377" style="zoom:43%;" />

![image-20221210185533555](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210185533555.png)

### Impainting and Colorization

![image-20221210190506600](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210190506600.png)

##### Iterative Latent Variable Refinement - ILVR

![image-20221210190727632](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210190727632.png)

![image-20221210191209284](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210191209284.png)

### Semantic Segmentation

![image-20221210191224249](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210191224249.png)

### Image Editing

![image-20221210192330231](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210192330231.png)

### *Applications (3):*

### *Video Synthesis, Medical Imaging, 3D Generation, Discrete State Models*

![image-20221210192506103](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210192506103.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210192755031.png" alt="image-20221210192755031" style="zoom:50%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210192813900.png" alt="image-20221210192813900" style="zoom:43%;" />

Generate far frames

![image-20221210193211672](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210193211672.png)



##### Solving Inverse Problem in Medical Imaging 

![image-20221210193340955](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210193340955.png)

*Song et al., “Solving Inverse Problems in Medical Imaging with Score-Based Generative Models”, ICLR, 2022*

![image-20221210193540892](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210193540892.png)

![image-20221210193643971](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210193643971.png)



### 3D Shape Generation

Point Cloud

![image-20221210193709733](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210193709733.png)

*•* *Point clouds as 3D shape representation can be diffused easily and intuitively*

*•* *Denoiser implemented based on modern point cloud-processing networks (PointNets & Point-VoxelCNNs)*

##### Conditional Shape

![image-20221210193743389](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210193743389.png)

![image-20221210193810482](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210193810482.png)

