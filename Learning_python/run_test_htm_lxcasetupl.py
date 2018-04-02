import unittest
import HtmlTestRunner
import os
from LXCASetup import lxcaSetupTest
#from Manage_chassis import ManageChassisTest
#from SeleniumPythonMultipleTests import HomePageTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
setup = unittest.TestLoader().loadTestsFromTestCase(lxcaSetupTest)
#manage_chassis_test = unittest.TestLoader().loadTestsFromTestCase(ManageChassisTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite(setup)

# open the report file
outfile = open(dir + "\Lxcasetuptest.html",'w')

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(output = dir+ '\\Html_results\\')


# run the suite using HTMLTestRunner
runner.run(test_suite)
