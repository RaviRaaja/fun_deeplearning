import numpy as np

#Function for initializing random weights
def init_weights():
	W = np.random.rand(1,2)
	b = 1
	return W, b

def step(z):
	return np.heaviside(z,1)

def propagate(W,b,X,Y):
	'''
	W is Weight matrix of dimension (1,2)
	X is input matrix of dimension (4,2)
	b is bias which is 1
	'''	
	A = step((np.dot(X,W.T) + b))
	Error = Y - A
	return Error

def optimize(W,b,X,Y,num_iterations, learning_rate):
	for i in range(num_iterations):
		Error = propagate(W,b,X,Y)
		#print ("Error is {} for iteration {}".format(Error, i+1))
		W = W + np.multiply(learning_rate , (np.dot(Error.T,X))) 
		b = b + np.multiply(learning_rate , Error)
	params = {"W" : W, "b" : b}
	return params

def model(X,Y,num_iterations,learning_rate):
	W, b = init_weights()
	print ("Initial W is {} and b is {}".format(W,b))
	params = optimize(W,b,X,Y,num_iterations, learning_rate)
	print ("Final updated W and b are")
	print ("W is" ,params["W"])
	print ("b is ",params["b"])
	return params  

def validation(X,params):
	W = params["W"]
	b = params["b"]
	A = step((np.dot(X,W.T) + b))
	return  A

def main():
	X = np.array([[0,0],[0,1],[1,0],[1,1]])
	Y_XOR = np.array([0,1,1,0]).reshape((4,1))
	params = model(X,Y_XOR,100,0.1)
	print ("X is input {} \n corresponding Y as output {}".format(X,validation(X,params)))


main()





