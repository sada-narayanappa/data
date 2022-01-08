# Discriminative and Generative Models in ML
---

*Disriminative* and *Generative* models are terms in used in machine learning to describe the characteristics of the learning.

Intuitvely, if we have a classification problem of two classes, one can imagine two ways to learn about the data set.

(1) Either learn, how two classes, $A$ and $B$, are seperated - know what distinguishes the two classes. In other words, you can imagine a boundary  separating $A$ and $B$.

OR

(2) Learn each class and its characteristics. For example you could learn the statistical properties of $A$ just by focussing on $A$. Similarly you can learn about the properties of $B$.

The distinction is very subtle at first. However think how we can use such models.
Suppose if we have new data $x$, then we can know if $x$ belongs to class $A$ or class $B$.

In case of (1) i.e. *Disriminative*, you would check which side of boundary line does $x$ falls and declare the result.

In case of (2) i.e. *Generative* you would compare statistical evidence of which class $A$ or $B$ and declare the result.

There is a mathematical implication of this notion which we will get to soon.

The figures below might help to clariy and we will use these pictures illustrate the further

<img src="/static/articles/imgs/discri.png" style="height:256px; border: 1px solid gray"> <img src="/static/articles/imgs/generative.png" style="height:256px;border: 1px solid gray">

### Mathematical interpretation

Consider a classification problem

Labels: $Y=y $, and
Features: $X={x_1, x_2, … x_n}$

If the joint distribution of the model can be represented as $p(Y,X) = P(y,x_1,x_2…x_n)$

We almost always want to do two things in ML
(1) train the model
(2) given a new data point, determine the class it belongs to - i.e. P(Y=1|X) or P(Y=0|X)

Both generative and discriminative approaches solve this in different ways.

In case of **Generative** models, the model consists of learning
$P(X|y)$ and $P(y)$ - if we have these two, we can apply Bayes theorem to compute $P(y|X)$
i.e.

$$P(y=1|X) = \frac {P(X|y=1) . P(y=0)}{P(X)} $$
$$P(y=0|X) = \frac {P(X|y=0) . P(y=0)}{P(X)} $$‣

The way to apply is find the probability of both $P(Y=1|X)$ and $P(Y=0|X)$ and choose the $max(P(Y=1|X), P(Y=0|X))$.

In case of **Discriminative** models,
we learn the boundary directly that disntinguishes y=1 and y=0 by learning $P(Y=1|X)$ directly. 


> Interview Question.
When do use *Disriminative* Vs *Generative*? 
.
Generative models:
+ need fewer data to train.
+ they make stronger assumptions i.e, assumption of conditional independence.
+ Can work with missing data because it can marginalize over unseen variables
- less Accurate 
- Disriminate models are preferred for "outliers"

### Examples
<table width=90%>
  <tr><th>*Disriminative* </th><th> *Generative* </th></tr>
<tr><td>Logistic regression
Scalar Vector Machine (SVMs)
‌Traditional neural networks
‌Nearest neighbor
Conditional Random Fields (CRFs)
Decision Trees and Random Forest
</td><td>‌Naïve Bayes
Bayesian networks
Markov random fields
‌Hidden Markov Models (HMMs)
Latent Dirichlet Allocation (LDA)
Generative Adversarial Networks (GANs)
  Autoregressive Model</td></tr></table>
  
<hr/>
## References

<iframe src="https://www.youtube.com/embed/z5UQyCESW64"
    width="640"    height="480" frameborder="0"
    allow="autoplay; encrypted-media" allowfullscreen
></iframe>  

<iframe src="https://www.youtube.com/embed/nt63k3bfXS0"
    width="640"    height="480" frameborder="0"
    allow="autoplay; encrypted-media" allowfullscreen
></iframe>  

 
