import requests,sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import hosts

class List(object):
	url = hosts.testuri['mt06'] + 'api/v2/wd/info/fengChuListV2'
	res = requests.get(url)
	resp = res.json()
	#print(res.status_code)

	def get_id(self,res,resp):
		id = {}
		#print(len(resp['data']['targets']))
		for i in range(len(resp['data']['targets'])):
			res = requests.get(self.url)
			resp = res.json()
			id[i] = resp['data']['targets'][i]['id']
		print(id)
		return id

if __name__ == '__main__':
	obj = List()
	id = obj.get_id(obj.res,obj.resp)