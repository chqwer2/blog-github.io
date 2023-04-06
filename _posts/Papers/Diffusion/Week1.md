基础：

Diffusion model - https://proceedings.neurips.cc/paper/2020/file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf

Stable Diffusion：

Stable diffusion -  https://arxiv.org/pdf/2112.10752.pdf

Conditional Stable diffusion:

ControlNet - https://arxiv.org/pdf/2302.05543.pdf

T2I-Adapter - https://arxiv.org/pdf/2302.08453.pdf

Depth render:

Infinite Nature - https://arxiv.org/pdf/2012.09855.pdf





### Why Diffusion Model?

https://lilianweng.github.io/posts/2021-07-11-diffusion-models/

reverse the diffusion process to construct desired data samples from the noise

diffusion models are learned with a fixed procedure and the latent variable has high dimensionality 

<img src="https://lilianweng.github.io/posts/2021-07-11-diffusion-models/generative-overview.png" alt="img" style="zoom:15%;" />

*denoising diffusion probabilistic models* (**DDPM**; [Ho et al. 2020](https://arxiv.org/abs/2006.11239)).

![image-20221210145717381](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210145717381.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210145741201.png" alt="image-20221210145741201" style="zoom:53%;" />

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/DDPM.png" alt="img" style="zoom:33%;" />

The Markov chain of forward (reverse) diffusion process of generating a sample by slowly adding (removing) noise. (Image source: [Ho et al. 2020](https://arxiv.org/abs/2006.11239) with a few additional annotations)



#####  [Reparameterization Trick](https://lilianweng.github.io/posts/2018-08-12-vae/#reparameterization-trick)

![image-20221210150222004](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210150222004.png)

<img src="https://lilianweng.github.io/posts/2018-08-12-vae/reparameterization-trick.png" alt="img" style="zoom:33%;" />

##### DDPM

![image-20221210145928005](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210145928005.png)

![image-20221210151038985](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210151038985.png)



### Reverse Process

![image-20221210151600244](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210151600244.png)

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/diffusion-example.png)

![image-20221210152022506](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210152022506-0656823.png)

#### Speed up Diffusion Model Sampling

![image-20221210152308697](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210152308697.png)

 [nice property](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/#nice):

![image-20221210152520066](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210152520066.png)

### DDIM

![image-20221210152744111](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210152744111.png)

![image-20221210152843909](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210152843909.png)

### LDM - Latent

*Latent diffusion model* (**LDM**; [Rombach & Blattmann, et al. 2022](https://arxiv.org/abs/2112.10752)) 

![image-20221210153003405](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210153003405.png)



### Generation

![image-20221210153311963](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210153311963.png)

### Conditional Generation

![image-20221210153354876](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210153354876.png)

![image-20221210153407560](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210153407560.png)

![image-20221210153425864](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210153425864.png)









### **CVPR 2022 Tutorial:**

Denoising Diffusion-based Generative Modeling: 
Foundations and Applications

https://cvpr2022-tutorial-diffusion-models.github.io/

https://lilianweng.github.io/posts/2021-07-11-diffusion-models/

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/diffusion.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221210100743925.png" alt="image-20221210100743925" style="zoom:33%;" />

![image-20221203002231345](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221203002231345.png)

![image-20221203002245926](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221203002245926.png)

### Part 1 Denoising Diffusion Probabilistic Model

![image-20221203002715170](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221203002715170.png)

![image-20221203002936631](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221203002936631.png)

![image-20221203003122091](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221203003122091.png)

##### Diffusion Kernel

![image-20221203093138494](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221203093138494.png)

PPT: https://drive.google.com/file/d/1DYHDbt1tSl9oqm3O333biRYzSCOtdtmn/view

![image-20221203093856182](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221203093856182.png)

### Reverse Denoising Process

![image-20221203093929799](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221203093929799.png)



Sampling…

![image-20221203105236602](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221203105236602.png)

### Implementation 

![image-20221203105313487](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221203105313487.png)

![image-20221203105920566](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221203105920566.png)

### Connected to VAEs

![image-20221207161958299](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221207161958299.png)

See [“Elucidating the Design Space of Diffusion-Based Generative Models” by Karras et al.”()



## Score-based Generative Model

![image-20221207162507651](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221207162507651.png)

![image-20221207162736046](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221207162736046.png)

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221207162856292.png" alt="image-20221207162856292" style="zoom:50%;" />

![image-20221207163007493](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221207163007493.png)

The decision is stochastic. 



















