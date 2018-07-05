from io import StringIO

f=StringIO('hello!\nHi!\n\nGoodbye!')
while(True):
	s = f.readline()
	if s=='':
		break
	print(s)

