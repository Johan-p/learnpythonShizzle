"""
In a previous exercise we explored the idea of using a list of lists as a data structure
to store information about a tic tac toe game. In a tic tac toe game, 
the game server needs to know where the Xs and Os are in the board, 
to know whether player 1 or player 2 (or whoever is X and O won).

There has also been an exercise about drawing the actual tic tac toe gameboard 
using text characters.

The next logical step is to deal with handling user input. 
When a player (say player 1, who is X) wants to place an X on the screen, 
they can t just click on a terminal. 
So we are going to approximate this clicking simply by asking 
the user for a coordinate of where they want to place their piece.

"""
print(__doc__)

#imports

def player_1():
	global game
	global turn
	print "Player one!"
	user_input = raw_input("Row,Colomn: ")
	user_input = user_input.strip().split(",")
	row = user_input[0]
	row = int(row)
	col = user_input[1]
	col = int(col)
	game[row-1][col-1] = 1
	turn = "player_2"
	gameboard()

def player_2():
	global game
	global turn
	print "Player Two!"
	user_input = raw_input("Row,Colomn: ")
	user_input = user_input.strip().split(",")
	row = user_input[0]
	row = int(row)
	col = user_input[1]
	col = int(col)
	game[row-1][col-1] = 2
	turn = "player_1"
	gameboard()


def gameboard():
	print "-------"
	print "|" + str(game[0][0]) + "|" + str(game[0][1]) + "|" + str(game[0][2]) + "|"
	print "-------"
	print "|" + str(game[1][0]) + "|" + str(game[1][1]) + "|" + str(game[1][2]) + "|"
	print "-------"
	print "|" + str(game[2][0]) + "|" + str(game[2][1]) + "|" + str(game[2][2]) + "|"
	print "-------"
	next_player()

def next_player():
	if turn == "player_1":
		player_1()
	elif turn == "player_2":
		player_2()


game = [
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]

turn = "player_1"

if __name__=='__main__':
	gameboard()