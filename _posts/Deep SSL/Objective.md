**否完全不要训练集**

 但这对减少由单张图像带来的大 ![[公式]](https://ik.imagekit.io/haochen/Typora/equation) 是无效的，所以N2V和N2S这两种方法在单幅图像上训练时效果不佳。简要来说，**减少 ![[公式]](https://www.zhihu.com/equation?tex=%5Ctext%7Bvariance%7D) 是单幅图自监督学习**的关键。

[0]使用了Dropout技术来减少 ![[公式]](https://ik.imagekit.io/haochen/Typora/equation-20220609095711202) 。在深度神经网络中，Dropout[9]是一个常用的正则化技术，指的是在训练过程中随机丢掉一些节点。由Dropout带来的模型不确定性，使得这些模型的预测有着独立统计的确定度，因此这些预测的平均可以减少结果的方差。

但是这一类方法一张图片需要训练一个模型，不具有泛化能力。



 相似含噪图像采样位置不同而导致的图像过于平滑的问题

# Objective



Self2Self is a very recent self-supervised framework that iterates the image itself multiple times to get performance competitive to the supervised learning. 

It is now the state-of-the-art out of the various self-supervised denoising methods. 

But this method comes with several drawbacks preventing itself from practical use:



Which are the **considerable run time**, **single image specified model**, **poor neighbourhood denoising assumption** and **unoptimistic loss metrics**.



##### Considerable run time

 For real-world applications, such as medical image denoising, run time is a critical factor that needs to be considered. Self2Self is much slower than supervised learning. Unlike the latter one which uses a learned model and only does one-time inference, Self2Self needs to iterate one image about $1.5 \times 10^5$ times that may take hours to converge. The faster convergence method should be taken to empower this method. 



##### Single image specified model

The second is that this line of methods requires a specific model for every single image, which extremely undermines the practical ability to reuse this method. 

So it is possible to use meta-learning or memory banj to capture shared features across images that can reduce this limitation to learn only part of the model rather than the whole.



##### Poor neighbourhood denoising assumption

This line of methods is largely based on assumptions with Additive Gaussian Noise Model and Neighbour Information recovery theory. This theory is saying that large observed random noise is aligned with a mean equal to 0, and the pixel information is strongly related to its neighbour pixels, thus, it is possible to recover the clean pixel information based on observation of its neighbour pixels and can potentially eliminate the influence of the noise in neighbours because according to the law of large number, the influence of noise will eventually be brought to its mean value, which is the 0. 



This strong assumption can be poor in some fields, where global systematic and structural can be hard to handle. Basically obtaining information from the neighbourhood is not satisfying for demonising.

​       

##### Unoptimistic loss metrics

The widely used loss metric in demonising, and in the majority of other image processing fields is the Mean Square Error (MSE), which is mathematically equal to Peak Signal-to-Noise Ratio (PSNR), a widely recognised objective metric.



Statistically, MSE works fine to minimize the distance between prediction and ground truth, which can be seen as minimising the square bias plus variance of the estimator. As we usually assume that we have an unbiased estimator, the MSE only works to reduce the variance, which can be compromised as the predicted value is close enough. 



However, the pixel-wise approximated value can be compromised and is not a good representation of the target value, which is correlated with other pixels across the image.

  

The problem is we want to maximize the quality of the image rather than minimise the estimator variance.



##### Other Problem

 Self2Self only performing one single output and merge it with the original input into next stage, which acting like a one stage recurrent unit. The shared problem of this kind of recurrent architecture is that the error produced in some time stamps can be inherited with it off-springs, and the information loss in the procedure can not be recovered. 





### Approach

##### Time Concern

​    Self2Self is only training with one image sample that makes the network hard to converge compared to the large batch supervised training. Thus, inspired with Unsupervised Contrastive Learning, it is possible that we can using data augmentation to boost the training process with more image samples.

​    

​    Another possible way to reduce the running time is similar to \textit{divide and conquer} ideas in Search Algorithms. We can devide the image into parts and running in parallel, thus can give us run time boost.



​    And because the rotation invariance of much of the image, we can also treat the network with outputing \textit{prediction candidates}, that is to say network now can output denoised image with $4\times$ Rotation, and that average can also be seen as a more robust prediction.



##### Single image specified model

One possibility is to set up a noise feature extractor to work as a noise prior to guiding the training process.









##### Poor neighbourhood denoising assumption

This can be redeemed by various methods.



##### Unoptimistic loss metrics

Encouraging disentanglement with MSE term still only shown on relatively toy domains.



##### Other Possibility

​    In statistical views, the target of the network can be recognised as estimating a high-dimension distribution. General network will treat the sample mean as the output because it is with the highest possibility, but it will be of much loss. Inspired by DivNoising (Krull), which takes many samples from that distribution and average them up to intergrate as much information as possible to recover denoised image, It is possible if we can turn the architecture to assimilate the VAE that we can generate many samples from the distribution, we can get a lossy network that reserve majority of the image information.

​    

