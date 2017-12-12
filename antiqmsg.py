'''
carrier pigeon
morse-code
encryption


choose 3 messenger classes
1 main class
1 write to file class

'''


from message import main, writer, morser, piglatin
from numswitch import numswitch

wwmessage = input ('what is your message')
wwresult = numswitch(wwmessage)
wwresult.encode()
wwresult.decode()

x = main()

x.intake()

x.translate()

x.mitto()


