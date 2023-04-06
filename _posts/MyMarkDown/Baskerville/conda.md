**Cache**

/bask/homes/h/hxc093/.cache/pip/wheels/

**Gdown**

```
import gdown
url = "https://drive.google.com/drive/folders/147blfyulF0nljwE3esq8zGOgjgUVSO0Z"
gdown.download_folder(url, quiet=True)
```

**OneDrive Download**

```
wget -c https://gist.github.com/chales/11359952/archive/25f48802442b7986070036d214a2a37b8486282d.zip -O db-connection-test.zip
```

<img src="/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/image-20221211153313649.png" alt="image-20221211153313649" style="zoom:33%;" />





**Download**

```
disable hint:
conda config --set unsatisfiable_hints false

conda install --override-channels  -c conda-forge mamba
--no-deps --no-update-deps
```

**Activate conda-forge**

```
conda config --add channels conda-forge
conda config --set channel_priority flexible # Solved
```

**Clone Env**

```
conda create --name myclone --clone myenv
```

**Create Env with yam**

```
conda env export > pt.yml
conda env create -f py37.yml
```

**Install**

```
conda install -c conda-forge xorg-libx11 -y
conda install -c conda-forge xorg-libxext -y

conda install -c anaconda libxcb -y

conda install -y -c conda-forge -c pytorch pytorch cudatoolkit=10.2
conda install cudatoolkit==10.2 -c pytorch -c conda-forge -y
conda install cudnn==7.4.2 -c pytorch -c conda-forge
conda install -c anaconda cudnn


```

```
libc10_cuda.so


```



##### Torch_Sparse

```
conda install -c bioconda sparsehash -y

conda install -q -y pyg -c pyg
conda install -q -y pytorch -c pytorch
conda install pytorch-sparse -c pyg -y

/anaconda3/envs/xrnerf/lib/python3.7/site-packages/torch/lib/libc10.so
ls /bask/projects/j/jiaoj-3d-vision/Hao/anaconda/envs/py37/lib/python3.7/site-packages/torch/lib/lib*
/bask/projects/j/jiaoj-3d-vision/Hao/anaconda/envs/py37/lib/python3.7/site-packages/torch/lib/libc10_cuda.so

vim /bask/projects/j/jiaoj-3d-vision/Hao/anaconda/envs/py37/lib/python3.7/site-packages/torch/_ops.py
```

```
from torch_sparse import coalesce

```

**Torch Scatter**

```
conda install pyg -c pyg

conda install  --no-update-deps -c conda-forge -c pyg pytorch-scatter

conda install pycuda

# or

pip install torch-scatter -f https://data.pyg.org/whl/torch-1.7.1+cu110.html

pip install torch-sparse -f https://data.pyg.org/whl/torch-${TORCH}+${CUDA}.html
pip install torch-geometric

```

```
conda install -c conda-forge pycuda

conda install  --no-update-deps  --force  --no-deps -c conda-forge -c pyg pytorch-scatter 

pip install git+https://github.com/mapillary/inplace_abn.git


```

**PiP install**

```
pip install --pre torch torchvision torchaudio -f https://download.pytorch.org/whl/nightly/cu110/torch_nightly.html


pip install --pre torch==1.7.1 -f https://download.pytorch.org/whl/nightly/cu110/torch_nightly.html
```

