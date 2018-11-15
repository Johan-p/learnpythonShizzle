"""
In the previous exercise we saved information about famous scientists names and birthdays to disk.
In this exercise, load that JSON file from disk, 
extract the months of all the birthdays, 
and count how many scientists have a birthday in each month.

"""
print(__doc__)

from collections import Counter
import json


def read_from_jsonfile():
	global birthday_dictionary
	with open("birthday.json", "r") as read_file:
		birthday_dictionary = json.load(read_file)

def var():
	pass


month_dict = {"01":"January",
			  "02":"Febuary",
			  "03":"March",
			  "04":"April",
			  "05":"May",
			  "06":"June",
			  "07":"July",
			  "08":"August",
			  "09":"September",
			  "10":"October",
			  "11":"November",
			  "12":"December"}

if __name__=='__main__':
	read_from_jsonfile()
	numberic_list = []
	alphabettic_list = []
	for values in birthday_dictionary.values():
		nummeric_month = values[3] + values[4]
		numberic_list.append(str(nummeric_month))
	for x in numberic_list:
		alphabettic_list.append(month_dict[x])
	#print numberic_list
	#print alphabettic_list
	c = Counter(alphabettic_list)
	print c