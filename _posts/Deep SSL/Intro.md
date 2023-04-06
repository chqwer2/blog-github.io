# Intro



Denoising is an everlasting topic in the science of Digital Image Processing. Good image denoising increases the image quality and better reflects the information carried by the original image. But the treatment of real noise in images is domain-dependent and non-trivial. 



Plenty of denoising methods have been developed, originating from probability theory, statistical models, linear and nonlinear filtering etc. Many so-called classic methods more or less rely on the explicit or implicit assumption of prior noise distribution, which is usually unknown in a real-world scenario. 

​    

To mitigate this problem, a series of learning-based denoising methods without the requirement of knowing any noise model is proposed. Despite their great ability on learning a mapping from corresponding pairs of noisy and clean images from toy datasets, the performance of their real-world applications heavily depends on a large number of real noisy-clean image pairs for training. Unfortunately, collecting such an aligned pairwise dataset is extremely challenging and expensive in real-world photography and prone to dataset biases as the conditions for obtaining paired images are limited and harsh.



Some works tend to relieve the above cumbersome by synthesising noise or adjusting camera gain to obtain images with different noise levels. However, the real raw image noise is a complex combination of many noise sources and varies greatly among different fields. Existing methods are laborious and unable to target and model all noise sources accurately.

​    

 A more ambitious path is the \textit{Self-supervised} denoising, where the noisy image is used both as input and ground truth to train the network, such as N2N, N2V, N2S, S2S \cite{quan2020self2self}. It is much based on the assumption that the noise is independent of the image signal, and statistics tell us if the model is expressive enough and if enough data is given, it is possible that we can recover the image signal from noise input.



As the self-supervision method only assume the availability of one single unorganized noisy image, It is more applicable for real-world denoising problems across uncountable subfields in science and engineering.



​    

