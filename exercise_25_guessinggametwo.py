"""
In a previous exercise, 
we ve written a program that knows a number and asks a user to guess it.

This time, we re going to do exactly the opposite. 
You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you, 
the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took
to get your number.

As the writer of this program, 
you will have to choose how your program will strategically guess. 
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) 
until you hit the number. 
But that s not an optimal guessing strategy. 
An alternate strategy might be to guess 50 (right in the middle of the range), 
and then increase  decrease by 1 as needed. After you ve written the program, 
try to find the optimal strategy! 
(We ll talk about what is the optimal one next week with the solution.)

"""
print(__doc__)

#import random

def game():
	number = 50
	attempts = 0
	playing = False

	print "Is the number %s?" % (number)
	response = str(raw_input("lower, higher, correct: "))
	if response == "higher":
		number = number + 25
		attempts = attempts +1
		playing = True
	elif response == "lower":
		number = number - 25
		attempts = attempts +1
		playing = True
	elif response == "correct":
		print "Yes I guessed it in %s attempts" % (attempts)
	else:
		print "?"
		exit()
	
	while playing:
		print "Is the number %s?" % (number)
		response = str(raw_input("lower, higher, correct: "))
		if response == "higher":
			number = number + 1
			attempts = attempts + 1
		elif response == "lower":
			number = number -1
			attempts = attempts +1
		elif response == "correct":
			print "Yes I guessed it in %s attempts" % (attempts)
			playing = False
		else:
			exit()




if __name__=='__main__':
	print "instructions"
	number_list = range(0,100 +1)
	game()