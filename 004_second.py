import re

def count(filepath):
	f = open(filepath,'r')
	s = f.read()
	words = re.findall(r'[a-zA-Z]+',s)
	return len(words)

if __name__=='__main__':
	num = count('tong.txt')
	print(num)
