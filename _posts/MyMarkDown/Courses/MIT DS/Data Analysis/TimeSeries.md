# TimeSeries



![image-20220715110641072](https://ik.imagekit.io/haochen/Typora/image-20220715110641072.png)



Weak stationarity

![image-20220715153333408](https://ik.imagekit.io/haochen/Typora/image-20220715153333408.png)

![image-20220715154556282](https://ik.imagekit.io/haochen/Typora/image-20220715154556282.png)



**X = Trend + Sesonality + Stationary (Reminder)**

![image-20220715155647447](https://ik.imagekit.io/haochen/Typora/image-20220715155647447.png)



2. Fitting a nonparametric (e.g. kernel smoothing and local polynomials, -nearest-neighbors; series regression) regression model of the series on the time index and subtracting off the fitted mean function from the series. 
3. ![image-20220715155951190](https://ik.imagekit.io/haochen/Typora/image-20220715155951190.png)

![image-20220715160106032](https://ik.imagekit.io/haochen/Typora/image-20220715160106032.png)

This can remove increasing variance

![image-20220715160224529](https://ik.imagekit.io/haochen/Typora/image-20220715160224529.png)

![image-20220715160617257](https://ik.imagekit.io/haochen/Typora/image-20220715160617257.png)

![image-20220715160626182](https://ik.imagekit.io/haochen/Typora/image-20220715160626182.png)



Marginal -> at each time step

![image-20220715163100127](https://ik.imagekit.io/haochen/Typora/image-20220715163100127.png)

![image-20220715163208938](https://ik.imagekit.io/haochen/Typora/image-20220715163208938.png)

![image-20220715163622467](https://ik.imagekit.io/haochen/Typora/image-20220715163622467.png)

https://www.statsmodels.org/devel/generated/statsmodels.tsa.stattools.ccovf.html

# White noise model

![image-20220716164610530](https://ik.imagekit.io/haochen/Typora/image-20220716164610530.png)

The white noise model is not very interesting. In particular, it has no stochastic dependencies (correlations).

**Autoregressive model appears to be exp-decay**

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716165312550.png" alt="image-20220716165312550" style="zoom:33%;" />

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716165747843.png" alt="image-20220716165747843" style="zoom:33%;" />

The  random walk is not stationary because the variance is growing with time  and the autocovariance depends on the smallest of the two time stamps  rather than on the difference.  

### acf function

ACF - auto-correlation

![image-20220716170503594](https://ik.imagekit.io/haochen/Typora/image-20220716170503594.png)

### Autoregressive Process

![image-20220716170548385](https://ik.imagekit.io/haochen/Typora/image-20220716170548385.png)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716171714492.png" alt="image-20220716171714492" style="zoom:40%;" />

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716171932547.png" alt="image-20220716171932547" style="zoom:50%;" />

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716171950609.png" alt="image-20220716171950609" style="zoom:50%;" />







### Moving average model

![image-20220716172826094](https://ik.imagekit.io/haochen/Typora/image-20220716172826094.png)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716172948383.png" alt="image-20220716172948383" style="zoom: 67%;" />

![image-20220716173549082](https://ik.imagekit.io/haochen/Typora/image-20220716173549082.png)

### Regression for Time-series

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716174338929.png" alt="image-20220716174338929" style="zoom:50%;" />

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716174706179.png" alt="image-20220716174706179" style="zoom:50%;" />

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716174854243.png" alt="image-20220716174854243" style="zoom:50%;" />

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716174905654.png" alt="image-20220716174905654" style="zoom:50%;" />

### Yule-Walker Equation

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716175212453.png" alt="image-20220716175212453" style="zoom:50%;" />

![image-20220716175310457](https://ik.imagekit.io/haochen/Typora/image-20220716175310457.png)

![image-20220716175316712](https://ik.imagekit.io/haochen/Typora/image-20220716175316712.png)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716175354143.png" alt="image-20220716175354143" style="zoom:45%;" />

### Get long-term predictions

<img src="https://ik.imagekit.io/haochen/Typora/image-20220716175619697.png" alt="image-20220716175619697" style="zoom:50%;" />

Well, one thing we can do is we can actually

look at other things, like linear trend

seasonality, et cetera, and we can take that into account.

And these will basically--

like a seasonal trend that will actually be,

basically, going into the future as it is.



![image-20220716175738269](https://ik.imagekit.io/haochen/Typora/image-20220716175738269.png)

### Information Criterion

A tradeoff between data fit and model complexity

![image-20220717185046353](https://ik.imagekit.io/haochen/Typora/image-20220717185046353.png)

![image-20220717185140602](https://ik.imagekit.io/haochen/Typora/image-20220717185140602.png)



### Linear process

<img src="https://ik.imagekit.io/haochen/Typora/image-20220717190234889.png" alt="image-20220717190234889" style="zoom:33%;" />





























