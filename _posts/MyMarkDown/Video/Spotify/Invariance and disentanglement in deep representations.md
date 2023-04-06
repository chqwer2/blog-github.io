# View-invariance

Defining Properties

as informative as the data

has nothing to do with the task

<img src="https://ik.imagekit.io/haochen/Typora/image-20220803221238827.png" alt="image-20220803221238827" style="zoom:50%;" />

no throw away any information about the task

and invariant to the **nuisance**

Minimal and easy to work with

should look for stochastic function of the data.

<img src="https://ik.imagekit.io/haochen/Typora/image-20220803221553963.png" alt="image-20220803221553963" style="zoom:50%;" />

We should measure complexity not by dimensionality, 

If it is a random vector (we want it to be disentangle, independent)

<img src="https://ik.imagekit.io/haochen/Typora/image-20220803221720998.png" alt="image-20220803221720998" style="zoom:50%;" />

Sufficient to the **task**

<img src="https://ik.imagekit.io/haochen/Typora/image-20220803222904035.png" alt="image-20220803222904035" style="zoom:33%;" />

throw as many as you want

If Z is a random vector, should be as independent of each other as possible,

 It is called vector mutual information or total correlation

<img src="https://ik.imagekit.io/haochen/Typora/image-20220803223314166.png" alt="image-20220803223314166" style="zoom:50%;" />

![image-20220803223348322](https://ik.imagekit.io/haochen/Typora/image-20220803223348322.png)

relative entropy between of the task given representation, 0 is perfect

![image-20220803223415018](https://ik.imagekit.io/haochen/Typora/image-20220803223415018.png)

That is the assumption



### information bottleneck

if you are minimizing the exp cross-entropy, you are 

<img src="https://ik.imagekit.io/haochen/Typora/image-20220803224238455.png" alt="image-20220803224238455" style="zoom:50%;" />



### desiderata



### +SGD = how the two connected



New Deep Learning Techniques 2018 "Invariance and disentanglement in deep representations" Stefano Soatto, University of California, Los Angeles (UCLA) Abstract: Theories of Deep Learning are like anatomical parts best not named explicitly in an abstract: Everyone seems to have one. That is why it is important for a theory to be inclusive: It has to be compatible with all known results, and at the very least explain known empirical phenomena. I will describe the basic elements of the Emegence Theory of Deep Learning, that started as a general theory for represenations, and is comprised of three parts: (1) Formalization of desirable properties a representation should possess, based on classical principles of statistical decision and information theory: Sufficiency, Invariance, Minimiality, Independence. This has nothing to do with Deep Leaerning, but is closely tied with the notion of Information Bottleneck and Variational Inference. (2) Description of common empirical losses employed in Deep Learning (e.g., empirical cross-entropy), and implicit or explicit regularization practices, including Dropout, Pooling, as well as recently proven additive entropic components of the loss computed by SGD. Finally, (3) theorems and bounds that show that minimizing suitably (implicitly or explicitly) regularized losses with SGD with respect of the weights implies optimization of the loss described in (1) with respect to the activations of a deep network, and therefore achievement of the desirable properties of the resulting representation formalized in (1). The link between the two is specific to the architecture of deep networks. The theory is related to the Information Bottleneck, but not that described in recent theories, but instead a new Information Bottleneck for the weights of a network, rater than the activation. It is also related to PAC-Bayes, and could be derived with that lens, providing independent validation. It is also related to Kolmogorov complexity. It is also related to “flat minima”, in the sense that the crucial regularizing quantity - the information in the weights - bounds the nuclear norm of the Hessian around critical points. It also shows that there is no need to rethink regularization, and that - unlike the Hessian - information is invariant to reparametrization. Joint work with Alessandro Achille and Pratik Chaudhari. References: [https://arxiv.org/pdf/1706.01350.pdf](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbHZ4MFdUU21qNHhJd2prMGx6dE96Y0RNUXM1UXxBQ3Jtc0tuMFVJeUtCRnZwMm1zdzBHeDVqNEJqeEVvTGRpWmNwU01kR1lmTlVieDFqbDFPbnF6RnRRbWJjbDVzaVV6Y200TlFrS0R0SElnNTBjVTVyX1JSUVo5dU00ZVlGR3V3R01LcG5udXpfS2VTc2NMdS1uRQ&q=https%3A%2F%2Farxiv.org%2Fpdf%2F1706.01350.pdf&v=zbg49SMP5kY) and [https://arxiv.org/abs/1710.11029](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbEgxeXMyeFJ4bmdzbUJISmtGb2loM292T3FuUXxBQ3Jtc0tuTy0xOWdtaWZ2MERBRkVJV250WnlGMzlBUGNkNGVLNnotNVdBMnhoNHYtMzJMZ1lYMVlZNWgtdHExMjJoZm1uWWtoWnRrdzd3RGVxWktBM0xtLUV0T3RuVmJHdUdxenNuWmd5bm5adGFuaWszbjE4VQ&q=https%3A%2F%2Farxiv.org%2Fabs%2F1710.11029&v=zbg49SMP5kY)







