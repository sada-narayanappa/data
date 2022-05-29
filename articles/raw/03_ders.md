Suppose if we have a function:

$f(a) = 3.a$ when plotted, it looks like in the figure as shown.

<img align=middle src="/static/media/NNBook/imgs/der1.png"  style="width: 3in">

Derivative is just a slope of the function evaluated at any point x.

For example at $x = 2$, slope is height divided by width. Suppose if we evaluate the function by  a small margin say $2+0.0001$ we get $f(2.0001) = 6.0003$. By computing the ratio, we get the slope.

$\frac{(6.0000 - 6.0003)}{(2 - 2.0001)} = 3$.

For this function, slope is 3 regarless of the value of $x$.

In other examples slopes copuld be different at different points.

Thke for example a function $f = a^2$ shown below. 


At point a = 2, slope is 4, when a = 5, the slope is 10. In general for this slope or the derivative is 2a.

<img align=middle src="/static/media/NNBook/imgs/der2.png"  style="width: 6in">

As you can see, one can compute the slope by evaluating the valu at x and nudging the value by a small increment, say by 0.001 and computing the ratio. In general slope can be defined as follows:


$$
\lim _{\Delta a \rightarrow 0}\frac{f(a) - f(a + \Delta a)}{a + \Delta a - a} 
$$

$$
= \lim_{\Delta a \rightarrow 0}\frac{f(a) - f(a + \Delta a)}{\Delta a}
$$ 
