import os
def test(path):
	all = []
	list1 = os.listdir(path)
	for i in list1:
		p1 = os.path.join(path,i)
		if '.py' in p1 :
			all.append(p1)
		if os.path.isdir(p1):
			test(p1)
	return all

p = '/Users/liulin/lianxi/test'

print(test(p))
