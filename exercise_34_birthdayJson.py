"""
In the previous exercise we created a dictionary of famous scientists birthdays. 
In this exercise, modify your program from Part 1 to load the birthday dictionary 
from a JSON file on disk,
rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientists name and birthday to add to the dictionary, 
and update the JSON file you have on disk with the scientists name. 
If you run the program multiple times and keep adding new names, 
your JSON file should keep getting bigger and bigger.

"""
print(__doc__)

import json


#function to write the data to our file
def save_to_file():
	with open("birthday.json", 'w') as open_file:
		json.dump(save_dictionary, open_file)

#function to read our json file
def read_from_jsonfile():
	global birthday_dictionary
	with open("birthday.json", "r") as read_file:
		birthday_dictionary = json.load(read_file)

def add_to_dictionary():
	global save_dictionary
	key = str(raw_input("profide a name: "))
	value = str(raw_input("profide a date, example 31/12/1965: "))
	save_dictionary[key] = value
	#print save_dictionary
	save_to_file()

#our dictionary that will write to a json file
save_dictionary = {"Albert Einstein":"14/03/1879",
                       "Benjamin Franklin":"17/01/1706",
                       "Winston Churchill":"24/01/1965",}

#variable that will later use to store the content of our json file in
birthday_dictionary = None

if __name__=='__main__':
	print "Welcome to the birthday dictionary."
	response = str(raw_input("Do you want to add a new entry? y/n: "))
	if response == "y":
		add_to_dictionary()
	elif response == "n":
		save_to_file()
	else:
		exit()

	read_from_jsonfile()
	print "We know the birthdays of: "
	for key in birthday_dictionary.keys():
		print key
	#we now ask the user what birhtday they want to look up
	user_input = str(raw_input("Who's birthday do you want to look up? "))
	if user_input in birthday_dictionary:
		print "%s birthday is %s" % (user_input, birthday_dictionary[user_input])
	else:
		exit()