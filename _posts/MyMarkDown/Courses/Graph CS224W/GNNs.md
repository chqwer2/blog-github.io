# GNNs

<img src="../../../../img/Typora/GNNs/image-20221228152130408.png" alt="image-20221228152130408" style="zoom:53%;" />

## Stacking Layers



## Layers

### Classical GNN Layers: GCN

<img src="../../../../img/Typora/GNNs/image-20221228145752164.png" alt="image-20221228145752164" style="zoom:50%;" />

$N$ is the node degree

### GraphSAGE

<img src="../../../../img/Typora/GNNs/image-20221228150510143.png" alt="image-20221228150510143" style="zoom:50%;" />

<img src="../../../../img/Typora/GNNs/image-20221228150847715.png" alt="image-20221228150847715" style="zoom:50%;" />

### Graph Attention Network (GAT)

<img src="../../../../img/Typora/GNNs/image-20221228151428493.png" alt="image-20221228151428493" style="zoom:50%;" />

How to learn $\alpha_{vu}$?

<img src="../../../../img/Typora/GNNs/image-20221228151926529.png" alt="image-20221228151926529" style="zoom:50%;" />



### Deep Graph Encoders

<img src="../../../../img/Typora/GNNs/image-20221226152659802.png" alt="image-20221226152659802" style="zoom:50%;" />

<img src="../../../../img/Typora/GNNs/image-20221226153129939.png" alt="image-20221226153129939" style="zoom:50%;" />

### A Simple Natural Way

![image-20221226153326469](../../../../img/Typora/GNNs/image-20221226153326469.png)

### Conv on graph (Neighbor based)

Collect info from its neighbor, and aggregate them. 

![image-20221226161306155](../../../../img/Typora/GNNs/image-20221226161306155.png)

![image-20221226161412543](../../../../img/Typora/GNNs/image-20221226161412543.png)

Every node has its own computational graph

Now, we have many NN architecture. 

<img src="../../../../img/Typora/GNNs/image-20221226162127813.png" alt="image-20221226162127813" style="zoom:50%;" />

**How to aggregate information across the layers? **

Need to be Permutation Invariant -> apply NN

**One way is to average**

![image-20221226162654554](../../../../img/Typora/GNNs/image-20221226162654554.png)

$Z_v$ is the final node embedding

![image-20221226163050846](../../../../img/Typora/GNNs/image-20221226163050846.png)

![image-20221226163147703](../../../../img/Typora/GNNs/image-20221226163147703.png)

### How to train?

Use the graph structure as the supervision! 

![image-20221226163413851](../../../../img/Typora/GNNs/image-20221226163413851.png)

### Inductive: New Nodes

It can generalized to unseen nodes

![image-20221226163626895](../../../../img/Typora/GNNs/image-20221226163626895.png)

![image-20221226163544507](../../../../img/Typora/GNNs/image-20221226163544507.png)



<img src="../../../../img/Typora/GNNs/image-20221228143032040.png" alt="image-20221228143032040" style="zoom:80%;" />

<img src="../../../../img/Typora/GNNs/image-20221228143055434.png" alt="image-20221228143055434" style="zoom:57%;" />

<img src="../../../../img/Typora/GNNs/image-20221228143113527.png" alt="image-20221228143113527" style="zoom:50%;" />

And also the (5) Learning Objective 

### Definition

### A GNN Layer - Message and Aggregation

**Message**

<img src="../../../../img/Typora/GNNs/image-20221228144142460.png" alt="image-20221228144142460" style="zoom:53%;" />

**Aggregation**

<img src="../../../../img/Typora/GNNs/image-20221228144223638.png" alt="image-20221228144223638" style="zoom:63%;" />

**Issue**

Info could get lost, for node $v$ :

<img src="../../../../img/Typora/GNNs/image-20221228144508541.png" alt="image-20221228144508541" style="zoom:50%;" />

Nonlinearity can be added to **message or aggregation**.

![image-20221228144858953](../../../../img/Typora/GNNs/image-20221228144858953.png)



