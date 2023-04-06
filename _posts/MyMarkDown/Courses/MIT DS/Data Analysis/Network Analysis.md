# Graph Basic

##### Konigsberg Bridge Problem

seven bridge problem



The beginning and the end?

Those are the only two that can have an odd degree,

and everything else has to have an even degree.



![image-20220622224329508](https://ik.imagekit.io/haochen/Typora/image-20220622224329508.png)



![image-20220622224350176](https://ik.imagekit.io/haochen/Typora/image-20220622224350176.png)

### Adjacency Matrix

![image-20220623153513141](https://ik.imagekit.io/haochen/Typora/image-20220623153513141.png)





**To check if it was a tree:**

So you can just run breadth-first search

or depth-first search, starting anywhere.

And it just has to terminate without you getting back

to any one of your nodes.

So that would be one way of checking that a graph is

actually a tree.

### Connected Component

![image-20220623160643543](https://ik.imagekit.io/haochen/Typora/image-20220623160643543.png)

![image-20220623161014796](https://ik.imagekit.io/haochen/Typora/image-20220623161014796.png)

**Power-log distribution** can put the degree distribution into linear relation.



![image-20220623161222443](https://ik.imagekit.io/haochen/Typora/image-20220623161222443.png)

![image-20220623171035319](https://ik.imagekit.io/haochen/Typora/image-20220623171035319.png)



![image-20220623172538500](https://ik.imagekit.io/haochen/Typora/image-20220623172538500.png)

![image-20220623172934679](https://ik.imagekit.io/haochen/Typora/image-20220623172934679.png)



![image-20220623195323439](https://ik.imagekit.io/haochen/Typora/image-20220623195323439.png)





### Clustering Coefficient

![image-20220623195525692](https://ik.imagekit.io/haochen/Typora/image-20220623195525692.png)

![image-20220623195605433](https://ik.imagekit.io/haochen/Typora/image-20220623195605433.png)

![image-20220623200146626](https://ik.imagekit.io/haochen/Typora/image-20220623200146626.png)

### Graph Centrality Measures

that's a measure that captures the importance

of a node in a network



![image-20220624105553661](https://ik.imagekit.io/haochen/Typora/image-20220624105553661.png)



![image-20220624105638652](https://ik.imagekit.io/haochen/Typora/image-20220624105638652.png)

![image-20220624105934854](https://ik.imagekit.io/haochen/Typora/image-20220624105934854.png)





![image-20220624105823371](https://ik.imagekit.io/haochen/Typora/image-20220624105823371.png)

![image-20220624105859001](https://ik.imagekit.io/haochen/Typora/image-20220624105859001.png)



### Eigenvector Centrality

<img src="https://ik.imagekit.io/haochen/Typora/image-20220624112324359.png" alt="image-20220624112324359" style="zoom:33%;" />

**This one here updated: should become the sum of the the neighbors.**

<img src="https://ik.imagekit.io/haochen/Typora/image-20220624112405139.png" alt="image-20220624112405139" style="zoom:33%;" />

**Converge to something?**

<img src="https://ik.imagekit.io/haochen/Typora/image-20220624112659276.png" alt="image-20220624112659276" style="zoom:50%;" />

![image-20220624112743077](https://ik.imagekit.io/haochen/Typora/image-20220624112743077.png)

That is also the node that the most important as well

<img src="https://ik.imagekit.io/haochen/Typora/image-20220624113033789.png" alt="image-20220624113033789" style="zoom:50%;" />

### python图论库：

`networkx.eigenvector_centrality`. 

```python
import networkx as nx
import pandas as pd
import numpy as np

my_graph = nx.Graph(np.array([[1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0]]))

a = nx.eigenvector_centrality_numpy(my_graph)
print(a)
```

Ref：https://networkx.org/documentation/networkx-1.10/reference/classes.digraph.html

Not suitable for Directed Acyclic Graphs (DAGs)

### Katz Centrality

For Directed Acyclic Graphs (DAGs)

So if you have a sink node, then this node

is not pointing to any one.

So its measure, its score is going to be 0 at some point.

And so now you're propagating this score

so you know since the importance comes from pointing towards it.

So now at the next step, all the nodes that point to this node

have scored 0.

So in the end, everyone gets score 0, OK？



**Just give some remedy to every node**

<img src="https://ik.imagekit.io/haochen/Typora/image-20220624114519482.png" alt="image-20220624114519482" style="zoom:30%;" />

![image-20220624114821791](https://ik.imagekit.io/haochen/Typora/image-20220624114821791.png)

```
networkx.katz_centrality
```



###  Page-Rank Centrality; Hubs and Authorities

<img src="https://ik.imagekit.io/haochen/Typora/image-20220624120028262.png" alt="image-20220624120028262" style="zoom:30%;" />

![image-20220624120111757](https://ik.imagekit.io/haochen/Typora/image-20220624120111757.png)

![image-20220624120229413](https://ik.imagekit.io/haochen/Typora/image-20220624120229413.png)

```python
k = nx.katz_centrality_numpy(my_graph, alpha=0.85, beta=1.0)
networkx.pagerank
```



![image-20220624120853176](https://ik.imagekit.io/haochen/Typora/image-20220624120853176.png)



**networkx** has an implementation of the hubs and authorities concept in the algorithm called *HITS*. 

```
h = nx.hits_numpy(my_graph)
```

**Output Hubs and Authorities**



![image-20220624121405687](https://ik.imagekit.io/haochen/Typora/image-20220624121405687.png)





# Spectral Clustering

### Steiner trees

<img src="https://ik.imagekit.io/haochen/Typora/image-20220624161040761.png" alt="image-20220624161040761" style="zoom:33%;" />

There are a lot potential tree, but the smallest is preferred (NP).



<img src="https://ik.imagekit.io/haochen/Typora/image-20220624161421515.png" alt="image-20220624161421515" style="zoom:50%;" />



![image-20220624161702637](https://ik.imagekit.io/haochen/Typora/image-20220624161702637.png)



```
networkx.algorithms.tree.mst.minimum_spanning_tree
```

### Community Detection, Clustering, Modularity Maximization, Louvain Method

![image-20220624165649036](https://ik.imagekit.io/haochen/Typora/image-20220624165649036.png)

##### Graph Laplacian

![image-20220624170245441](https://ik.imagekit.io/haochen/Typora/image-20220624170245441.png)

Public Code: [Recitation_Code_For_Basic_Network_Analysis_With_NetworkX](https://courses.edx.org/assets/courseware/v1/520cd425992a973d2f126feaff3f10aa/asset-v1:MITx+6.419x+2T2022+type@asset+block/recitation_notebooks_networks_networks_recitation_networks_recitation.zip)



# Graphical models

### Erdos-Renyi model

Randomly place edges

<img src="https://ik.imagekit.io/haochen/Typora/image-20220624211522100.png" alt="image-20220624211522100" style="zoom:40%;" />

### Configuration model



![image-20220624214135568](https://ik.imagekit.io/haochen/Typora/image-20220624214135568.png)

Draw the network

```
!apt-get install graphviz graphviz-dev
!pip install pygraphviz 

g = G[1]
nx.draw(g, pos=nx.drawing.nx_agraph.graphviz_layout(g), with_labels=True) 
```

![image-20220709095250875](https://ik.imagekit.io/haochen/Typora/image-20220709095250875.png)

### Relation in Graph

## Compute normalized degree centrality of the player

![image-20220709095205615](https://ik.imagekit.io/haochen/Typora/image-20220709095205615.png)

##  betweenness centrality 

![image-20220709095218909](https://ik.imagekit.io/haochen/Typora/image-20220709095218909.png)

### Eigenvector centrality

![image-20220709095233409](https://ik.imagekit.io/haochen/Typora/image-20220709095233409.png)
$$
\frac{n \times (n-1) \times (n-2)}{2}\\
n^3
$$
