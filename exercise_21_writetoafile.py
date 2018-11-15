"""
Take the code from the How To Decode A Website exercise 
Instead of printing the results to a screen, write the results to a txt file. 
In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.

"""
print(__doc__)


import requests
from bs4 import BeautifulSoup


def get_titles():
	name = str(raw_input("Please profide a filename: "))
	filename = str(name) + ".txt"
	print filename
	url = "https://www.security.nl/"
	r = requests.get(url)
	r_html = r.text
	soup = BeautifulSoup(r_html, "html.parser")
	with open(filename, 'w') as open_file:
		for title in soup.find_all(class_="title"):
			if title.a:
				open_file.write(title.a.text.encode("utf-8"))
			else:
				open_file.write(title.contents[0].encode("utf-8"))


if __name__=='__main__':
	get_titles()


	#replace("\n", " ")