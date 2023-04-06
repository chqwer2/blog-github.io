### Attention is All You Need

Encoder + Attention Mechinism + Decoder = Main stream

Simple network architecture

BLEU score in machine translation

##### Recurrent -> Multi-head attention

sequential model cannot be paralized

<img src="https://chqwer2.github.io/img/Typora/image-20211030110809987.png" alt="image-20211030110809987" style="zoom:50%;" />





### SwinIR

SwinIR is made up of three modules: shallow feature extraction, deep feature extraction, and high-quality (HQ) image reconstruction (shown in the diagram below).

**卷积善于进行早期视觉处理，同时有助于稳化训练并取得更优结果**。

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/SwinIR-1024x364.png)



### Swin-Transformer

[video](https://www.bilibili.com/video/BV1eb4y1k7fj/?spm_id_from=333.788.recommend_more_video.-1)

![image-20221127102011690](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221127102011690.png)



***hierarchical feature maps\***

##### Patch Merging

can we downsample feature maps in a pure transformer network without using convolution?

convolution-free downsampling technique used in Swin Transformer is known as **patch merging**.

![img](https://miro.medium.com/max/1400/1*0MDU8PIJ-wS_fpz-48xGJQ.gif))

##### Window-based Self-Attention

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/1*XbTV-X6eZ8iXEvhsl04N8Q.gif)

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/1*sincgodQpiqGet67un55rg.gif)



![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/1*qJ6egEhj-KtW1MAJ-sxwxQ.gif)







![image-20211114193110685](https://chqwer2.github.io/img/Typora/image-20211114193110685.png)

![image-20211114193122539](https://chqwer2.github.io/img/Typora/image-20211114193122539.png)

Patch and Geometry Bias

![image-20211114193220626](https://chqwer2.github.io/img/Typora/image-20211114193220626.png)

![image-20211114193304720](https://chqwer2.github.io/img/Typora/image-20211114193304720.png)

Learnable NMS

![image-20211114193410156](https://chqwer2.github.io/img/Typora/image-20211114193410156.png)

解释为一个查询问题

![image-20211114193418186](https://chqwer2.github.io/img/Typora/image-20211114193418186.png)

![image-20211114193853350](https://chqwer2.github.io/img/Typora/image-20211114193853350.png)







![image-20211114194053525](https://chqwer2.github.io/img/Typora/image-20211114194053525.png)

![image-20211114195522837](https://chqwer2.github.io/img/Typora/image-20211114195522837.png)

![image-20211114195638908](https://chqwer2.github.io/img/Typora/image-20211114195638908.png)

![image-20211114195926639](https://chqwer2.github.io/img/Typora/image-20211114195926639.png)

![image-20211114200022418](https://chqwer2.github.io/img/Typora/image-20211114200022418.png)

![image-20211114200130643](https://chqwer2.github.io/img/Typora/image-20211114200130643.png)

为什么加入B可以引入平行不变性

![image-20211114200321213](https://chqwer2.github.io/img/Typora/image-20211114200321213.png)

![image-20211114200409229](https://chqwer2.github.io/img/Typora/image-20211114200409229.png)

![image-20211114200610740](https://chqwer2.github.io/img/Typora/image-20211114200610740.png)

Self-Supervised Learning

![image-20211114200830770](https://chqwer2.github.io/img/Typora/image-20211114200830770.png)

![image-20211114201003059](https://chqwer2.github.io/img/Typora/image-20211114201003059.png)

![image-20211114201028731](https://chqwer2.github.io/img/Typora/image-20211114201028731.png)

### Swin-Transformer V2

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/v2-0e6adf516e16f75c79b9096019d4caad_1440w.webp)

第一个改进是，将原本transformer block中的**pre-norm操作替换为了post-norm操作**

第二个【Scaled cosine attention】

原始self-attention中对于两两特征之间的相似度衡量是用的内积，作者观察到当替换为post-norm操作后，在大模型下，某些block或者head中的attention map会被某些特征主导，为了改善这个问题，作者将内积相似度替换为了余弦相似度

![img](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/v2-db7d7b8d5e40c7af67c6e32a4da3aac9_1440w.png)

第三个是【Log-spaced contiguous position bias（log spaced CPB）】

![image-20221127103912709](/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221127103912709.png)

