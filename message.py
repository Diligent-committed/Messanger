morse = {'a' : '* -  ', 'b' : '- * * *  ', 'c' : '- * - *  ', 'd' : '- * *  ', 
'e' : '*  ', 'f' : '* * - *  ', 'g' : '- - *  ', 'h' : '* * * *  ', 'i' : '* *  ',
'j' : '* - - -  ', 'k' : '- * -  ', 'l' : '* - * *  ', 'm' : '- -  ', 'n' : '- *  ', 
'o' : '- - -  ', 'p' : '* - - *  ', 'q' : '- - * -  ','r' : '* - *  ', 's' : '* * *  ', 
't' : '-  ', 'u' :'* * - -  ', 'v' :'* * * -  ', 'w' : '* - -  ', 'x' : '- * * -  ',
'y' :'- * - -  ', 'z' : '- - * *  ', ' ' : ' ', '.' : '* * *  -  - - -  * - - *  '}


class main:
	def __init__(self):
		print('Hello')
	def intake(self):
		x = input('What would you like to send? ').casefold()
		self.message = x
		x = input('How would you like to send it? ').casefold()
		self.gens = x

	def translate(self):
		if self.gens == 'morse':
			self.secondary = morser(self.message)
			self.secondary.convert()
		elif self.gens == 'cypher':
			self.secondary = cypher(self.message)
			self.secondary.convert()

	def mitto(self):
		self.loca = writer('writeto')
		self.loca.send(self.secondary.output)



class writer:
	def __init__(self, location):
		self.location = location

	def send(self, info):
		f = open(self.location, 'w')
		f.write(info)
		f.close()

	def recieve(self):
		f = open(self.location)
		print(f.read())
		f.close()

class morser:
	def __init__(self, info):
		self.info = info.casefold()
		self.output = ''

	def convert(self):
		recent = 0
		for i in range(len(self.info)):
			self.output += morse[self.info[i]]
			if len(self.output) - recent > 60:
				self.output += '\n'
				recent = len(self.output)


