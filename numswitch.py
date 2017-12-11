import sys 

original = str(input('what is your message'))
class numswitch():
	def __init__ (self, message):
		self.message = message

	def encode(self): 
		origlist = list(original)
		listnum = []
		for i in origlist:
			listnum.append(ord(i)-97)
	def decode(self):
		backtoorig = [] 
		for i in listnum:
			backtoorig.append(chr(i+97))

 
print (listnum)
print(backtoorig)
