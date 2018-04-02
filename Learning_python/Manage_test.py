import unittest
import HtmlTestRunner
import os
from testManageStark import test_001_ManageStarkTest
from Manage_chassis import test_002_ManageChassisTest
import LXCATaskTracker as jobtrack


# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchText and HomePageTest class
stark = unittest.TestLoader().loadTestsFromTestCase(test_001_ManageStarkTest)
chassis = unittest.TestLoader().loadTestsFromTestCase(test_002_ManageChassisTest)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([stark, chassis])

# open the report file
#outfile = open(dir + "\Lxcasetuptest.html",'w')

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(output = dir+ '\\Html_results\\')


# run the suite using HTMLTestRunner
runner.run(test_suite)
