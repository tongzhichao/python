import mysql.connector
import uuid
def create_code(number=3):
	result = []
	while True:
		temp = str(uuid.uuid1()).replace('-','')
		if not temp in result:
			result.append(temp)
		if len(result) is number:
			break
	return result

def listt(number = 3):
        result = []
        s = 0
        while s < number:
                result.append(str(s))
                s=s+1
        return result
#200个自动生成的uuid码
s = create_code()
print(s)
#200个序列号
s2 = listt()
print(s2)
#组成列表
s3 = list(zip(s2,s))
print(s3)



#连接数据库
conn = mysql.connector.connect(user='root',password='1',database='test')
cursor = conn.cursor()
#创建表
cursor.execute('create table user (id varchar(50), name varchar(100))')
#插入数据，注意多条是many
cursor.executemany('insert into user values(%s,%s)',s3)
#提交
conn.commit()
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

