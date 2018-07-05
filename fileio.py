# read file

f = open('/home/zk/a.txt','r')
print(f.read().strip())
f.close()

# each io operation should close file
try:
	f = open('/home/zk/a.txt','r')
	print(f.read().strip())
finally:
	if f:
		f.close()


# using with ... as to avoid invoking close everytime  

with open('/home/zk/a.txt','r') as m:
	for line in m.readlines():
		print(line.strip())

# file - like Object