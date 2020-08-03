import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from api.fclist import List

class Test_list():
	def test_01(self):
		print('success')
		assert List.res.status_code == 200

	def test_02(self):
		assert List.resp['success']

if __name__ == '__main__':
	pytest.main(['-s','test_fclist.py','--html=../report/Test_list.html'])
