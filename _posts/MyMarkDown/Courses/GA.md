### Genetic Algo (Evolution Algo)

Link: https://ocw.mit.edu/courses/6-034-artificial-intelligence-fall-2010/resources/lecture-13-learning-genetic-algorithms/

Exploit and Explore

such as how the structures are articulated.

**Mutation** 

How much you allowed per chromosome?

How does step size translate in to mutation?

allow myself to takes step of 1/10.

**Crossover**

Then crossover for jump out the local-maxima (local hills)

![image-20221118093412727](https://ik.imagekit.io/haochen/Typora/image-20221118093412727.png)

chromsome $\to$ phnotype

Each Phnotype $\to$ fitness score $\to$ probability of survival

![image-20221118093816627](https://ik.imagekit.io/haochen/Typora/image-20221118093816627.png)



How you compute the fitness?

How you compute the probability of survival?

How different they are?

<img src="https://ik.imagekit.io/haochen/Typora/image-20221118094243485.png" alt="image-20221118094243485" style="zoom:33%;" />

But these suppose the temperature is one of your fitness characteristics, the hotter the better.

Then you survival $P$ will depend the person next to you, then probability depends on measuring Celsius or Fairenheit. That’s strange, this will shift the probability. 



How about we not care about the actual fitness, rather to care about rank order?

**Rank space method**..

<img src="https://ik.imagekit.io/haochen/Typora/image-20221118100539473.png" alt="image-20221118100539473" style="zoom:33%;" /><img src="https://ik.imagekit.io/haochen/Typora/image-20221118100713967.png" alt="image-20221118100713967" style="zoom:40%;" />

Rank probility = 0.5 

+ +suitable step size can help get it spread out

<img src="https://ik.imagekit.io/haochen/Typora/image-20221118100936218.png" alt="image-20221118100936218" style="zoom:33%;" />

<img src="https://ik.imagekit.io/haochen/Typora/image-20221118103741159.png" alt="image-20221118103741159" style="zoom:33%;" />

+ Then clamp down the step size again

**Diversity Rank**

<img src="https://ik.imagekit.io/haochen/Typora/image-20221118103554934.png" alt="image-20221118103554934" style="zoom:33%;" />

Help the chromosome to spread out

<img src="https://ik.imagekit.io/haochen/Typora/image-20221118103754672.png" alt="image-20221118103754672" style="zoom: 33%;" />

can also handle Moat Problem

<img src="https://ik.imagekit.io/haochen/Typora/image-20221118103932591.png" alt="image-20221118103932591" style="zoom:33%;" />

### 

### Particle Swarm Optimization

Birds fishes







