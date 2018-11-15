'''
Wanna play a game?

The program should do the following:

Roll a pair of dice.
Add the values of the roll.
Ask the user to guess a number.
Compare the user's guess to the total value.
Determine the winner (user or computer).
Let's begin!
'''

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "the maximum possible value is %d" % (max_val)
  guess = get_user_guess() 
  if guess > max_val:
    print "No guessing higher than the maximum possible value!"
  else:
    print "Rolling..."
    sleep(2)
    print "The first dice roll is: %d " % (first_roll)
    print "The second dice roll is: %d " % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "You Won!"
    else:
      print "You lose!"
roll_dice(6)