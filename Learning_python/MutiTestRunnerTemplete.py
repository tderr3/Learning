import unittest
import HtmlTestRunner
import os

'''import scripts
from script1 import class1
from script2 import class2'''



'''# get all tests from SearchText and HomePageTest class
class1tests = unittest.TestLoader().loadTestsFromTestCase(class1)
class2tests = unittest.TestLoader().loadTestsFromTestCase(class2)'''

'''# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([class1tests, class2tests])'''


'''# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(output = '\\testResults\\')'''


# run the suite using HTMLTestRunner
runner.run(test_suite)
