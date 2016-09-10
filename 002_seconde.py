#tong.txt的内容为三行数据
#2KEeZOg
#dp4CYqt
#mXlUyD2
import mysql.connector

def store_mysql(filepath):
	conn = mysql.connector.connect(user='root',password='1',database='test')
	cursor = conn.cursor()
	
	#判断表是否存在
	#查看test数据库的所有表	
	cursor.execute('show tables in test')
	tables = cursor.fetchall()
	print(tables)
	findtables = False
	#查看code表是否在test数据库内
	for table in tables:
		
		if 'code' in table:
			findtables = True
	#如果没在就新建code的表
	if not findtables:
	#两种方式建表
	#	cursor.execute('create table code(id INT  NOT NULL Primary KEY AUTO_INCREMENT,username VARCHAR(15) NOT NULL) AUTO_INCREMENT = 1')
		sql = """create table code ( id INT NULL primary KEY AUTO_INCREMENT,username VARCHAR(50) NOT NULL) AUTO_INCREMENT=1"""
		cursor.execute(sql)
	#打开存放激活码的文件
	f = open(filepath,'r')
	#每次读取1行数据
	for line in f.readlines():
		code = line.strip()
	#	print(code)
	#	print([code])
		cursor.execute('insert into code(username) values(%s)',[code])
	conn.commit()
	cursor.close()
	conn.close()
if __name__ == '__main__':
	store_mysql('tong.txt') 
			
