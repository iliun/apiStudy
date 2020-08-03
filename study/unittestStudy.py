

#1.直接使用Testcase
'''
import unittest
class Test01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('execute setUpClass')

    def setUp(self):
        print('execute setUp')

    def tearDown(self):
        print('execute tearDown')

    def test_01(self):
        print('test_01')

    def test_02(self):
        print('test02')

    @classmethod
    def teardownClass(cls):
        print('execute teardownClass')

if __name__ == '__main__':
    unittest.main()

'''

#2.使用testSuite
'''
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test01('test_02'))
    suite.addTest(Test01('test_01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
'''
import unittest
class Test01(unittest.TestCase):
    def test_01(self):
        self.assertEqual('foo'.upper(),'FOo','error')

    @unittest.skip('skip test02')
    def test_02(self):
        self.assertTrue('FOO'.isupper())
        print('test_02')

    def test_03(self):
        s = 'hello word'
        self.assertEqual(s.split(),['hello','word'])

    def test_04(self):
        try :
            assert 'FOo'.isupper()
        except : 
            print('test_04')
if __name__ == '__main__':
    unittest.main()


