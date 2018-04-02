from selenium import webdriver


dr = webdriver.Firefox()
dr.get('https://10.243.1.90')

user = dr.find_element_by_xpath('//input[contains(@placeholder,"user")]')
password = dr.find_element_by_xpath('//input[contains(@placeholder,"password")]')
log_in_button = dr.find_element_by_xpath('//span[contains(text(),"Log In")]')

user.send_keys('USERID')
password.send_keys('CME44len')
log_in_button.click()


dr.find_element_by_id('user-id-menu').click()
dr.find_element_by_link_text('Log out').click()
dr.find_element_by_xpath('//span[contains(text(),"Log Off")]').click()
