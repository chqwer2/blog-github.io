### Feature Design

Attributes of the nodes (such as the structure of the protein)

### Node-level Feature

- Node degree: $k$ 

- Node centrality: $c$

  How important this node in a graph

  - Eigenvector centrality

    ![image-20221222092128844](../../../../img/Typora/Feature-based Methods/image-20221222092128844.png)

  - Betweenness centrality

    ![image-20221222092303493](../../../../img/Typora/Feature-based Methods/image-20221222092303493.png)

  - Closeness centrality

    ![image-20221222092511961](../../../../img/Typora/Feature-based Methods/image-20221222092511961.png)

- Clustering coefficient

  measure the local structure
  It counts the triangles in the ego-network (import to such as friend network)

  <img src="../../../../img/Typora/Feature-based Methods/image-20221222092845183.png" alt="image-20221222092845183" style="zoom:50%;" />

- ##### Graphlets

  Rooted connected non-isomorphic subgraphs

  Not just count triangles,

  <img src="../../../../img/Typora/Feature-based Methods/image-20221222093155224.png" alt="image-20221222093155224" style="zoom:33%;" />

  ##### Graphlet Degree Vector (GDV)

  <img src="../../../../img/Typora/Feature-based Methods/image-20221222093600813.png" alt="image-20221222093600813" style="zoom:50%;" />

### Link-level Feature

The task is to predict **new links** based on existing links

##### As a Task

<img src="../../../../img/Typora/Feature-based Methods/image-20221222093942482.png" alt="image-20221222093942482" style="zoom:50%;" />

##### As a Proximity

<img src="../../../../img/Typora/Feature-based Methods/image-20221222094324907.png" alt="image-20221222094324907" style="zoom:50%;" />

##### Features

- Distance

- Local neighborhood overlap

  <img src="../../../../img/Typora/Feature-based Methods/image-20221222094611672.png" alt="image-20221222094611672" style="zoom:30%;" />

- Global neighborhood overlap

  **Katz Index:**

  <img src="../../../../img/Typora/Feature-based Methods/image-20221222095803566.png" alt="image-20221222095803566" style="zoom:33%;" />

  <img src="../../../../img/Typora/Feature-based Methods/image-20221222095718954.png" alt="image-20221222095718954" style="zoom:33%;" />

  The power of Adj Matrices

  <img src="../../../../img/Typora/Feature-based Methods/image-20221222095013938.png" alt="image-20221222095013938" style="zoom:30%;" />

  <img src="../../../../img/Typora/Feature-based Methods/image-20221222095315587.png" alt="image-20221222095315587" style="zoom:30%;" />

### Graph-level Feature

Goal: We want features that characterize the structure of an entire graph.

##### Kernel methods:

<img src="../../../../img/Typora/Feature-based Methods/image-20221222144654121.png" alt="image-20221222144654121" style="zoom:50%;" />

##### Why Graph Kernel?

<img src="../../../../img/Typora/Feature-based Methods/image-20221222144954984.png" alt="image-20221222144954984" style="zoom:33%;" />

##### Graphlets Kernel

Count the number of different graphlets in a graph.

<img src="../../../../img/Typora/Feature-based Methods/image-20221223092229944.png" alt="image-20221223092229944" style="zoom:30%;" />

<img src="../../../../img/Typora/Feature-based Methods/image-20221223092257910.png" alt="image-20221223092257910" style="zoom:33%;" />

**Limitation**: counting graphlets is expensive -> takes $n^k$, with graph size n, size k graphlets

##### Weisfeiler-Lehman Kernel (WL Kernel), color refinement

Color refinement vector?

<img src="../../../../img/Typora/Feature-based Methods/image-20221223093733763.png" alt="image-20221223093733763" style="zoom:33%;" />

<img src="../../../../img/Typora/Feature-based Methods/image-20221223093749847.png" alt="image-20221223093749847" style="zoom:33%;" />



<img src="../../../../img/Typora/Feature-based Methods/image-20221223093308821.png" alt="image-20221223093308821" style="zoom:33%;" />

<img src="../../../../img/Typora/Feature-based Methods/image-20221223093512107.png" alt="image-20221223093512107" style="zoom:33%;" />









