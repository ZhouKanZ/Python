# file and dir operations
import os

# Q:A dir-l which list all file and dir in current dir

def dir_l(path):
	p = [x for x in os.listdir(path)]
	print(p)

dir_l('.')	

# Q:B find current dir and all child dir to match a earmark str and print realPath
def find(regex):
	m = [x for x in os.listdir('.') if os.path.isfile(x) and regex in x]
	print(m)

find('md')

	

