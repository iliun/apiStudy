import pytest
'''
@pytest.fixture(scope='function')
def setup_function(request):
	def teardown_function():
		print('teardown_function')
	request.addfinalizer(teardown_function)
	print('setup_function')

@pytest.fixture(scope='module')
def setup_module(request):
	def teardown_module():
		print('teardown_module')
	request.addfinalizer(teardown_module)
	print('setup_module')

@pytest.mark.website
def test_1(setup_function):
	print('test_1')

def test_2(setup_module):
	print('test_2')

def test_3(setup_function):
	print('test_3')
	assert 2 == 1+2

'''
class Test_01():
	def setup_class(self):
		print('setup_class')
	def teardown_class(self):
		print('teardown_class')
	def setup(self):
		print('this is setup')
	def teardown(self):
		print('this is teardown')
	def test_01(self):
		print('test_01')
		assert 1 == 1

if __name__ == '__main__':
	pytest.main(['-s','test_01.py'])