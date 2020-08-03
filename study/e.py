import re
file = open('/Users/liulin/lianxi/jiekoustudy/logs/log.txt','r+')
reader = file.read()
print(reader)
a = re.sub(r'(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',reader)
file.write(a)
file.close()