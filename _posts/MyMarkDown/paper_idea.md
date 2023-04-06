### Experiments

Ours (Scratch) Ours

+ Unsupervised Learning
+ Self-supervised Learning

<img src="https://ik.imagekit.io/haochen/Typora/image-20220817141153100.png" alt="image-20220817141153100" style="zoom:33%;" />

对噪声程度敏感的..

对留存信息敏感的…

VGG16 - Classification Trained

CLIP - For  Generation



4.1 in StyleGan, Perceptual Length: Drastic changes when interpolating latent space?

punish highly curved latend space 



Various Noise Identification.



A natural definition for the perceptual path length would be the limit of this sum under
infinitely fine subdivision



we train auxiliary
classification networks for a number of binary attributes,
e.g., to distinguish male and female faces.



<img src="https://ik.imagekit.io/haochen/Typora/image-20220817143243684.png" alt="image-20220817143243684" style="zoom:50%;" />



5 Up

Interestingly, adding a mapping network in front of a traditional
generator results in severe loss of separability in Z but improves the situation in the intermediate latent space W, and
the FID improves as well. This shows that even the traditional generator architecture performs better when we introduce an intermediate latent space that does not have to
follow the distribution of the training data



Across Scales



Diffusion Decoder..

