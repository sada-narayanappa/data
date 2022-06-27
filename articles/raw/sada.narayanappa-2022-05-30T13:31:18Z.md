# Introduction to the Jacobian
####  Jacobian matrix or its determinant.

---

In the literature, the term Jacobian is often interchangeably used to refer to both the Jacobian matrix or its determinant. 

Both the matrix and the determinant have useful and important applications: in machine learning, the Jacobian matrix aggregates the partial derivatives that are necessary for backpropagation; the determinant is useful in the process of changing between variables.

In this tutorial, you will review a gentle introduction to the Jacobian. 

After completing this tutorial, you will know:

* The Jacobian matrix collects all first-order partial derivatives of a multivariate function that can be used for backpropagation.
* The Jacobian determinant is useful in changing between variables, where it acts as a scaling factor between one coordinate space and another. 

---

<div class="alert alert-success">
<strong>Tip:</strong> Dont be afraid of too many math symbols and few will give up.
</div>

Partial Derivatives in Machine Learning
We have thus far mentioned gradients and partial derivatives as being important for an optimization algorithm to update, say, the model weights of a neural network to reach an optimal set of weights. The use of partial derivatives permits each weight to be updated independently of the others, by calculating the gradient of the error curve with respect to each weight in turn.

Many of the functions that we usually work with in machine learning are multivariate, vector-valued functions, which means that they map multiple real inputs, n,  to multiple real outputs, m:



For example, consider a neural network that classifies grayscale images into several classes. The function being implemented by such a classifier would map the n pixel values of each single-channel input image, to m output probabilities of belonging to each of the different classes. 

In training a neural network, the backpropagation algorithm is responsible for sharing back the error calculated at the output layer, among the neurons comprising the different hidden layers of the neural network, until it reaches the input. 

> The fundamental principle of the backpropagation algorithm in adjusting the weights in a network is that each weight in a network should be updated in proportion to the sensitivity of the overall error of the network to changes in that weight. 

This sensitivity of the overall error of the network to changes in any one particular weight is measured in terms of the rate of change, which, in turn, is calculated by taking the partial derivative of the error with respect to the same weight. 

For simplicity, suppose that one of the hidden layers of some particular network consists of just a single neuron, k. We can represent this in terms of a simple computational graph:

 

‣

            