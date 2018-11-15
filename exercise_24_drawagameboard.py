"""
Time for some fake graphics! Lets say we want to draw game boards
Ask the user what size game board they want to draw, 
and draw it for them to the screen using Pythons print statement.
"""
print(__doc__)


def tic_tac_toe():
	a = '---'.join('    ')
	b = '   '.join('||||')
	print('\n'.join((a, b, a, b, a, b, a)))

def chess():
	a = '---'.join('         ')
	b = '   '.join('|||||||||')
	print('\n'.join((a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a)))	

def go():
	a = '---'.join('                    ')
	b = '   '.join('||||||||||||||||||||')
	print('\n'.join((a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a,b,a)))

def user_choice():
	board_choice = str(raw_input("TicTacToe, Chess or Go: "))
	if board_choice == "TicTacToe":
		tic_tac_toe()
	elif board_choice == "Chess":
		chess()
	elif board_choice == "Go":
		go()
	else:
		user_choice()


if __name__=='__main__':
	user_choice()