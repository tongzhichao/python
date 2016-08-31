import uuid

def create_code(number=200):
	result = []
	while True is True:
		temp = str(uuid.uuid1()).replace('-','')
		if not temp in result:
			result.append(temp)
		if len(result) is number:
			break
	return result
s = create_code()
print(s)
