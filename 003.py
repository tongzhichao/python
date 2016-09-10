import io 
import operator

def get_count_table(filepath='tong.txt',ignore=[',','“','.','!',':',';','?','1','2','3','4','5','6','7','8','9','0'],lower=True):
	txt = open(filepath).read()
	for i in ignore:
		txt = txt.replace(i,' ')
	if lower:
		txt = txt.lower()
	words = txt.split(' ')
	#print(list(words))
	dic = {}
	for word in words:
		if word is '':
			continue
		if word in dic:
			dic[word] += 1
		else:
			dic[word] = 1
#	print(dic.values())
	return dic
#安装字典中的第2个元素排序，并倒序显示
#key=operator.itemgetter(1)表示字典元组中的第二个数值，固定写法
#reverse=True 倒序显示，最大的在上面
#result = sorted(get_count_table().items(),key=operator.itemgetter(1),reverse=True)

#这个是我自己模拟的，a_tuple名字随意
result1 = get_count_table().items()
result = sorted(result1,key=lambda a_tuple:a_tuple[1],reverse=True)

for item in result:
	print(item[0],item[1])
