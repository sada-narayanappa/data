# Chapter - Sequence Models

Sequence Models have transformed speech recognition, natural language processing and other areas. ‣
There are lots of diffent types of sequence problems. A few examples of where sequence models are shown below:

* Speech recognition, an input audio clip X and o/p text transcript; both the input and the output here are sequence data - X is an audio clip and Y, the output, is a sequence of words. 

* Music generation is another example, where input can be a singl integer and output is a music sequence.

* Sentiment classification the input X, output an integer

* Machine translation you are given an input sentence to output the translation in a different language. 

<img src="/static/media/NNBook/imgs/lstm1.png"  style="width: 5in">

<video width="320" height="240" controls>
  <source src="/static/media/video/videos/teaching-videos/NNintro.mp4" type="video/mp4">
</video>

--- 

## Notations

<span class="col-md-2"> $X$           </span>  the input
<span class="col-md-2"> $y$           </span>  the ouput                  
<span class="col-md-2"> $T_x$         </span>  Length of i/p sequence     
<span class="col-md-2"> $T_y$         </span>  Length of o/p sequence      
<span class="col-md-2"> $x^{[l]}$     </span>  $[l]$ represents the $l^{th}$ layer  

$x^{(i)}$ is used to represent one of $m$ i/p training example
Similarly $y^{(i)}$ is used to represent one of $m$ training o/p example

Superscript $\langle t \rangle$ denotes an object at the $t^{th}$ time-step. 
Example: $x^{\langle t \rangle}$ is the input x at the $t^{th}$ time-step. $x^{(i)\langle t \rangle}$ is the input at the $t^{th}$ timestep of example $i$.
    
Lowerscript $i$ denotes the $i^{th}$ entry of a vector.
Example: $a^{[l]}_i$ denotes the $i^{th}$ entry of the activations in layer $l$.

As a concrete example in a Named Entity Recognition (NER) task to recognize organization names as in:



>```
Example:
Input X : Apple makes great phones 
Output y:   1      0     0     0
>```

$t$ is used to index into the input sequence. For example: $$X^{(i)<t>}$$ is used to refer to index into a specfic training example. Concretely $X^{(i)<2>}$ is used to refer to second item in the i/p sequence - in the above example:

> 
$X^{(i)<2>}$ = "makes" 
$y^{(i)<1>}$ = 1
$T_x$ = 4
$T_y$ = 4


Fianlly, words will be encoded using several notiations including one-hot encoding schemes.  
  
  
<img src="/static/media/NNBook/imgs/nnnot1.png"  style="width: 5in">

---

## Calculations
<img src="/static/media/NNBook/imgs/nncal1.png"  style="width: 5in"/>
<img src="/static/media/NNBook/imgs/nncal2.png"  style="width: 5in"/>
<img src="/static/media/NNBook/imgs/nncal3.png"  style="width: 5in"
/>
## Types of RNN
<img src="/static/media/NNBook/imgs/nntypes1.png"  style="width: 5in">

## Language modeling
Given a set of sentence, which sentence is more likely

The apple and pair salad	ex: 	P = 3.2 
The apple and pear salad		P = 5.7 <== this is more likely

## Vanishing/exploding gradient
In a much deeper NN, then the gradient is difficult to propagate up. The errors in later step to affect the weights in earlier in the layer. Therefore outputs are influenced strongly influenced by local nodes.

Vanishing gradients can cause the weights to almost becomes zero. Exploding gradients is where weights increase astronomically. Exploding gradients are easy to spot and easy to manage by gradient clipping. Vanishing does more things to do to handle.


## Gated Recurrent Unit (GRU)


<img src="/static/media/NNBook/imgs/nngru1.png"  style="width: 5in">
 
