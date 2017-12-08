morse = {'a' : '* -  ', 'b' : '- * * *  ', 'c' : '- * - *  ', 'd' : '- * *  ', 
'e' : '*  ', 'f' : '* * - *  ', 'g' : '- - *  ', 'h' : '* * * *  ', 'i' : '* *  ',
'j' : '* - - -  ', 'k' : '- * -  ', 'l' : '* - * *  ', 'm' : '- -  ', 'n' : '- *  ', 
'o' : '- - -  ', 'p' : '* - - *  ', 'q' : '- - * -  ','r' : '* - *  ', 's' : '* * *  ', 
't' : '-  ', 'u' :'* * - -  ', 'v' :'* * * -  ', 'w' : '* - -  ', 'x' : '- * * -  ',
'y' :'- * - -  ', 'z' : '- - * *  ', ' ' : ' '}




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
		for i in range(len(self.info)):
			if (i + 1)%12 == 0:
				self.output += morse[self.info[i]]
				self.output += '\n'
			else:
				self.output += morse[self.info[i]]


