#此题有两种写法，其中一种借鉴别人的，快速实现

import random,string
#定义函数，需要激活码的格式和长度
def rand_str(num,length=7):
	#打开一个文件，准备存放激活码
	f = open('tong.txt','w')
	s = []
#循环生成多少个激活码
	for i in range(num):
		#string.ascii_letters代表固定的字符(大小写字母)
		#string.digits代表固定的数值(0123456789)
		#拼接成新的长串chars
		chars = string.ascii_letters + string.digits
		#每次随即找出一个字符，并循环length次
	#	s = [random.choice(chars) for i in range(length)]
		#写入文件
	#	f.write(''.join(s)+'\n')
		#循环length次，每次都追加到列表s里	
		for m in range(length):
			r = random.choice(chars)
			s.append(r)
		print(s)
		#将列表里的数值写入文件
		for i in s:
			f.write(i)
		#输完为一行
		f.write('\n')
		#记得清空列表S，不然会一直追加
		s.clear()	
		
	f.close()

if __name__ == '__main__':
	rand_str(3)


