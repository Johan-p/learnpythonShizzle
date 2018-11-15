import random


class PwdGen(object):

	def strenght(self):
		print "starting password generator"
		print "..........................."
		strenght = str(raw_input("Do you want a strong, weak or easy password? "))
		if strenght == "strong" or strenght == "Strong":
			self.strong()
		elif strenght == "weak" or strenght == "Weak":
			self.weak()
		elif strenght == "easy" or strenght == "Easy":
			self.easy()
		else:
			self.strenght()

	def strong(self):
		lenght = int(raw_input("how long should the password be?"))
		gen = [1,2,3,4,5,6,7,8,9,0,
			"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
			"s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J",
			"K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", "!", "@",
			"#", "$", "%", "^", "&", "*", "(", ")", "-", "+","/","<",">","?","[","]","|"]

		if lenght < 24:
			print "A strong password should atleast be 24 characters long"
			self.createpassword(gen, 24)
		elif lenght > 81:
			print "maxium lenght is 81"
			self.createpassword(gen,81)
		else:
			self.createpassword(gen, lenght)
	
	def weak(self):
		gen = ["a","b","c","d","e","f","g","h","i","j","k",
		"l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		self.createpassword(gen, 8)
	
	def easy(self):
		gen = ["password", "welcome123", "admin", "toor", "root", "pwd"]
		self.createpassword(gen,1)

	def createpassword(self,x,y):
		pwd = random.sample(x,y)
		password = ""
		for p in pwd:
			password = password + str(p)
		print "Your Password is:"
		print password

passwordgen = PwdGen()
passwordgen.strenght()