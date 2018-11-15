import random

"""
We ask the user for a 4 digit number as input, this can include 0's as such we use the raw_input.
raw_input creates a string type.
input creates a integer, integers lose there 0's if they change type.
Since we use a list to compare we use the raw_input so we don't lose our 0's in the front.
"""


def set_difficulty():
	difficulty = raw_input("please set the difficulty; easy, medium or hard: ")
	
	global pins
	global lenght
	if difficulty == "easy":
		pins = 5 # 0 t/m 5 (6 pins)
		lenght = 4
	elif difficulty == "medium":
		pins = 7 # 0 t/m 7 (8 pins)
		lenght = 4
	elif difficulty == "hard":
		pins = 7 # 0 t/m 9 (8 pins)
		lenght = 6
	else:
		set_difficulty()


def game_turn():
	user_guess = raw_input("Guess the digit number: ")
	user_guess = list(str(user_guess))
	if lenght == 4 and len(user_guess) != 4:
		print "please provide a 4 digit number!"
		game_turn()
	elif lenght == 6 and len(user_guess) != 6:
		print "please provide a 6 digit number!"
		game_turn()
	else:
		print user_guess
		result = user_guess
		for x in range(0,lenght):
			if user_guess[x] == number_random[x]:
				result[x] = "Cow"
			else:
				result[x] = "Bull"
	print result




if __name__ == "__main__":
	pins = 4
	lenght = 3
	#intro text
	print "lets play Mastermind!"
	print "I'll create a number and you will have to guess it"
	print "Hit will indicate a number on the right position"
	print "Close will indicate a number thats correct but not on right position"
	print "Miss is an incorrect number"
	print "--------------------------------"

	#asking the user for the difficulty
	set_difficulty()
	#returning the difficulty to the user
	print "I'll create a %s digit number from 0 to %s" % (lenght, pins)
	
	#generating the random number
	number_random = random.sample(range(0,pins +1),lenght)
	for x in range(0, lenght):
		number_random[x] = str(number_random[x])
	print number_random
	#asking the user for there guess
	game_turn()