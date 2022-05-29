# CHAPTER 1 

---

## What is a Neural Network

Consider a simple function of predicting the house prices based on the size of the house. This is a simple function that finds a linear fit of the data and also a simple neural network that takes a size of the house and outputs the price.

<img src="/static/media/NNBook/imgs/nn1.png"  style="width: 3in">

A simple network fits a function to points shown in cross marks. The resulting function is called RELU function (Rectified Linear Unit) which will be described later. However, the methods to fit the function to set of predictors is what NN does. The term deep learning refers to training deep neural networks which will be discussed later.


If we have multiple features such as, size, #bedrooms, Zip code etc. then we may have lot more cells (or neurons).

<img src="/static/media/NNBook/imgs/nn2.png"  style="width: 3in">

A Neural Network is a set of nodes that takes the input and predicts a function that maps input to the  output - we denote the predicted value using $\hat{y}$. 


### Notations

<pre>
m			Size of length of training examples	
n			Length of predictors X = |X|
X			Notation for input predictors		
$x^{(i)}$   Super script $(i)$ represents the ith example


</pre> 

---
## Binary classification

Binary classification is given an input, classify the data into one or other class. As an example: if we are given a set of images, classify them as pictures of cat or non-cats.

### Logistic regression

*Logistic regression*   is used for classification problems. The term **regression** here seems to indicate otherwise. Model predicts a number between 0 and 1 and a threshold is used to compare the result to predict one or other depending upon if it is greater or lesser than the threshold. A threshold T (usually 0.5) which indicates if it the predicted number is less than threshold T then we predict one otherwise other class.

Here we are restricting for two classes - however, later we show how it can be extended to show multiple classes.

In Linear regression we had the hypothesis function

$$h = \theta^T X $$ 
                           
We would like to interpret $h$ as a probability function. As is, it is not a function that can do binary classification becuase the values are not between 0 and 1.

Therefore if we consider the *logit* AKA **log of odds** where $P$ as the conditional probability of output give input $X$:

$$\begin{matrix}
P = g(x) \\\
log \frac{P}{1-P} = z = \theta^T X \\\ 
\end{matrix}
$$

$g$ is a function that translates hypothesis $h$ to $P$, the probability function conditioned on $X$		
Given $X$ we want to compute the output  $\hat{y} = P( y = 1 | X )$  s.t. Probability that $y = 1$. 

Solving for P, we get:
			$$P = \frac{1}{1+e^{-z}}$$ 

Therefore, in Logistic Regression, the form of the hypothesis takes the form:

\begin{matrix}
 h(x) = g(\theta^T x) \\\\
 g(\theta^T x) = \frac{1}{1+e^{-z}}  \\\\
 z = \theta^T x  
\end{matrix}

---
#### Derivation of Sigmoid function:

<div class="alert alert-success">
<strong>Derivation of Sigmoid function:</strong> 

\begin{matrix}
P = g(x) \\\
log \frac{P}{1-P} = z = \theta^T X   \\\ 
e^{log \frac{P}{1-P}} = e^z          \\\ 
\frac{P}{1-P} = e^z                  \\\ 
\frac{1-P}{P} = e^{-z}               \\\ 
\frac{1}{P} -1= e^{-z}               \\\ 
\frac{1}{P}   = 1 + e^{-z}           \\\ 
P             = \frac{1}{1 + e^{-z}} \\\
\end{matrix}

----
<img src="/static/media/NNBook/imgs/sigmoid.png" align=left 
     style="width:2.59327in;height:1in; padding-right: 50px;" />

The function $g$ is called Logistic function or Sigmoid function. Logistic or Sigmoid can be used interchangeably.

It is shown on the figure left. 

<br/>
</div>
When $z>>0$, the $e^{-z} \rightarrow 1$ function $g \rightarrow 1$

when $z<<0$, the $e^{-z} \rightarrow \infty$ then $g \rightarrow 0$

When at 0, g(x) is 0.5.

when $z$ is +ve the term $e^{− z} < 1$, therefore, $\frac{1}{1 + e^{- z}}$ is greater than $\frac{1}{2}$; and when $z$ is -ve the denominator is > 2 and thus $g$ will be < 0.5


$$g = \begin{matrix} \frac{1}{1 + e^{0}} = 0.5, & 
\text{if }z = 0 \\ > .5,  & 
\text{z < 1}    \\ < 0.5, & 
\text{z > 1}   \\ 
\end{matrix}
$$

You may recall that in Linear regressions we had the cost function:

$$Cost(\text{AKA Loss function }\mathcal{L}) = J(\theta) = \frac{1}{2m}\overset{m}{\sum_{1}}(\widehat{y} - y)^{2}$$

sum of squares of residues We need to modify this because $(ŷ − y)^2$ is non-convex function for $y$ in [0, 1]. If you plot it will look wavy with no one max or minima. Gradient Decent wants a convex function to converge to find a global minimum.


In Logistic Regression, given $X$ a set of $m$ examples: 
  
$$(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), ...(x^{(m)}, y^{(m)})$$ , 
  
we want to compute $\hat{y}  \approx y^{(i)}$ 

Where $\widehat{y} = \frac{1}{1 + e^{- z}}$ in the training example want it to be as close match as possible.

We define the cost function for single training example as:


<table border=0  ><tr valign="middle" ><td>  
$$
Cost(\hat{y},y)=
  \begin{Bmatrix}
    -\log \hat{y},     & \text{if  } y = 1 \\\
    -\log(1- \hat{y})  & \text{if  } y = 0 \\\
  \end{Bmatrix}
$$ 
 </td><td> 
If y is 1, then want $\hat{y}$ to be close to 1 anything less is incurred as cost
If y is 0, then want $\hat{y}$ to be close to 0, otherwise cost is the difference.
</td></tr></table> 
   
Since log of number  that lies in [0, 1] is negative, we take the negative log. The above equation can be combined in equation:

$$[ −y_i \log \hat{y} − (1 − y_i) \log(1 − \hat{y})]$$ when $y_i$ is 0, first term goes away and similarly second term when $y_i$ is 1
 
The cost function for the entire training set is defined as:

$$J(\theta) = - \frac{1}{m}\overset{m}{\sum_{i = 1}}y^{i}\log({\widehat{y}}^{i}) + (1 - y^{i})\log(1 - {\widehat{y}}^{i}))$$

Now all that remains to be done is to find $\theta$ to minimize $𝐽(\theta)$ that is convex such that the slope is zero (first derivate) is zero.


> *NOTE* - We want to find  𝜃 that minimize the cost function. In order to find the minimum:

>* We take the first order differentiation of the equation to be minimized
* Find the roots from step (1) - Since Cost function is convex, there should be only one root.
 
 
$h_{(\theta(x))} $ is defined as follows:
  
$$
\begin{matrix}
\widehat{y}  = h_{\theta}(x) = g(\theta^{T}x) = g(z) \\\
g(z)    = \frac{1}{1 + e^{- z}} \\\  
\frac{\partial}{\partial\theta_j} J(\theta) = \\\
 \sum_i^m  = (\hat{y} - y^i) x_j^{(i)}  
\end{matrix}
$$
 
---
 
  