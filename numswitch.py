import sys 
# At first I tried to do this with lists of alphabetic values, but eventuaally i found a much simpler and more efficient way to do this 
# By using the functions ord and chr. In the end once I figured out how to work these functions it was a pretty simple tak of putting 
#them in for loops and then tinkering with them until i got the result i wanted (Of course this was simple but time consuming)
#lastly I took all of my code and put it in class format and that seemed to work well and made my main code into functions which was 
#not difficult and i was able to do it succesfully. Some difficulties I had were i was trying to do this task with two lists instead 
# of making empyty lists that i append and then reuse. 
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

 

