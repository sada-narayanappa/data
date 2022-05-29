## Computation Graphs

Computation graphs helps to break down the complex derivative functions to make it easier to follow. It also helps to understand how a automated-derivation code works. Here is an example.

Suppose we have a function $J(a,b,c) = 3 (a + b \cdot c)$, we want to find the $J’$ - derivative of $J$ w.r.t. $a,b,c$.

Lets write this equivalently as:

$$\begin{align}
u &= bc      \\\
v &= a + u   \\\
J &= 3v      \\\
\end{align}
$$

We can write this as graph as shown here.

<img src="/static/media/NNBook/imgs/der3.png"  style="width: 3in">


To find derivative of $J$ w.r.t. $a, b, c$ first find the derivative of $J$ w.r.t $v$, which is $\frac{dJ}{dv} = 3$.

Next, we find $J’$ w.r.t $u$, we can do this as follows:

$$
\frac{dJ}{du} = \frac{dJ}{dv}\overset{\cdot}{}\frac{dv}{du}
$$
we already know $\frac{dJ}{dv}$ = 3; and $\frac{dv}{du} = 1$ therefore, $\frac{dJ}{du} = $3$
$$

Similarly, 

$$
\frac{dJ}{da} = \frac{dJ}{dv}\overset{\cdot}{}\frac{dv}{da} = 3\overset{\cdot}{}1 = 3
$$

Continuing this way,

$$
\frac{dJ}{db} = \frac{dJ}{du}\overset{\cdot}{}\frac{du}{db} = 3
\overset{\cdot}{}c \\\
\frac{dJ}{dc} = \frac{dJ}{du}\overset{\cdot}{}\frac{du}{dc} = 3\overset{\cdot}{}b \\\
$$

