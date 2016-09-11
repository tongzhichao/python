import re
import operator
def count(filepath):
	f = open(filepath,'r')
	s = f.read()
	words = re.findall(r'[a-zA-Z]+',s)
	dic={}
	print(words)
	
	for word in words:
		if word is '':
			continue
		if word in dic:
			dic[word] +=1
		else:
			dic[word] = 1 
			
	return dic
if __name__=='__main__':
	num = count('tong.txt')
	result = sorted(num.items(),key=operator.itemgetter(1),reverse=True)
	print(result)
	for item in result:
		print("单词\'%s\'的个数是%s" % (item[0],item[1]))
	print("单词总数为:%s" % len(num.items()))

