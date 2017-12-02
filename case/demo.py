import unittest

class Demo(unittest.TestCase):
    def test_case02(self):
        print 2

    def test_case01(self):
        print 1

    def setUp(self):
        print 0

    def tearDown(self):
        print 'close'

    @classmethod
    def setUpClass(cls):
        print 'before'

if __name__ == '__main__':
    testSuite = unittest.TestSuite()
    testSuite.addTest(Demo('test_case02'))
    unittest.TextTestRunner().run()