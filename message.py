'''
This program allows for translation into morse code, pig latin, and 
a numeric cypher. The code to reverse the translation is also provided 
for morse code and the numeric cypher, although reversing pig latin
is not included as it is far beyond the scope of this project. 

- Will & Will

'''

#These two blocks are dictionaries for the morse code process
morse = {'a' : '* -  ', 'b' : '- * * *  ', 'c' : '- * - *  ', 'd' : '- * *  ', 
'e' : '*  ', 'f' : '* * - *  ', 'g' : '- - *  ', 'h' : '* * * *  ', 'i' : '* *  ',
'j' : '* - - -  ', 'k' : '- * -  ', 'l' : '* - * *  ', 'm' : '- -  ', 'n' : '- *  ', 
'o' : '- - -  ', 'p' : '* - - *  ', 'q' : '- - * -  ','r' : '* - *  ', 's' : '* * *  ', 
't' : '-  ', 'u' :'* * - -  ', 'v' :'* * * -  ', 'w' : '* - -  ', 'x' : '- * * -  ',
'y' :'- * - -  ', 'z' : '- - * *  ', ' ' : ' ', '.' : ' * * *  -  - - -  * - - *  '}

revmorse = {'* - ' : 'a', '- * * * ' : 'b', '- * - * ' : 'c', '- * * ' : 'd',
'* ' : 'e', '* * - * ' : 'f', '- - * ' : 'g', '* * * * ' : 'h', '* * ' : 'i',
'* - - - ' : 'j', '- * - ' : 'k', '* - * * ' : 'l', '- - ' : 'm', '- * ' : 'n',
'- - - ' : 'o', '* - - * ' : 'p', '- - * - ' : 'q', '* - * ' : 'r', '* * * ' : 's',
'- ' : 't', '* * - - ' : 'u', '* * * - ' : 'v', '* - - ' : 'w', '- * * - ' : 'x',
'- * - - ' : 'y', '- - * * ' : 'z', ' ' : ' '}


#The program functions with one main class that manages all other 
#work. The script to run it is four lines long. 

class main: #main class
	def __init__(self): #takes inputs for message and type to translate into
		print('Hello')
	def intake(self):
		x = input('What would you like to send? ').casefold()
		self.message = x
		x = input('How would you like to send it? ').casefold()
		self.gens = x

	def translate(self): #based on type of translation, inits one of 3 classes
		if self.gens == 'morse':
			self.secondary = morser(self.message)
			self.secondary.convert()
		elif self.gens == 'piglatin':
			self.secondary = piglatin(self.message)
			self.secondary.convert()
		elif self.gens == 'cypher':
			self.secondary = cypher(self.message)
			self.secondary.convert()

	def mitto(self): #This function 'sends' the result of the translation, writing it to the file 'writeto'
		self.loca = writer('IncomingMessage')
		self.loca.send(self.secondary.output)



class writer: #This class handles writing the output
	def __init__(self, location):
		self.location = location

	def send(self, info): #This function writes the output
		f = open(self.location, 'w')
		f.write(info)
		f.close()

	def recieve(self): #this function could be used to read, but isn't used in this code.
		f = open(self.location)
		print(f.read())
		f.close()

class morser: #This class allows for conversion into morse code.
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

# At first I tried to do this with lists of alphabetic values, but eventuaally i found a much simpler and more efficient way to do this 
# By using the functions ord and chr. In the end once I figured out how to work these functions it was a pretty simple tak of putting 
#them in for loops and then tinkering with them until i got the result i wanted (Of course this was simple but time consuming)
#lastly I took all of my code and put it in class format and that seemed to work well and made my main code into functions which was 
#not difficult and i was able to do it succesfully. Some difficulties I had were i was trying to do this task with two lists instead 
# of making empyty lists that i append and then reuse. 
class cypher(): #This class allows for conversion into the numeric cypher
	def __init__ (self, message):
		self.message = message

	def convert(self): 
		self.inter = list(self.message)
		self.output = ''
		for i in self.inter:
			self.output += (str((ord(i)-97)) + ' ')

class piglatin: #This class converts into piglatin
	def __init__(self, info):
		self.info = info.casefold()
		self.output = ''

	def convert(self):
		word = ''
		inter = ''
		for i in range(len(self.info)):
			if self.info[i] == ' ':
				if word != '':
					if word[0] not in 'aeiouy':
						for i in range(1,len(word)):
							inter += word[i]
						inter += word[0]
						inter += 'ay '
					else:
						inter = word
						inter += 'ay '
					self.output += inter
				inter = ''
				word = ''
			elif self.info[i] == '.':
				if word[0] not in 'aeiouy':
					for i in range(1,len(word)):
						inter += word[i]
					inter += word[0]
					inter += 'ay. '
				else:
					inter = word
					inter += 'ay. '
				self.output += inter
				inter = ''
				word = ''
			elif self.info[i] != ' ':
				word += self.info[i]
		if word != '':
			if word[0] not in 'aeiouy':
				for i in range(1,len(word)):
					inter += word[i]
				inter += word[0]
				inter += 'ay '
			else:
				inter = word
				inter += 'ay '
			self.output += inter
			inter = ''
			word = ''

class decode: #This class decodes an input. 
	def __init__(self, info):
		self.info = info
		self.output = ''

	def run(self): #If the input's firts char is a morse char, it runs morse decoding. if its first char is a letter, it runs piglatin decoding. if the first char is a number, it runs cypher decoding.
		x = self.info[0]
		if x in ['*', '-']:
			self.unmorse()
		elif x.isalpha():
			self.unpiglatin()
		elif x.isnumeric():
			self.uncypher()

	def unmorse(self): #Runs input throught the reverse morse dictionary
		inter = 'X'
		letter = ''
		for char in self.info:
			if char != ' ':
				inter += char
			elif char == ' ' and inter[-1] == 'X':
				self.output += ' '
			elif char == ' ' and inter[-1] != ' ':
				inter += char
			elif char == ' ' and inter[-1] == ' ':
				for i in range(1,len(inter)):
					letter += inter[i]
				self.output += revmorse[letter]
				inter = 'X'
				letter = ''

	def unpiglatin(self): #Pig latin is very complex to decode in a program, and as a result while some conceptual work was done, no code was ever written.
		print('Error. Piglatin is unnable to be decoded at this time.')

	def uncypher(self): #Runs input through the chr function. 
		inter = ''
		for i in self.info:
			if i != ' ':
				inter += i
			else:
				inter = int(inter)
				self.output += (chr(inter+97))
				inter = ''

