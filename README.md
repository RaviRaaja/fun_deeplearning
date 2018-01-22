# Artificial Intelligence Basics

# Contents in this repo
This repo contains fun and basic projects to play with deep learning concepts, containing experiments like 
* [code_link](https://github.com/RaviRaaja/fun_deeplearning/blob/master/AND_OR_XOR_perceptron.py) Implementation of logic gates like AND, OR, XOR(proving that xor is not linearly seperable) using single perceptron and activation function as Unit step function.
* [code_link](https://github.com/RaviRaaja/fun_deeplearning/blob/master/IRIS_perceptron.ipynb) Implementation of perceptron learning rule for planar seperation , dataset used is IRIS. This experiments shows that perceptron with step activation function will not give perfect seperation line like linear SVM does.
* [code_link](https://github.com/RaviRaaja/fun_deeplearning/blob/master/Logic_gates_using_keras_sigmoid.ipynb) Implementation of logic gates using sigmoid activation function using keras.
* [code_link](https://github.com/RaviRaaja/fun_deeplearning/blob/master/MNIST_Adaline_with_single_perceptron.ipynb) Implementation of ADALINE with MNIST dataset for classifying hand written 0's and other numbers similar to 0's.
* [code_link](https://github.com/RaviRaaja/fun_deeplearning/blob/master/MNIST_using_single_perceptron_UNIT_STEP_Function.ipynb) Implementation of Perceptron with UNIT_STEP function for classifying hand written 0's and other numbers similar to 0's.
* [code_Link](https://github.com/RaviRaaja/fun_deeplearning/blob/master/Mnist_sigmoid_1perceptron_SSE.ipynb) Implementation of single perceptron for classification problem on same previously used dataset with cost as sum of squared errors.
* [code_link](https://github.com/RaviRaaja/fun_deeplearning/blob/master/Mnist_2layer_sigmoid_SSE.ipynb) Implementaion of 2 layered Neural network with sigmoid as activation function with SSE as cost function. Number of nodes in hidden layer is 2.
* [code_link](https://github.com/RaviRaaja/fun_deeplearning/blob/master/Mnist_2layer_sigmoid_logloss.ipynb) Implementation and cross validation of MNIST classification using 2 layered neural network with sigmoid activation in both layers(hidden and output) and loss function as cross entrophy. (logistic loss)

# Dataset 
MNIST dataset is hand crafted for this experiments, dataset is divided into 2 classes,
* [class_0](https://drive.google.com/drive/folders/1qCDIBMvN-P9icQQM7huCt0_EOaLpZjsJ?usp=sharing) - Contains hand written 0's
* [class_1](https://drive.google.com/drive/folders/1fj2G5SnfQsRyKyVQ8U5XLPrjzmZp-H82?usp=sharing) - Contains hand written 2's 3's 6's 9's 5's
* Download dataset and extract in parent folder where jupyter notebook is located. (put dataset in parent working directory).

# Note
Experiments above were implemented using python2 and python3 , implementaion of numpy exp function may result in cost as NaN, in such cases update your packages or try with other version of python.




