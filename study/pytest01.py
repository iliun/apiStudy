import pytest,requests
import hosts
class Test01():
	url = hosts.prouri['passport'] + '/fengInfo/api/v2/common/getListAll'
	params = {
	"version":"2.0",
	"user_id":"5E8B240B-45A6-4F22-86CC-90EC970E0515",
	"page_size":"9",
	"category_type":"9",
	"glide_type":"init"
	}
	res = requests.post(url,params=params)
	resp = res.json()
	@pytest.mark.p0
	def test_01(self):
		assert self.res.status_code == 200 ,'status_code error'
	@pytest.mark.skip('skip test_02')
	def test_02(self):
		print('this is test_02')
	@pytest.mark.skipif(res.status_code==200,reason='status_code error ,so skip it!')
	def test_03(self):
		print('this is test_03')

if __name__ == '__main__':
	pytest.main(['-s','-v','-m p0','pytest01.py','--html=../report/report02.html'])

