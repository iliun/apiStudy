import pytest,os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
# print(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from api.fcdetail import Detail
from api.fclist import List


class Test_detail(object):
	res,resp = Detail.get_detail_requests(Detail)
	def test_01(self):
		assert self.res.status_code == 200
	def test_02(self):
		assert self.resp['success'] == False

if __name__ == '__main__':
	pytest.main(['-s','test_fcdetail.py','--html=../report/Test_detail.html'])