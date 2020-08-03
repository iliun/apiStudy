#import pytest
'''
class TestClass_01:
	def test_01(self):
		x = 'this'
		print(x)
		assert 'h' in x

	def test_02(self):
		x = 'hello'
		print(x)
		assert hasattr(x,'123')

class TestClass_02:
	def test_01(self):
		x = 'hello'
		assert hasattr(x,'h'),'error'
		print(x)

	def test_02(self):
		x = 'iphone'
		print(x)
		assert 'h' in x
print('----------------')

def f():
	raise SystemExit(1)

def test_mytest():
	with pytest.raises(SystemExit):
		f()
'''
import pytest

def test_main():
	assert 5 != 5
if __name__ == '__main__':
	pytest.main(['-q','pytestst.py'])
