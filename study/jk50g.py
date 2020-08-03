import requests
import random
import hosts
import pytest
'''
#1.智能资讯，模块刷新,get方法判断status——code后判断data中是否有数据
url = hosts.prouri['passport'] + '/fengInfo/api/v2/common/getListAll'
params = {
	"version":"2.0",
	"user_id":"5E8B240B-45A6-4F22-86CC-90EC970E0515",
	"page_size":"9",
	"category_type":"9",
	"glide_type":"init"
	}
# headers = {
# 	'Authorization':'Bearer ctnD1hZeMJfHM3QGFP0NWXbxOeQCwhSKKoyXjnEsr3ywgrepDtWMAU47gs83SDM0'
# 	}

res= requests.get(url,params=params)
resp = res.json()
print(res.status_code)
#判断返回状态码
try:
	assert res.status_code == 200
except:
	print('status_code error!!')
#判断参数是否存在
try :
	assert 'success' in resp
except:
	print('success not in resp!!')
#判断类型是否正确
try:
	assert type(resp['data']) == dict
except:
	print('type error!!')

print(resp['data']['downList'][0])
try:
 	assert resp['data']['downList'][0] != None
except:
 	print('no data!!')
print('**'*random.randint(10,15))


#2.订阅管理页面 get,获取订阅列表
url = "https://passport.fengjr.com/fengInfo/api/v2/common/getUserSubscription/MYSELF"

params = {"version":"2.0"}

headers = {
    'Authorization': "Bearer ctnD1hZeMJfHM3QGFP0NWXbxOeQCwhSKKoyXjnEsr3ywgrepDtWMAU47gs83SDM0"
    }

res = requests.get(url, headers=headers, params=params)
resp = res.json()
try:
	assert res.status_code == 200
except:
	print('status_code error')

try:
	assert resp['success']== True
except:
	print('success is false')

try:
	assert resp['data']['content'] != None
except:
	print('data is null')


print('**'*random.randint(10,15))


#3.收藏记录，get，获取收藏记录列表
url = 'https://passport.fengjr.com/fengInfo/api/v2/common/getFunctionListNew/MYSELF'
params = {
	"version":"2.0",
	"page_size":"10",
	"type":"collections"
	}

res= requests.get(url,params=params,headers=headers)
resp = res.json()
#判断返回状态码
try:
	assert res.status_code == 200
except:
	print('status_code error!!')
#判断参数是否存在
try :
	assert 'success' in resp
except:
	print('success not in resp!!')
#判断类型是否正确
try:
	assert type(resp['data']) == list
except:
	print('type error!!')
print(resp['data'][0])
#判定data中是否有数据
try:
	assert resp['data'][0] != None
except:
	print('data is null')

print('**'*random.randint(10,15))

#4.凤储列表，get
url = 'https://m.fengjr.com/api/v2/wd/info/fengChuListV2'
res = requests.get(url)
resp = res.json()
#判断状态码
try :
	assert res.status_code == 200
except:
	print('status_code is error!!')
#判断targets 是否存在
try :
	assert 'data' in resp
except:
	print('data not in response !!')
#判断higLightIndex 类型是否正确
print(type(resp['data']['highLightIndex']))
try:
	type(resp['data']['highLightIndex']) == int
except:
	print('type error !!')
print('**'*random.randint(10,15))


print('4**'*random.randint(10,15))
'''
#5.关联

uri = 'http://mt06.fengjr.inc/'
url = uri + 'api/v2/wd/info/fengChuListV2'
headers = {
	"token":"uZaxzKSB7L2vMWVNmFEKDpV2kQOImMqJhvatbfxCibazBT3zpx3ikUjhZj9NGrpJ"
}
id ={}
for i in range(0,4):
	res = requests.get(url,headers=headers)
	resp = res.json()
	id[i] = resp['data']['targets'][i]['id']
print(len(resp['data']['targets']))
url = uri + 'api/v2/fixed/info/detail' 

#print(id)
print(len(id))
for i in range(len(id)):
	params = {
	"version":"2.0",
	"type":"fengChu",
	"id":id[i],
	"userId":"EFDBFA9F-C8B0-499C-AE67-45FD7608858B"
}

	res = requests.get(url,headers=headers,params=params)
	resp = res.json()
	print(id[i])
	#print(res.status_code,resp['success'])
	assert res.status_code == 200,'!!!status_code error'
	assert resp['success'],'!!!error'
 

