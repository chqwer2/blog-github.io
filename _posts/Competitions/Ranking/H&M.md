![image-20221217172859116](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20221217172859116.png)

### **NN part ( KF )**

I used E2E NN approach based on the great [baseline notebook](https://www.kaggle.com/code/aerdem4/h-m-pure-pytorch-baseline) published by

### **NN Stacking part ( [@shimacos](https://www.kaggle.com/shimacos) )**

[@shimacos](https://www.kaggle.com/shimacos) built 2 Stacking model from KF's many NN models with LightGBM.

### **Weighted blending ( KF )**

I blended GBDT, NN, and stacked NN models using Optuna to optimize map12 directly.
And then got CV: **0.04047**, Public: **0.03389**, and Private: **0.03394**.





