import unittest
import HtmlTestRunner
import os
from SeleniumPythonRefactorTestCase import SearchText
from SeleniumPythonMultipleTests import HomePageTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([home_page_test, search_text])

# open the report file
outfile = open(dir + "\seleniumPythonTestSummary.html",'w')

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(output = dir)


# run the suite using HTMLTestRunner
runner.run(test_suite)
