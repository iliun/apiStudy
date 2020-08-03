import requests,unittest

url = 'https://beta.fengjr.com/fengInfo/api/v2/common/getListAll'
params = {
            "category_type": "16",
            "page_size": "10",
            "user_id": "22B52EA7-5D85-44BF-8E89-96D3F43E2597",
            "version": "2.0"}
headers = {
            'Authorization': "Bearer Rxp1GxIn2VC27ylFIdy3Sh4WNMVSslm38AjNHB7vPhj0oLnRMiiirC73wbXG7o9x"
        }
response = requests.get(url,headers=headers,params=params)
res = response.json()
print(res)
print(type(res['data']))

try :
	assert 'success' in res 
except :
	print('no')

