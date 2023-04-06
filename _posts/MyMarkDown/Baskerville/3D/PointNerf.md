### PointNerf

Project:    /bask/projects/j/jiaoj-3d-vision/Hao/3D

```
conda activate point pt
```

**Run** **Per-scene Optimization**

```
python data/download-scannet.py -o data_src/scannet/ --id scene0101_04
python data/download-scannet.py -o data_src/nrData/scannet/ --id scene0241_01

python ScanNet/SensReader/python/reader.py --filename data_src/scannet/scans/scene0101_04/scene0101_04.sens  --output_path data_src/scannet/scans/scene0101_04/exported/ --export_depth_images --export_color_images --export_poses --export_intrinsics
```

train scripts

```
    bash dev_scripts/w_scannet_etf/scene101.sh 
    bash dev_scripts/w_scannet_etf/sc3ne241.sh
```

test scripts

```
    bash dev_scripts/w_scannet_etf/scane101_test.sh
    
    bash dev_scripts/w_scannet_etf/scane241_test.sh
```





**Data:**

How to download: https://github.com/tickstep/aliyunpan#%E4%B8%8B%E8%BD%BD%E6%96%87%E4%BB%B6

aliyun账号:13867466412 密码:zhang19900213



Project link:

https://github.com/Xharlie/pointnerf

```
pointnerf
├── data_src
│   ├── scannet
    │   │   │──scans 
    |   │   │   │──scene0101_04
    |   │   │   │──scene0241_01
```

Download using official link in the [here](https://github.com/Xharlie/pointnerf)



