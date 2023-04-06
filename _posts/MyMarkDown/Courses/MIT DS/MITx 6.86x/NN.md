![image-20220624223223046](https://ik.imagekit.io/haochen/Typora/image-20220624223223046.png)

![image-20220624230338192](https://ik.imagekit.io/haochen/Typora/image-20220624230338192.png)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220624230508294.png" alt="image-20220624230508294" style="zoom:50%;" />

![image-20220624231601047](https://ik.imagekit.io/haochen/Typora/image-20220624231601047.png)

![image-20220624231614048](https://ik.imagekit.io/haochen/Typora/image-20220624231614048.png)

![image-20220624231700111](https://ik.imagekit.io/haochen/Typora/image-20220624231700111.png)

C is the loss and a is the output 

![image-20220626213221183](https://ik.imagekit.io/haochen/Typora/image-20220626213221183.png)

![image-20220626213242012](https://ik.imagekit.io/haochen/Typora/image-20220626213242012.png)

### **Overcapacity** 

![image-20220624232037581](https://ik.imagekit.io/haochen/Typora/image-20220624232037581.png)

many things actually doing **random things**

<img src="https://ik.imagekit.io/haochen/Typora/image-20220624232118314.png" alt="image-20220624232118314" style="zoom:33%;" />

##### Random initialise Bias

![image-20220624232155184](https://ik.imagekit.io/haochen/Typora/image-20220624232155184.png)



But larger, easier to learn as larger model



### Gating and LSTM 

![image-20220625075142628](https://ik.imagekit.io/haochen/Typora/image-20220625075142628.png)

##### Simple RNN

![image-20220625075215759](https://ik.imagekit.io/haochen/Typora/image-20220625075215759.png)

##### LSTM

<img src="https://ik.imagekit.io/haochen/Typora/image-20220625223134339.png" alt="image-20220625223134339" style="zoom:50%;" />

![image-20220625075236744](https://ik.imagekit.io/haochen/Typora/image-20220625075236744.png)

![image-20220626211348764](https://ik.imagekit.io/haochen/Typora/image-20220626211348764.png)

### Markov Models

![image-20220625080318985](https://ik.imagekit.io/haochen/Typora/image-20220625080318985.png)



![image-20220625080629304](https://ik.imagekit.io/haochen/Typora/image-20220625080629304.png)



bigram model is what?

##### Feature-Based Markov Model

![image-20220625081527667](https://ik.imagekit.io/haochen/Typora/image-20220625081527667.png)



##### Difference of Markov Model and Feedforward

![image-20220625082344997](https://ik.imagekit.io/haochen/Typora/image-20220625082344997.png)

### RNNs for Sequences ( n-gram model )

The Markov looks at fixed history

![image-20220625085058807](https://ik.imagekit.io/haochen/Typora/image-20220625085058807.png)

### Convolution=Cross Correlation

![image-20220625090013489](https://ik.imagekit.io/haochen/Typora/image-20220625090013489.png)

![image-20220625090024226](https://ik.imagekit.io/haochen/Typora/image-20220625090024226.png)

![image-20220625091433466](https://ik.imagekit.io/haochen/Typora/image-20220625091433466.png)

![image-20220625095651216](https://ik.imagekit.io/haochen/Typora/image-20220625095651216.png)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220625095725397.png" alt="image-20220625095725397" style="zoom:33%;" />

The filter in CNN is not given, so it is more intuitive to use Cross-correction, because we cannot reverse the order of unknown.

### Derivative of ReLU

![self.epochs_to_train = 10 self.training points = [((2,1), 10), ((3,3), 21), ((4,5), 32), ((6, 6), 42)] self.testing points =](https://ik.imagekit.io/haochen/Typora/1584632147821_image.png)

```
        output_layer_error = y-output  # TODO
        #out_gradient = activated_output - y

        hidden_layer_error = np.transpose(np.multiply(-output_layer_error*self.hidden_to_output_weights, rectified_linear_unit_derivative(output)))# TODO (3 by 1 matrix)

        bias_gradients = hidden_layer_error# TODO
        hidden_to_output_weight_gradients =-(output_layer_error )*np.transpose(hidden_layer_activation)

        input_to_hidden_weight_gradients = np.dot(hidden_layer_error, np.transpose(input_values))
```



### Gradient

$$
\text{out\_error} = \hat y -y\\
\text{hidden\_error} = (\text{output\_error\ *\ hidden\_to\_out\_weights}).T
$$

$$
\text{hidden\_to\_output\_gradients = (output\_error )\ *\ hidden\_layer\_activation.T}
$$

### derivative of the sigmoid 

![image-20220626213937003](https://ik.imagekit.io/haochen/Typora/image-20220626213937003.png)

https://towardsdatascience.com/derivative-of-the-sigmoid-function-536880cf918e

![image-20220626214020624](https://ik.imagekit.io/haochen/Typora/image-20220626214020624.png)