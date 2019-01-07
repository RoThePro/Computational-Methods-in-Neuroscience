import check
import cli
import player
import computer
import numpy as np

game = False
p_coor = np.zeros((3,3))
c_coor = np.zeros((3,3))

cli.intro()
while not game:
	c_coor = computer.play(p_coor, c_coor)
	cli.render(p_coor, c_coor)
	if check.check(c_coor):
		game = True
		print "Computer wins"
		break
	p_coor = player.play(p_coor, c_coor)
	if check.check(p_coor):
		game = True
		print "Player wins"
	