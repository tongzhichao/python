#redis操作不熟，没深入研究过
#http://blog.csdn.net/love__coder/article/details/8293225

import redis

def store_redis(filepath):
	#连接redis
	r = redis.StrictRedis(host='localhost',port = 6379,db =0)
	f = open(filepath,'r')
	for line in f.readlines():
		code = line.strip()
		#新增到redis
		r.lpush('code',code)

if __name__ == '__main__':
	store_redis('tong.txt')
