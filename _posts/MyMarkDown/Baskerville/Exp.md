# Baskerville

Home:     /bask/homes/h/hxc093

Project:    /bask/projects/j/jiaoj-3d-vision/Hao  



### Data

```python
du -lh --max-depth=1
```

tf13, py37



​    

 /bask/projects/j/jiaoj-3d-vision/Hao

/rds/projects/j/jiaoj-3d-computer-vision/Hao/anaconda3/envs/py37/bin/python



```
pip install --user
```

/rds/projects/j/jiaoj-3d-computer-vision/Hao/data/DIV2K_train_HR

/rds/projects/j/jiaoj-3d-computer-vision/Hao/data/CBSD68-dataset/CBSD68/original

/rds/projects/j/jiaoj-3d-computer-vision/Hao/anaconda3/condabin/conda

conda create -n py37 python==3.7

cd /rds/projects/j/jiaoj-3d-computer-vision/Hao

conda activate py37

conda install torch, matplotlib, scipy, scikit-learn

### SwinIR

du -sh –max-depth=0 *

```
cd /rds/projects/j/jiaoj-3d-computer-vision/Hao
cd exp/KAIR/
python main_train_psnr.py --opt options/swinir/train_swinir.json  
```

```
python -m torch.distributed.launch\
        --nproc_per_node=1 \
        --master_port=1234 \
        main_train_psnr.py --opt options/swinir/train_swinir.json  --dist True
```

```
pip install typing_extensions
```

Load

```
CUDA/11.3.1
OPenCV/CUDA
```

**To find out the Linux distribution name, type in the following command –**  

```undefined
cat /etc/*-release
```

Set 

```py
export CUDA_HOME=/usr/local/cuda-X.X
```

### N2N

### Dataset

```
conda create -n my python=3.7 
conda init bash && source /root/.bashrc
```

```
python dataset_tool_tf.py \
        --input-dir /root/autodl-tmp/data/DIV2K_train_HR \
        --out=datasets/imagenet_val_raw.tfrecords
```

```
python dataset_tool_tf.py \
        --input-dir /root/autodl-tmp/data/coco/val2017 \
        --out=datasets/imagenet_val_raw.tfrecords
```

##### Run

```
cd /root/autodl-tmp/noise2noise
python config.py \
        --desc='-test' train \
        --train-tfrecords=datasets/imagenet_val_raw.tfrecords --long-train=true --noise=gaussian
```





### CVF-SID_PyTorch

https://github.com/Reyhanehne/CVF-SID_PyTorch

```
python train.py --device 0 --config config_SIDD_Val.json --tag SIDD_Val
```

```
# Test
cd /root/autodl-tmp/CVF-SID_PyTorch/src

python test.py --device 0 \
		--config ../models/CVF_SID/SIDD_Val/config.json \
		--resume 		../models/CVF_SID/SIDD_Val/model_best.pth

```



### Linux

查看linux容量

df ： disk free

### Download from Colab

```
pip install gdown


gdown https://drive.google.com/uc?id=<file_id>  # for files
gdown <file_id>                                 # alternative format
gdown --folder https://drive.google.com/drive/folders/<file_id>  # for folders
gdown --folder --id <file_id>                                   # this format works for folders too


```

