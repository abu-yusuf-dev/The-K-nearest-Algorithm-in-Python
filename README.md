# The-K-nearest-Algorithm-in-Python
My Implementation of k nearest algorithm in Python 

In pattern recognition, the k-nearest neighbors algorithm (k-NN) is a non-parametric method used for classification and regression.[1] In both cases, the input consists of the k closest training examples in the feature space. The output depends on whether k-NN is used for classification or regression:

In k-NN classification, the output is a class membership. An object is classified by a majority vote of its neighbors, with the object being assigned to the class most common among its k nearest neighbors (k is a positive integer, typically small). If k = 1, then the object is simply assigned to the class of that single nearest neighbor.
In k-NN regression, the output is the property value for the object. This value is the average of the values of its k nearest neighbors.
k-NN is a type of instance-based learning, or lazy learning, where the function is only approximated locally and all computation is deferred until classification. The k-NN algorithm is among the simplest of all machine learning algorithms.

Both for classification and regression, a useful technique can be to assign weight to the contributions of the neighbors, so that the nearer neighbors contribute more to the average than the more distant ones. For example, a common weighting scheme consists in giving each neighbor a weight of 1/d, where d is the distance to the neighbor.

The neighbors are taken from a set of objects for which the class (for k-NN classification) or the object property value (for k-NN regression) is known. This can be thought of as the training set for the algorithm, though no explicit training step is required.

A peculiarity of the k-NN algorithm is that it is sensitive to the local structure of the data.The algorithm is not to be confused with k-means, another popular machine learning technique.

The Program output is like this: 

<code>
  
The Euclidien Distance: [2, 4, 5, 5, 7, 7, 1, 9, 10, 11, 12, 13, 15, 16, 16, 17, 18, 19, 20, 22]
  
Sorted Output List:     [1, 2, 4, 5, 5, 7, 7, 9, 10, 11, 12, 13, 15, 16, 16, 17, 18, 19, 20, 22]

The Ranking List:       [0, 1, 2, 3, 3, 5, 5, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16, 17, 18, 19]

The final Ranking:      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

The Class Label: ['Bad', 'Bad', 'Bad', 'Good', 'Good', 'Good', 'Good', 'Bad', 'Good', 'Bad', 'Good', 'Bad', 'Bad', 'Bad', 'Bad', 'Bad', 'Good', 'Good', 'Bad', 'Bad']

Please Enter the K: 5 

['Bad', 'Bad', 'Bad', 'Good', 'Good']

The Prediction is :Bad 

</code>
