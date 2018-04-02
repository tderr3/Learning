import unittest
from pyunitreport import HTMLTestRunner
import os

'''import scripts
from script1 import class1
from script2 import class2'''

from CpTestBoth import test_001_Basic_rack_pattern, test_002_Basic_flex_pattern

'''# get all tests from SearchText and HomePageTest class
class1tests = unittest.TestLoader().loadTestsFromTestCase(class1)
class2tests = unittest.TestLoader().loadTestsFromTestCase(class2)'''

flexTest = unittest.TestLoader().loadTestsFromTestCase(test_002_Basic_flex_pattern)
rackTest = unittest.TestLoader().loadTestsFromTestCase(test_001_Basic_rack_pattern)

'''# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([class1tests, class2tests])'''
test_suite = unittest.TestSuite([flexTest, rackTest])

'''# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(output = '\\testResults\\')'''
runner = HTMLTestRunner(output = 'c:\\python34\\testResults\\')

# run the suite using HTMLTestRunner
runner.run(test_suite)
