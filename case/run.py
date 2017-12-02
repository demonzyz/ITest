# coding:utf-8
import unittest
import os
import case01, case02, case07
import importlib
from xml.etree import ElementTree as ET
import HTMLTestRunnerCN
import time

if __name__ == '__main__':
    # suite.xml = unittest.TestSuite()
    # suite.xml.addTest(case01.Run())
    # suite.xml.addTest(case02.Run())
    # suite.xml.addTest(case07.Run())
    # unittest.TextTestRunner().run(suite.xml)


    # print os.path.abspath('./')
    # test_dir = './'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    # unittest.TextTestRunner().run(discover)

    print os.path.abspath('../suite.xml')
    suite = unittest.TestSuite()
    doc = ET.parse('../suite.xml')
    print os.path.abspath('./*')
    all = doc.findall('./*')
    for e in all:
        m = importlib.import_module(e.tag)

        suite.addTest(m.Run())

    time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    fp = open('./report.html', 'wb')
    HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=u'自动化测试报告').run(suite)
    # unittest.TextTestRunner().run(suite.xml)