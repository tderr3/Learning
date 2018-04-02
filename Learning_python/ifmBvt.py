import unittest
from selenium import webdriver
import driver, os, paramiko, time, sys, HtmlTestRunner
#from ifm_bvt import *

actions = 0

class IFM_BVT_TEST(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.dr = driver.mycon()
        inst.dr.implicitly_wait(20)
        inst.dr.maximize_window()
        inst.dr.get('https://10.243.1.98:8044')
        time.sleep(3)

    def test_001_intitlize_user(self):
        user = self.dr.find_element_by_id('user')
        pw = self.dr.find_element_by_id('password')
        log = self.dr.find_element_by_id('btnLogin_label')
        user.clear()
        pw.clear()
        #'''
        user.send_keys('USERID')
        pw.send_keys('PASSW0RD')
        log.click()
        time.sleep(2)
        cp = self.dr.find_element_by_xpath('//input[contains(@id,"password")]')
        np = self.dr.find_element_by_xpath('//input[contains(@id,"newPassword")]')
        cnp = self.dr.find_element_by_xpath('//input[contains(@id, "confirmPassword")]')
        sub = self.dr.find_element_by_xpath('//span[3][contains(text(),"Submit")]')
        cp.send_keys('PASSW0RD')
        np.send_keys('CME44len')
        cnp.send_keys('CME44len')
        sub.click()
        #'''

        #login
        '''
        time.sleep(2)
        user.send_keys('USERID')
        pw.send_keys('CME44len')
        log.click()
        '''

        time.sleep(2)
        self.assertTrue(self.dr.find_element_by_xpath('//div[1][contains(text(),"IBM Fabric Manager")]').is_displayed())

    def test_002_create_edit_remove_etherent_Address_pool(self):
        time.sleep(6)
        self.dr.find_element_by_xpath('//span[contains(text(), "Address Pools")]').click()
        time.sleep(6)
        self.dr.find_element_by_id('dijit_MenuItem_3_text').click()
        #self.dr.find_element_by_xpath('//td[2][contains(text(),"Ethernet pool status/config")]').click()#select eth
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Global Ethernet Pool (Predefined)")]').click()
        actions = self.dr.find_element_by_xpath('//a[contains(text(),"Actions")]')
        actions.click()
        actAdd = self.dr.find_element_by_id('MenuAdd_text')
        actAdd.click()
        time.sleep(1)
        self.assertTrue(self.dr.find_element_by_xpath('//span[1][contains(text(),"Add Ethernet Pool")]').is_displayed())
        self.dr.find_element_by_id('add_name').send_keys('Pool1')
        self.dr.find_element_by_id('add_maxChassis').clear()
        self.dr.find_element_by_id('add_maxChassis').send_keys('3')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(1)
        self.assertTrue(self.dr.find_element_by_xpath('//td[1][contains(text(),"Pool1")]').is_displayed())

        

        #add eth pool 2
        #print('Adding Eth pool 2.','\n')
        
        time.sleep(.5)
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Global Ethernet Pool (Predefined)")]').click()
        actions.click()
        actAdd.click()
        time.sleep(1)
        self.dr.find_element_by_id('add_name').send_keys('Pool2')
        self.dr.find_element_by_id('add_maxChassis').clear()
        self.dr.find_element_by_id('add_maxChassis').send_keys('3')
        self.dr.find_element_by_id('add_first').clear()
        self.dr.find_element_by_id('add_first').send_keys('00:00:00:00:B7:20')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(1)

        #remove pool
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Pool1")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuRemove_text').click()
        time.sleep(1)
        #self.assertFalse(self.dr.find_element_by_xpath('//td[1][contains(text(),"Pool1")]')

        #editing pool 2
        #print('Editing Pool2 now','\n')
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Pool2")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuEdit_text').click()
        time.sleep(1)
        self.dr.find_element_by_id('edit_name').clear()
        self.dr.find_element_by_id('edit_name').send_keys('New Pool 1')
        self.dr.find_element_by_id('edit_first').clear()
        self.dr.find_element_by_id('edit_first').send_keys('00:00:00:00:ee:ff')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        self.assertTrue(self.dr.find_element_by_xpath('//td[1][contains(text(),"New Pool 1")]').is_displayed())

    def test_003_create_edit_remove_Fibrechannel_Address_pool(self):
        time.sleep(3)
        self.dr.find_element_by_xpath('//span[contains(text(), "Address Pools")]').click()#address pool:ethernet
        time.sleep(3)
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Fibre Channel")]').click()
        time.sleep(2)
        self.assertTrue(self.dr.find_element_by_xpath('//h2[contains(text(), "Fibre Channel Pools")]').is_displayed())
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Global Fibre Channel Pool (Predefined)")]').click()
        actions = self.dr.find_element_by_xpath('//a[contains(text(),"Actions")]')
        actions.click()
        self.dr.find_element_by_id('MenuAdd_text').click()
        self.dr.find_element_by_id('add_name').send_keys('FC_Pool_1')
        self.dr.find_element_by_id('add_maxChassis').clear()
        self.dr.find_element_by_id('add_maxChassis').send_keys('3')
        self.dr.find_element_by_id('add_first').clear()
        self.dr.find_element_by_id('add_first').send_keys('00:00:00:00:00:00:00:01')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Global Fibre Channel Pool (Predefined)")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuAdd_text').click()
        self.dr.find_element_by_id('add_name').send_keys('FC_Pool_2')
        self.dr.find_element_by_id('add_maxChassis').clear()
        self.dr.find_element_by_id('add_maxChassis').send_keys('3')
        self.dr.find_element_by_id('add_first').clear()
        self.dr.find_element_by_id('add_first').send_keys('00:00:00:00:00:00:05:42')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Global Fibre Channel Pool (Predefined)")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuAdd_text').click()
        self.dr.find_element_by_id('add_name').send_keys('FC_Pool_3')
        self.dr.find_element_by_id('add_maxChassis').clear()
        self.dr.find_element_by_id('add_maxChassis').send_keys('3')
        self.dr.find_element_by_id('add_first').clear()
        self.dr.find_element_by_id('add_first').send_keys('00:00:00:00:00:00:0A:83')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Global Fibre Channel Pool (Predefined)")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuAdd_text').click()
        self.dr.find_element_by_id('add_name').send_keys('FC_Pool_4')
        self.dr.find_element_by_id('add_maxChassis').clear()
        self.dr.find_element_by_id('add_maxChassis').send_keys('3')
        self.dr.find_element_by_id('add_first').clear()
        self.dr.find_element_by_id('add_first').send_keys('00:00:00:00:00:00:0F:C4')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Global Fibre Channel Pool (Predefined)")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuAdd_text').click()
        self.dr.find_element_by_id('add_name').send_keys('Test Pool')
        self.dr.find_element_by_id('add_maxChassis').clear()
        self.dr.find_element_by_id('add_maxChassis').send_keys('3')
        self.dr.find_element_by_id('add_first').clear()
        self.dr.find_element_by_id('add_first').send_keys('AA:AA:AA:AA:AA:AA:0F:C4')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(1)
        self.assertTrue(self.dr.find_element_by_xpath('//td[3][contains(text(),"00:00:00:00:00:00:0F:C3")]').is_displayed())

        self.dr.find_element_by_xpath('//td[3][contains(text(), "AA:AA:AA:AA:AA:AA:15:04")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuEdit_text').click()
        self.dr.find_element_by_id('edit_name').clear()
        self.dr.find_element_by_id('edit_name').send_keys('New_Test_pool')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(1)
        self.assertTrue(self.dr.find_element_by_xpath('//td[1][contains(text(),"New_Test_pool")]').is_displayed())
        self.dr.find_element_by_xpath('//td[1][contains(text(),"New_Test_pool")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuRemove_text').click()

    def test_004_create_edit_remove_SAS_Address_pool(self):
        time.sleep(2)
        self.dr.find_element_by_xpath('//span[contains(text(), "Address Pools")]').click()#address pool:ethernet
        time.sleep(2)
        self.dr.find_element_by_xpath('//td[1][contains(text(),"SAS")]').click()
        time.sleep(1)
        self.assertTrue(self.dr.find_element_by_xpath('//h2[contains(text(), "SAS Pools")]').is_displayed())
        actions = self.dr.find_element_by_xpath('//a[contains(text(),"Actions")]')
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Global SAS Pool (Predefined)")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuAdd_text').click()
        time.sleep(2)
        #saspool popup
        time.sleep(1)
        self.dr.find_element_by_id('add_name').send_keys('Pool1')
        self.dr.find_element_by_id('add_maxChassis').clear()
        self.dr.find_element_by_id('add_maxChassis').send_keys('3')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        #saspool2
        time.sleep(1)
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Global SAS Pool (Predefined)")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuAdd_text').click()
        time.sleep(2)
        #saspool popup
        self.dr.find_element_by_id('add_name').send_keys('Pool2')
        self.dr.find_element_by_id('add_first').clear()
        self.dr.find_element_by_id('add_first').send_keys('00:00:00:00:00:00:05:42')
        self.dr.find_element_by_id('add_maxChassis').clear()
        self.dr.find_element_by_id('add_maxChassis').send_keys('3')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        #edit pool 2
        time.sleep(1)
        self.dr.find_element_by_xpath('//td[3][contains(text(),"00:00:00:00:00:00:0A:82")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuEdit_text').click()
        self.dr.find_element_by_id('edit_name').clear()
        self.dr.find_element_by_id('edit_name').send_keys('New_Pool2')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        self.assertTrue(self.dr.find_element_by_xpath('//td[1][contains(text(),"New_Pool2")]').is_displayed())
        #del pool
        time.sleep(1)
        self.dr.find_element_by_xpath('//td[3][contains(text(),"00:00:00:00:00:00:05:41")]').click()
        actions.click()
        self.dr.find_element_by_id('MenuRemove_text').click()

        
    def test_005_BootTarget_testing(self):
        time.sleep(2)
        self.dr.find_element_by_xpath('//span[contains(text(),"Templates")]').click()
        time.sleep(2)
        self.dr.find_element_by_id('dijit_MenuItem_6_text').click()
        time.sleep(2)
        actions = self.dr.find_element_by_xpath('//a[contains(text(),"Actions")]')
    
        actadd1 = self.dr.find_element_by_id('Menuadd_text')
        addname = self.dr.find_element_by_id('add_name')
        prim1 = self.dr.find_element_by_id('add_address_p1')
        prim2 = self.dr.find_element_by_id('add_address_p2')
        sec1 = self.dr.find_element_by_id('add_address_s1')
        sec2 = self.dr.find_element_by_id('add_address_s2')
        lun1 = self.dr.find_element_by_id('add_lun_p1')
        lun2 = self.dr.find_element_by_id('add_lun_p2')
        lun3 = self.dr.find_element_by_id('add_lun_s1')
        lun4 = self.dr.find_element_by_id('add_lun_s2')
        typefc = self.dr.find_element_by_id('add_typeFC')
        typesas = self.dr.find_element_by_id('add_typeSAS')
    
        #adding target 1
        actions.click()
        actadd1.click()
        time.sleep(2)
        addname.send_keys('sas target 1')
        typesas.click()
        prim1.send_keys('BB:00:00:00:00:00:00:01')
        prim2.send_keys('BB:00:00:00:00:00:00:02')
        sec1.send_keys('BB:00:00:00:00:00:00:21')
        sec2.send_keys('BB:00:00:00:00:00:00:22')
        lun1.clear()
        lun2.clear()
        lun3.clear()
        lun4.clear()
        lun1.send_keys('1')
        lun2.send_keys('2')
        lun3.send_keys('3')
        lun4.send_keys('4')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(2)
    
        #adding target 2
        actions.click()
        actadd1.click()
        time.sleep(2)
        addname.send_keys('FC target 1')
        typefc.click()
        prim1.send_keys('CC:00:00:00:00:00:00:01')
        prim2.send_keys('CC:00:00:00:00:00:00:02')
        sec1.send_keys('CC:00:00:00:00:00:00:21')
        sec2.send_keys('CC:00:00:00:00:00:00:22')
        lun1.clear()
        lun2.clear()
        lun3.clear()
        lun4.clear()
        lun1.send_keys('5')
        lun2.send_keys('6')
        lun3.send_keys('7')
        lun4.send_keys('8')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(2)
    
        #adding target 3
        actions.click()
        actadd1.click()
        time.sleep(2)
        addname.send_keys('FC target 2')
        typefc.click()
        sec1.send_keys('CC:00:00:00:00:00:CC:21')
        sec2.send_keys('CC:00:00:00:00:00:CC:22')
        lun1.clear()
        lun2.clear()
        lun3.clear()
        lun4.clear()
        lun3.send_keys('10')
        lun4.send_keys('11')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(2)
    
        #adding target 4
        actions.click()
        actadd1.click()
        time.sleep(2)
        addname.send_keys('SAS target 2')
        typesas.click()
        prim1.send_keys('BB:00:00:00:00:00:BB:01')
        prim2.send_keys('BB:00:00:00:00:00:BB:02')
        lun1.clear()
        lun2.clear()
        lun3.clear()
        lun4.clear()
        lun3.send_keys('22')
        lun4.send_keys('23')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(2)
    
        #edit tartgets
        actedit1 = self.dr.find_element_by_id('MenuEdit_text')
        editname = self.dr.find_element_by_id('edit_name')
        self.dr.find_element_by_xpath('//tr/td[1][contains(text(),"FC target 1")]').click()
        time.sleep(2)
        actions.click()
        actedit1.click()
        time.sleep(1)
        editname.clear()
        editname.send_keys('New FC target 1')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//tr/td[1][contains(text(),"sas target 1")]').click()
        time.sleep(2)
        actions.click()
        actedit1.click()
        time.sleep(1)
        editname.clear()
        editname.send_keys('New sas target 1')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(1)
        #remove extra pools
        self.dr.find_element_by_xpath('//tr/td[1][contains(text(),"New sas target 1")]').click()
        time.sleep(1)
        actions.click()
        remove1 = self.dr.find_element_by_id('MenuRemove_text')
        remove1.click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//tr/td[1][contains(text(),"New FC target 1")]').click()
        time.sleep(1)
        actions.click()
        remove1.click()
        time.sleep(1)
        self.assertTrue(self.dr.find_element_by_xpath('//td[1][contains(text(),"FC target 2")]').is_displayed())
        self.assertTrue(self.dr.find_element_by_xpath('//td[1][contains(text(),"SAS target 2")]').is_displayed())

        
        
        
    def test_006_Chassis_template_testing(self):
        #add chassis template 1
        time.sleep(2)
        self.dr.find_element_by_xpath('//span[contains(text(),"Templates")]').click()
        time.sleep(2)
        self.dr.find_element_by_id('dijit_MenuItem_7_text').click()
        time.sleep(2)
        actions = self.dr.find_element_by_xpath('//a[contains(text(),"Actions")]')
        actadd1 = self.dr.find_element_by_id('MenuAdd_text')
        actions.click()
        time.sleep(.5)
        actadd1.click()
        rports1=['1','2','3','4','5','6','7','8']
        time.sleep(1)
        for port in (rports1):
            self.dr.find_element_by_id('add_macRangePort_' + port).click()
            time.sleep(.25)
        name1 = self.dr.find_element_by_id('add_name')
        name1.send_keys('Template 1')
        rangesize = self.dr.find_element_by_id('add_macRangeSize')
        rangesize.clear()
        rangesize.send_keys('4')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(2)
        #add chassis template 2
        actions.click()
        time.sleep(.5)
        actadd1.click()
        for port in (rports1):
            self.dr.find_element_by_id('add_macRangePort_' + port).click()
            time.sleep(.25)
        name1.send_keys('Template 2')
        rangesize = self.dr.find_element_by_id('add_macRangeSize')
        rangesize.clear()
        rangesize.send_keys('4')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(2)
        #edit chassis template
        self.dr.find_element_by_xpath('//tr/td[contains(text(),"Template 1")]').click()
        actions.click()
        time.sleep(.5)
        self.dr.find_element_by_id('MenuEdit_text').click()
        time.sleep(.5)
        self.dr.find_element_by_id('edit_name').clear()
        self.dr.find_element_by_id('edit_name').send_keys('New Template 1')
        time.sleep(2)
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(2)
        #removing chassis templete
        self.dr.find_element_by_xpath('//tr/td[contains(text(),"Template 2")]').click()
        time.sleep(.5)
        actions.click()
        self.dr.find_element_by_id('MenuRemove_text').click()
        time.sleep(2)
        self.assertTrue(self.dr.find_element_by_xpath('//td[contains(text(), "New Template 1")]').is_displayed())

    def test_007_vnic_template_testing(self):
        time.sleep(2)
        self.dr.find_element_by_xpath('//span[contains(text(),"Templates")]').click()
        time.sleep(2)
        self.dr.find_element_by_id('dijit_MenuItem_8_text').click()
        time.sleep(2)
        actions = self.dr.find_element_by_xpath('//span/a[contains(text(),"Action")]')
        #actadd1 = self.dr.find_element_by_id('MenuAdd_text')
        actions.click()
        time.sleep(3)
        self.dr.find_element_by_xpath('//td[2][contains(text(), "Add")]').click()
        time.sleep(.5)
        name1 = self.dr.find_element_by_id('add_name')
        flex = self.dr.find_element_by_id('familyFlexSystem2port')
        blade = self.dr.find_element_by_id('familyBladeCenter')
        p16 = self.dr.find_element_by_id('multipleVnicFilter16')
        p8 = self.dr.find_element_by_id('multipleVnicFilter8')
        save = self.dr.find_element_by_id('saveButton_label')
        #create vnic 1
        name1.send_keys('Flex 1')
        flex.click()
        p8.click()
        save.click()
        time.sleep(.5)

        #create vnic 2
        actions.click()
        time.sleep(4)
        self.dr.find_element_by_xpath('//td[2][contains(text(), "Add")]').click()
        time.sleep(.5)
        name1.send_keys('Bladecenter 1')
        blade.click()
        p8.click()
        save.click()
        time.sleep(.5)
    
    
        #create vnic 3
        actions.click()
        time.sleep(4)
        self.dr.find_element_by_xpath('//td[2][contains(text(), "Add")]').click()
        time.sleep(.5)
        name1.send_keys('Bladecenter remove')
        blade.click()
        p8.click()
        save.click()
        time.sleep(.5)
        
        
        #edit vnic 1
        edit1 = self.dr.find_element_by_id('MenuEdit_text')
        self.dr.find_element_by_xpath('//tr/td[1][contains(text(),"Flex 1")]').click()
        time.sleep(1)
        actions.click()
        edit1.click()
        time.sleep(.5)
        name1.clear()
        name1.send_keys('New Flex 1')
        p16.click()
        save.click()
        time.sleep(1)
        
        #edit vnic 2
        self.dr.find_element_by_xpath('//tr/td[1][contains(text(),"Bladecenter 1")]').click()
        time.sleep(1)
        actions.click()
        edit1.click()
        time.sleep(.5)
        name1.clear()
        name1.send_keys('New Bladecenter 1')
        p16.click()
        save.click()
        time.sleep(1)
        #remove vnic
        self.dr.find_element_by_xpath('//tr/td[1][contains(text(),"Bladecenter remove")]').click()
        time.sleep(.5)
        actions.click()
        self.dr.find_element_by_id('MenuRemove_text').click()
        time.sleep(1)
        
        
    def test_009_discovery_testing(self):
        time.sleep(2)
        #single Chassis
        self.dr.find_element_by_xpath('//span[contains(text(), "Hardware")][contains(@id, "Menu")]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//tr/td[1][contains(text(),"Devices")]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//span/a[contains(text(),"Actions")]').click()
        self.dr.find_element_by_id('Menuadd_text').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//span[3][contains(text(),"Next")]').click()
        self.dr.find_element_by_id('chassis').send_keys('10.243.0.23')
        self.dr.find_element_by_id('username').send_keys('USERID')
        self.dr.find_element_by_id('password').send_keys('CME44len')
        self.dr.find_element_by_id('snmpUserIp').send_keys('10.243.1.98')
        self.dr.find_element_by_id('snmpPw').send_keys('password')
        self.dr.find_element_by_id('snmpBkUserIp').send_keys('10.243.1.122')
        self.dr.find_element_by_id('snmpBkPw').send_keys('password')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(), "Start")][contains(@id,"form")]')
        self.isDisplayed(tmp).click()
        time.sleep(7)
        self.dr.find_element_by_xpath('//span[3][contains(text(), "OK")]').click()
        time.sleep(1)
        self.assertTrue(self.dr.find_element_by_xpath('//td[4][contains(text(), "10.243.0.23")]').is_displayed())
        #todo Range Chassis
        #todo By File

    def test_010_hardware_pool_testing(self):
        time.sleep(2)
        self.dr.find_element_by_xpath('//span[contains(text(), "Hardware")][contains(@id, "Menu")]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//tr/td[1][contains(text(),"Pools")]').click()
        time.sleep(1)
        self.dr.find_element_by_xpath('//span/a[contains(text(),"Actions")]').click()
        time.sleep(2)
        self.dr.find_element_by_id('MenuAdd_text').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//input[contains(@id,"poolName")]').send_keys('Test Pool .23')
        self.dr.find_element_by_xpath('//div[1][contains(@id, "poolGrid")]//input[contains(@class, "GridInput")]').click()
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(), "Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(3)
        self.assertTrue(self.dr.find_element_by_xpath('//td[contains(text(), "Test Pool .23")]').is_displayed())
    def test_011_Creating_full_profile(self):
        time.sleep(3)
        self.dr.find_element_by_xpath('//span[contains(text(),"Profiles")]').click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//span/a[contains(text(),"Actions")]').click()
        time.sleep(2)
        self.dr.find_element_by_id('MenuAdd_text').click()
        time.sleep(2)
        self.dr.find_element_by_id('add_name').send_keys('Profile_1')
        self.dr.find_element_by_id('add_hardwarePool').send_keys('Test Pool .23')
        self.dr.find_element_by_id('add_ethAddressPool').send_keys('New Pool 1')
        self.dr.find_element_by_id('add_fcWWNNAPool').send_keys('FC_Pool_1')
        self.dr.find_element_by_id('add_fcWWNNBPool').send_keys('FC_Pool_2')
        self.dr.find_element_by_id('add_fcWWPNAPool').send_keys('FC_Pool_3')
        self.dr.find_element_by_id('add_fcWWPNBPool').send_keys('FC_Pool_4')
        self.dr.find_element_by_id('add_sasAddressPool').send_keys('New_Pool2')
        self.dr.find_element_by_id('add_chassisTemplate').send_keys('New Template 1')
        self.dr.find_element_by_id('add_fcTargetTemplate').send_keys('FC target 2')
        self.dr.find_element_by_id('add_sasTargetTemplate').send_keys('SAS target 2')
        self.dr.find_element_by_id('add_qosFSTemplate').send_keys('Flex 1')
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(), "Save")]')
        self.isDisplayed(tmp).click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//tr/td[1][contains(text(),"Profile_1")]').click()
        time.sleep(.5)
        self.assertTrue(self.dr.find_element_by_xpath('//span[contains(text(), "Profile_1")]').is_displayed())

        self.dr.find_element_by_xpath('//tr/td[1][contains(text(),"Profile_1")]').click()
        self.dr.find_element_by_xpath('//span/a[contains(text(),"Action")]').click()
        time.sleep(2)
        self.dr.find_element_by_id('MenuDeploy_text').click()
        self.dr.find_element_by_id('deploy_name').send_keys('Deploy_Profile_1')
        self.dr.find_element_by_xpath('//span[3][contains(text(), "Deploy")]').click()
        time.sleep(4)
        tmp = self.dr.find_elements_by_xpath('//span[3][contains(text(),"Close")]')
        self.isDisplayed(tmp).click()
        time.sleep(2)
        self.dr.find_element_by_xpath('//td[1][contains(text(),"Profile_1")]').click()
        time.sleep(2)
        self.assertTrue(self.dr.find_element_by_xpath('//span[contains(text(), "Profile_1")]').is_displayed())
    def test_011_Deploying_full_profile(self):
        time.sleep(3)
        self.dr.find_element_by_xpath('//span[contains(text(), "Deployment")][contains(@id, "Menu")]').click()
        time.sleep(2)
        self.assertTrue(self.dr.find_element_by_xpath('//td[1][contains(text(),"Deploy_Profile_1")]').is_displayed())
        self.assertTrue(self.dr.find_element_by_xpath('//td[2][contains(text(),"Profile_1")]').is_displayed())
        
        
        

    @classmethod
    def tearDownClass(inst):
        print('CLEAN UP TIME!!!')
        time.sleep(8)
        inst.dr.quit()

    def isDisplayed(self,elems):
        for element in elems:
            if element.is_displayed() == True:
                return element


if __name__ == '__main__':
    #unittest.main(verbosity=3)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='c:\\python34\\Html_results\\', report_title='IFM BVT'))





























    def isDisplayed(self,elems): 
        for element in elems:
            if element.is_displayed() == True:
                return element        
