## Logistic regression - Back propagation
  
Lets consider a Logistic regression with only two predictors.

These are exactly same as before except we use 'a' for y-hat. We call $a$ as activation function.

Computation graph is

<img src="/static/media/NNBook/imgs/der4.png"  style="width: 3in">

To back-propagate we need to know how to adjust $w_1, w_2$ and $b$ to minimize the loss function $\mathcal{L}$ (error function). In otherwords to find derivative of the Loss function w.r.t to $w_1, w_2, b$ such that $\mathcal{L}'$ is zero (or approximately zero). 

From the computation graph,

$$\begin{align} 
\frac{d\mathcal{L}}{dw_1} &= \frac{d\mathcal{L}}{da}\frac{da}{dz}\frac{dz}{dw_1} & \phantom{xxx}(I) \\\
\frac{d\mathcal{L}}{da}   &= \frac{- y}{a} + \frac{1 - y}{1 - a} & \text{because:}log(1 - a) = \frac{- 1}{1 - a} \\\ 
&=\frac{- (1 - a)y + a(1 - y)}{a(1 - a)} = \frac{a - y}{a(1 - a)} & \phantom{xxx}(A) \\\ 
\text{*NOTE } \\\
\frac{da}{dz} & = \frac{(1 + e^{- z})\overset{\cdot}{}0 + e^{- z}}{(1 + e^{- z})^{2}} & \text{reminder:}a = \frac{1}{(1 + e^{- z})} \\\
&= \frac{e^{- z}}{(1 + e^{- z})^{2}} & \phantom{xxx}(B) \\\
\text{NOTICE } \\\
a = \frac{1}{1 + e^{- z}} & \therefore(1 - a) = \frac{1 + e^{- a} - 1}{1 + e^{- z}} = \frac{e^{- z}}{1 + e^{- z}} & (C) \\\
\\\
\text{Substituting (C) in (B):}  \\\ 
\\\
\frac{da}{dz} &= a(1 - a) & (D) \\\
\\\
\text{Finally:} \\\ 
\\\ 
\frac{dz}{dw_1} &= x_1 & (E) \\\ 
\\\ 
\text{Substituing (A), (D), (E) in (I):} \\\ 
\\\ 
\frac{d\mathcal{L}}{dw_1} &= \frac{d\mathcal{L}}{da}\frac{da}{dz}\frac{dz}{dw_1} \\\
&= \frac{(a - y)}{a(1 - a)} a(1 - a)\overset{\cdot} x_1 \\\
\frac{d\mathcal{L}}{dw_1} &= (a - y)x_1
\end{align} 
$$
   
 
Similarly we get:

$$\begin{align} 
\frac{d\mathcal{L}}{dw_2} &= (a - y)x_2 \\\
\frac{d\mathcal{L}}{db}  &= (a - y) 
\end{align} $$

In general the derivative of loss function is obtained by multiplying corresponding $(a-y)$ with the predicator.

With this we can implement back-propagation for one training to adjust weights:

$$\begin{align} 
dz  &= (a - y)       \\\
dw1 &= dz \cdot w1   \\\
dw2 &= dz \cdot w2   \\\
db  &= dz            \\\
\text{ Update weights as: }  \\\
\\\
w1 &= w1 - \alpha \cot dw1 \\\
w2 &= w2 - \alpha \cdot dw2  \\\
b  &= b - dz              \\\
\end{align}
$$

Repeat until error is minimized; Not a great algorithm. A complete example for m training example is shown below.