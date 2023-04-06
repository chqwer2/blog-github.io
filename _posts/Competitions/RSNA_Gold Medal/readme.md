# RSNA2022 解决方案

我们的方案也是由两阶段组成，而且都用到了2.5D CNN，我们从 [@Awsaf](https://www.kaggle.com/awsaf49) 在UWM中的 [UWMGI: 2.5D [Train\] [PyTorch] | Kaggle](https://www.kaggle.com/code/awsaf49/uwmgi-2-5d-train-pytorch) 收获很多。

stage1： 2.5D CNN + Unet for Segmentation 

stage2： CNN + BiGRU + Attention for Classification 

**What is 2.5D**: For CT, 3 channels will be the same.. 

Instead, we change two of three into the former and later inputs (stride = 1).

  

## Stage 1

首先，我们使用了主办方提供的87个Study Segmentation 样本 。我们根据如下的方式重新制作了mask标签

```
0 ---> background  
1 ---> C1  
2 ---> C2  
...
8 ---> T1 - T12  
```

我们采用较为通用的2.5D，拿到了3个通道的图像数据，即原图及其两侧：i-1， i， i+1，每个样本的尺寸320 * 320 * 3。stride=1，这意味着每张slice会被读取3次，这看上去非常笨重，但样本数量较少，训练还是比较快的。配合上我们使用比较高分辨率的分割图，我们在10epochs左右，就可以达到0.96的dice score.



在此的数据增强部分如下，与[UWMGI: 2.5D [Train\] [PyTorch] | Kaggle](https://www.kaggle.com/code/awsaf49/uwmgi-2-5d-train-pytorch) 类似，没有做太多改变：

我们也尝试过更重的数据增强，但没有起到更好的效果。

```
Resize(CFG.img_size, CFG.img_size, interpolation=cv2.INTER_NEAREST),
HorizontalFlip(p=0.5),
ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.05, rotate_limit=10, p=0.5),
OneOf([
    GridDistortion(num_steps=5, distort_limit=0.05, p=1.0),
    ElasticTransform(alpha=1, sigma=50, alpha_affine=50, p=1.0)
], p=0.25),
```



分割模型，我们使用了 segmentation_models_pytorch 库， backbone为efficientnet-b0，decoder为unet。

optimizer="AdamW" 

scheduler="CosineAnnealingLR" + "GradualWarmupSchedulerV3"





## Crop Voxel

当我们训练好分割模型后，我们将其推广到2019个所有的study上，我们对input数据做了和之前相同的方式，模型预测结果后，我们手动查看了若干张预测图像，发现准确度还不错。

我们决定将每个study的7 cervical vertebrae都单独crop出来，每一块cervical 对一个 fracture label（需要使用train.csv对应上），每一块cervical 上，都有24个通道（slice），根据我们的eda发现，大部分study包含200-300个slices，那么平均到每个cervical上 ，就是约30个slice。我们选择24张slice，将被大部分cervical满足。大于24张slice的cervical，我们采用一个简单numpy函数，即可均匀的取到24张slice。

```
sample_index = np.linspace(0, len(one_study_cid)-1, sample_num, dtype=int)
```

对于我们的难点是，本次比赛的训练图像有300GB，如果我们要将裁剪后的3D高分辨的训练图像保存至本地，会超出硬盘的容量，所以我们被迫选择了 记录下裁剪的坐标[x0:x1, y0:y1, z0:z1]以及对应的slice的dcm文件号码，以便在stage2的训练过程中进行读取和裁剪。



## Stage 2

我们经过crop后，我们的input的数据是24张均匀分布的slice，也是GRU的seq_len。

数据采样上，我们忽略了错误的study 1.2.826.0.1.3680043.20574 和 1.2.826.0.1.3680043.29952

关于数据增强，我们使用的和stage1类似，增加了一点点新的增强。

模型上我们使用了 CNN + biGRU + Attention，其中 CNN backbone 我们使用了timm库中的 tf_efficientnetv2_s 和 resnest50d 。另外一些细节，我们初始化了GRU，因为似乎在Pytorch上的GRU原始权重不是非常好。我们还加入了 SpatialDropout ，这也为我们带来了一点点的进步。



## Things we didn't had time to do

1. use bbox csv in yolo
2. Transformer for sequential model





