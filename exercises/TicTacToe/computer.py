import numpy as np
import matrixify
from itertools import combinations

magicSquare = np.array([
	[4,9,2],
    [3,5,7],
    [8,1,6]
])

def play(player, computer):
	moves = np.concatenate((center(), corners()))
	moves = np.concatenate((moves, edges()))

	if computer.sum() >= 2:
		combos = combinations(np.argwhere(computer == 1), 2)
		for combo in combos:
			mat = matrixify.matrix(combo)
			idx = 15 - np.multiply(magicSquare, mat).sum()
			nec = matrixify.matrix(np.argwhere(magicSquare == idx))
			if np.multiply(nec, player).sum() == 0:
				c_coor = computer + nec
				return c_coor

	for move in moves:
		if np.multiply(move, player).sum() == 0 and np.multiply(move, computer).sum() == 0:
			c_coor = computer + move
			return c_coor

	return computer

def center():
	return matrixify.coors([[1,1]])

def corners():
	return matrixify.coors([[0,0],[0,2],[2,0],[2,2]])

def edges():
	return matrixify.coors([[1,0],[0,1],[2,1],[1,2]])