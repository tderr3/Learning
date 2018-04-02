from selenium import webdriver
import time, unittest, os, random
#import HtmlTestRunner "this line is optional if you want the nice html report"
from selenium.webdriver.common import action_chains, keys

#jobtrack.warnings.filterwarnings('ignore')

class test_001_Basic_rack_pattern(unittest.TestCase):
    @classmethod
    def setUpClass(inst):#this will open the browser, direct it to 10.243.1.90, and login
        inst.dr = webdriver.Firefox()
        inst.dr.implicitly_wait(25)
        inst.dr.maximize_window()
        inst.dr.get('https://10.243.1.100')
        user = inst.dr.find_element_by_xpath('//input[contains(@placeholder,"user")]')
        paswd = inst.dr.find_element_by_xpath('//input[contains(@placeholder,"password")]')
        user.send_keys('USERID')
        paswd.send_keys('CME44len')
        paswd.send_keys(keys.Keys.ENTER)
        time.sleep(4)


    def test_001_basic_rack_test(self):#this test creates a basic pattern containing some system information pattern for rack server
        time.sleep(2)
        prov = self.dr.find_element_by_id('provisioning')
        prov.click()
        patterns = self.dr.find_element_by_link_text('Patterns')
        patterns.click()
        time.sleep(2)
        temp = self.dr.find_elements_by_xpath('//span[1][contains(@class, "Create")]')
        create = self.isDisplayed(temp)
        create.click()
        time.sleep(1)
        createScratch=self.dr.find_element_by_xpath('//span[contains(text(), "Create a new pattern from scratch")]')
        createScratch.click()
        formFactor = self.dr.find_element_by_xpath('//span[contains(text(),"Flex Compute Node")]')
        formFactor.click()
        rackFormFactor = self.dr.find_element_by_xpath('//td[2][contains(text(),"Rack, Tower, or Dense Server")]')
        rackFormFactor.click()
        formFactorChangeCheck = self.dr.find_element_by_xpath('//span[3][contains(text(),"Change")]')
        formFactorChangeCheck.click()
        patternName = self.dr.find_element_by_xpath('//input[contains(@id, "templateName")]')
        patternName.send_keys('Rack Pattern from scratch'+(str(random.randint(1,100))))
        patternDesciption = self.dr.find_element_by_xpath('//textarea[contains(@id, "templateDescription")]')
        patternDesciption.send_keys('Description test for rack server')
        nextButton = self.dr.find_element_by_xpath('//span[3][contains(text(),"Next")]')
        nextButton.click()
        time.sleep(1)
        nextButton.click()
        time.sleep(1)
        nextButton.click()
        time.sleep(1)
        nextButton.click()
        time.sleep(1)
        nextButton.click()
        time.sleep(1)
        sysInfoCreate = self.dr.find_element_by_xpath('//img[contains(@id, "systmplcreateicon")]')
        sysInfoCreate.click()
        #System infromation pattern creation box
        self.dr.find_element_by_xpath('//input[contains(@id,"name-field")][contains(@id,"SystemInfoPattern")]').send_keys('Rack_server_'+(str(random.randint(1,100))))
        self.dr.find_element_by_xpath('//textarea[contains(@id, "SystemInfoPattern")]').send_keys('rack test description for system info pattern')
        self.dr.find_element_by_xpath('//span[3][contains(text(), "Custom")]').click()
        cusText = self.dr.find_element_by_xpath('//option[contains(text(), "Custom Text")]')
        sysLoc = self.dr.find_element_by_xpath('//option[contains(text(), "System Location")]')
        incrNum = self.dr.find_element_by_xpath('//option[contains(text(), "Incrementing Numeric")]')
        cusText.click()
        addButton = self.dr.find_element_by_xpath('//img[1][contains(@class, "MoveRightIcon")]')
        addButton.click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//input[contains(@id, "ValidationTextBox")][contains(@aria-invalid,"false")]').send_keys('Rack_'+(str(random.randint(1,100))))
        time.sleep(1)
        self.dr.find_element_by_xpath('//span[3][contains(text(),"Add")][contains(@id,"form")]').click()
        time.sleep(1)
        cusText.click()
        sysLoc.click()
        addButton.click()
        time.sleep(1)
        incrNum.click()
        addButton.click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//input[contains(@id, "contact-field")]').send_keys('Auto_User')
        time.sleep(1)
        self.dr.find_element_by_xpath('//input[contains(@id, "location-field")]').send_keys('loc')
        time.sleep(1)
        self.dr.find_element_by_xpath('//span[3][contains(text(),"Create")]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//span[3][contains(text(),"Save")][not(contains(text(),"Deploy"))]').click()
        time.sleep(2)
        self.assertTrue(self.dr.find_element_by_partial_link_text('Rack Pattern from scratch').is_displayed())


    '''def test_001(self):#this test creates a basic pattern containing some system information pattern for flex server
        time.sleep(2)
        prov = self.dr.find_element_by_id('provisioning')
        prov.click()
        patterns = self.dr.find_element_by_link_text('Patterns')
        patterns.click()
        time.sleep(2)
        temp = self.dr.find_elements_by_xpath('//span[1][contains(@class, "Create")]')
        create = self.isDisplayed(temp)
        create.click()
        time.sleep(1)
        createScratch=self.dr.find_element_by_xpath('//span[contains(text(), "Create a new pattern from scratch")]')
        createScratch.click()
        patternName = self.dr.find_element_by_xpath('//input[contains(@id, "templateName")]')
        patternName.send_keys('Flex Pattern from scratch'+(str(random.randint(1,100))))
        patternDesciption = self.dr.find_element_by_xpath('//textarea[contains(@id, "templateDescription")]')
        patternDesciption.send_keys('Description test for flex server')
        nextButton = self.dr.find_element_by_xpath('//span[3][contains(text(),"Next")]')
        nextButton.click()
        nextButton.click()
        nextButton.click()
        nextButton.click()
        nextButton.click()
        sysInfoCreate = self.dr.find_element_by_xpath('//img[contains(@id, "systmplcreateicon")]')
        sysInfoCreate.click()
        #System infromation pattern creation box
        self.dr.find_element_by_xpath('//input[contains(@id,"name-field")][contains(@id,"SystemInfoPattern")]').send_keys('Flex_server_'+(str(random.randint(1,100))))
        self.dr.find_element_by_xpath('//textarea[contains(@id, "SystemInfoPattern")]').send_keys('Flex test description for system info pattern')
        self.dr.find_element_by_xpath('//span[3][contains(text(), "Custom")]').click()
        cusText = self.dr.find_element_by_xpath('//option[contains(text(), "Custom Text")]')
        sysLoc = self.dr.find_element_by_xpath('//option[contains(text(), "System Location")]')
        incrNum = self.dr.find_element_by_xpath('//option[contains(text(), "Incrementing Numeric")]')
        cusText.click()
        time.sleep(3)
        addButton = self.dr.find_element_by_xpath('//img[1][contains(@class, "MoveRightIcon")]')
        addButton.click()
        time.sleep(3)
        temp = self.dr.find_elements_by_xpath('//input[contains(@id, "ValidationTextBox")]')
        customText = self.isDisplayed(temp)
        customText.send_keys('Flex_'+(str(random.randint(1,9))))
        time.sleep(3)
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Add")]')
        self.isDisplayed(tmp).click()
        cusText.click()
        sysLoc.click()
        time.sleep(3)
        addButton.click()
        incrNum.click()
        addButton.click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//input[contains(@id, "contact-field")]').send_keys('Auto_User')
        time.sleep(1)
        self.dr.find_element_by_xpath('//input[contains(@id, "location-field")]').send_keys('loc')
        time.sleep(1)
        self.dr.find_element_by_xpath('//span[3][contains(text(),"Create")]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//span[3][contains(text(),"Save")][not(contains(text(),"Deploy"))]').click()
        time.sleep(2)
        self.assertTrue(self.dr.find_element_by_link_text('Flex Pattern from scratch').is_displayed())'''

                
    @classmethod
    def tearDownClass(inst):#this closes the browser
        '''inst.dr.refresh()
        time.sleep(2)
        inst.dr.find_element_by_id('provisioning').click()
        inst.find_element_by_link_text('Patterns').click()
        time.sleep(1)
        inst.dr.find_element_by_xpath('//td[1][contains(@class,"gridxCell")][contains(@aria-describedby, "uniq")]').click()
        inst.dr.find_element_by_xpath('//span[1][contains(@class, "DeleteLgIcon")][not(contains(@role,"presentation"))]').click()
        inst.dr.find_element_by_xpath('//span[3][contains(text(),"Delete")]').click()'''
        inst.dr.quit()

#This function takes a list of elements and checks if it is active on the page.
#I use this when i have multiple elements that i can't tell apart from the one i want to interact with

    def isDisplayed(self,elems): 
        for element in elems:
            if element.is_displayed() == True:
                return element


if __name__ == '__main__':
    unittest.main(verbosity=3)
    #you can comment out the above line and uncoment the bellow if you want to generate an html report for your status
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='c:\\python34\\Html_results\\'))     
        
