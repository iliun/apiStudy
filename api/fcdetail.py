import os
import sys
import pytest
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
print(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from api.fclist import List
from config	import hosts

# class Detail():
# 	ids = List.get_id(List,List.res,List.resp)
# 	id = ids[0]
# 	url = hosts.testuri['mt06'] + 'api/v2/fixed/info/detail'
# 	params = {
# 		"version":"2.0",
# 		"type":"fengChu",
# 		"id":id,
# 		"userId":"EFDBFA9F-C8B0-499C-AE67-45FD7608858B"
# 	}
# 	res = requests.get(url,params=params)
# 	resp = res.json()
class Detail():
	def get_detail_requests(self):
		ids = List.get_id(List,List.res,List.resp)
		id = ids[0]
		url = hosts.testuri['mt06'] + 'api/v2/fixed/info/detail'
		params = {
			"version":"2.0",
			"type":"fengChu",
			"id":id,
			"userId":"EFDBFA9F-C8B0-499C-AE67-45FD7608858B"
		}
		res = requests.get(url,params=params)
		resp = res.json()
		return res,resp

if __name__ == '__main__':
	obj = Detail()
