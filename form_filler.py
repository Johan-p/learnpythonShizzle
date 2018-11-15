"""
url


"""
print(__doc__)

import requests
import os
import random
import string
import json

def var():
	for name in names:
		name_extra = "".join(random.choice(string.digits))
		username = name.lower() + name_extra + "@yahoo.com"
		password = "".join(random.choice(chars)) for i in range(8)

		#stuk string vervangen door wat er in post request meegestuurd wordt
		requests.post(url, allow_redirects=False data={
		"string" : username,
		"string" : password
		})
		print "sending username %s and password %s" % (username, password)

chars = string.ascii_letters + string.digits +"!@#$%^&*()"
random.seed = (os.urandom(1024))
url = "www.exampleurl.com/"
names = json.loads(open("names.json", "r"))

if __name__=='__main__':
	var()