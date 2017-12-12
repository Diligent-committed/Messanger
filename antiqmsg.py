from message import main, writer, morser, piglatin, cypher decode




from message import main, writer, morser, piglatin, cypher

x = main()

x.intake()

x.translate()

x.mitto()



x = input('What would you like to decode? ')
if not x.isalpha():
	m = decode(x)
	m.run()
	print(m.output)