#4 chili exersise! :D

import requests
from bs4 import BeautifulSoup

#request code:
url = "https://www.security.nl/"
r = requests.get(url)
r_html = r.text

#soap code:
soup = BeautifulSoup(r_html, "html.parser")
#print soup.prettify()


#dev class = title is de html code referentie voor de titels van de pagina.
for title in soup.find_all(class_="title"):
	#de title.a is de <a string die na de class volgt, 
	#hier staat de daadwerkelijke title die we willen zien
	if title.a:
		print title.a.text
