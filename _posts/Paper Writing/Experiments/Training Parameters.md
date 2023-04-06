







We implemented the neural network from Section 3 using the Caffe2 framework3. Each modelwas trained using 4 Tesla M40 GPUs. As described in Section 3, training took place in two stages. 

First a single-frame model was trained. This model used a batch size of 128 andwas trained for 500 epochs in approximately 5 hours. Using this single-frame model as initialization for the multi-frame (8-frame) model, we continue training with a batch size of 32 to accommodate the increased size of the multi-frame model over the single-frame model. This second stage was trained for 125 epochs in approximately 20 hours. We used Adam [25] with a learning rate of 10􀀀4 which decays to zero following a square root law. We trained on 64  64 crops with random flips. Finally, we train the multi-frame model using back-propagation through time [41]