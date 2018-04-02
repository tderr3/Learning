from selenium import webdriver
import driver, time

userList = ['tderr','noone']
unfoundUserlist = []

dr = driver.mycon()
#dr.get('https://bz.labs.lenovo.com/editusers.cgi')
userInput = dr.find_element_by_xpath('//input[1][contains(@id,"matchstr")]')
searchButton = dr.find_element_by_xpath('//input[2][contains(@id,"search")][contains(@type,"submit")]')


for user in userList:
    dr.get('https://bz.labs.lenovo.com/editusers.cgi')
    dr.find_element_by_xpath('//input[1][contains(@id,"matchstr")]').send_keys(user)
    time.sleep(.5)
    dr.find_element_by_xpath('//input[2][contains(@id,"search")][contains(@type,"submit")]').click()
    time.slep(1)
    try:
        dr.find_element_by_partial_link_text(user).click()
        time.sleep(1)
        dr.find_element_by_id('group_32').click()
        time.sleep(.5)
        dr.find_element_by_id().click()
        sleep(.5)
        dr.find_element_by_id().click()
        time.sleep(.5)

    except:
        unfoundUserlist.append(user)

print(unfoundUserlist)
    
