import numpy as np
import numpy.core.defchararray as char

def render(player, comp):
	c_coor = np.chararray((3, 3))
	c_coor[:] = "X"
	p_coor = np.chararray((3, 3))
	p_coor[:] = "O"
	print char.add(char.multiply(c_coor, comp.astype(int)), char.multiply(p_coor, player.astype(int)))
def intro():
	print "Welcome to the game of Computer Tic Tac Toe!!!!"
	print "Use this numbering system when inputing your move. \n"

	spaces = ["1","2","3","4","5","6","7","8","9"]
	print("{0} | {1} | {2}".format(spaces[0],spaces[1],spaces[2]))
	print("---------")
	print("{0} | {1} | {2}".format(spaces[3],spaces[4],spaces[5]))
	print("---------")
	print("{0} | {1} | {2}".format(spaces[6],spaces[7],spaces[8]))
	print "\n\n"