"""
In this exercise, use the bokeh Python library to plot a histogram
of which months the scientists have birthdays in!
"""
print(__doc__)

from bokeh.plotting import figure, show, output_file
from collections import Counter
import json

def read_jsonfile():
	#global birthday_dictionary
	global x
	global y
	with open("birthday.json", "r") as read_file:
		birthday_dictionary = json.load(read_file)
	
	#counting number of times months occur in each entry
	numberic_list = []
	alphabettic_list = []
	for values in birthday_dictionary.values():
		nummeric_month = values[3] + values[4]
		numberic_list.append(str(nummeric_month))
	for num in numberic_list:
		alphabettic_list.append(month_dict[num])
	c = dict(Counter(alphabettic_list))
	x = list(c.keys())
	y = list(c.values())

	# create a figure
	# To make sure bokeh draws the axis correctly,
	# you need to specify a special call to figure() to pass an x_range
	p = figure(x_range=x_categories)
	
	# create a histogram
	p.vbar(x=x, top=y, width=0.5)

	# render (show) the plot, this opens the browser
	show(p)

# we specify an HTML file where the output will go
output_file("plot.html")

x_categories = ["January","Febuary","March","April",
"May","June","July","August","September","October","November","December"]
x = []
y = []

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
	read_jsonfile()