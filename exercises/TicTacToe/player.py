import math
import numpy as np
import matrixify

def play(player, computer):	
	while True:
		number = input("Which square would you like to pick? ")
		number -= 1
		x = int(math.ceil(int(number)/3))
		y = (number % 3) 
		move = matrixify.matrix([[x,y]])
		if np.multiply(move, player).sum() == 0 and np.multiply(move, computer).sum() == 0:
			p_coor = player + move
			return p_coor
		else:
			print "Pick another square!"