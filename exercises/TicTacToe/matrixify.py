import numpy as np

def matrix(array):
	x = np.zeros((3,3))
	for coor in array:
		x[coor[0]][coor[1]] = 1
	return x

def coors(array):
	y = []
	for coor in array:
		x = np.zeros((3,3))
		x[coor[0]][coor[1]] = 1
		y.append(x)
	np.random.shuffle(y)
	return y