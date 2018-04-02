prov = dr.find_element_by_id('provisioning')
prov.click()
patterns = dr.find_element_by_link_text('Patterns')
patterns.click()
temp = dr.find_elements_by_xpath('//span[1][contains(@class, "Create")]')
create = isDisplayed(temp)
temp = dr.find_elements_by_xpath('//span[1][contains(@class, "Import")]')
importButton = isDisplayed(temp)

#tabs
catagoryTab = dr.find_element_by_xpath('//span[2][contains(text(),"Category Patterns")]')
PlaceholderTab = dr.find_element_by_xpath('//span[2][contains(text(),"Placeholder Chassis")]')
patternsTab = dr.find_element_by_xpath('//span[2][contains(text(),"Server Patterns")]')

create.click()

#pattern types
createScratch=dr.find_element_by_xpath('//span[contains(text(), "Create a new pattern from scratch")]')
createExisting = dr.find_element_by_xpath('//span[contains(text(),"existing server")]')


createScratch.click()

#flex path







#rack path
formFactor = dr.find_element_by_xpath('//span[contains(text(),"Flex Compute Node")]')
formFactor.click()
rackFormFactor = dr.find_element_by_xpath('//td[2][contains(text(),"Rack, Tower, or Dense Server")]')
rackFormFactor.click()
formFactorChangeCheck = dr.find_element_by_xpath('//span[3][contains(text(),"Change")]')
formFactorChangeCheck.click()
patternName = dr.find_element_by_xpath('//input[contains(@id, "templateName")]')
patternName.send_keys('Rack Pattern from scratch')
patternDesciption = dr.find_element_by_xpath('//textarea[contains(@id, "templateDescription")]')
patternDesciption.send_keys('Description test for rack server')
nextButton = dr.find_element_by_xpath('//span[3][contains(text(),"Next")]')
nextButton.click()
nextButton.click()
nextButton.click()
nextButton.click()
sysInfoCreate = dr.find_element_by_xpath('//img[contains(@id, "systmplcreateicon")]')
manIntCreate = dr.find_element_by_xpath('//img[contains(@id, "ethtmplcreate")]')
sysInfoCreate.click()
#System infromation pattern creation box
dr.find_element_by_xpath('//input[contains(@id,"name-field")][contains(@id,"SystemInfoPattern")]').send_keys('Rack_server')
dr.find_element_by_xpath('//textarea[contains(@id, "SystemInfoPattern")]').send_keys('rack test description for system info pattern')
dr.find_element_by_xpath('//span[3][contains(text(), "Custom")]').click()
cusText = dr.find_element_by_xpath('//option[1]')
sysLoc = dr.find_element_by_xpath('//option[2]')
incrNum = dr.find_element_by_xpath('//option[3]')
cusText.click()
addButton = dr.find_element_by_xpath('//img[1][contains(@class, "MoveRightIcon")]')
addButton.click()
dr.find_element_by_xpath('//input[contains(@id, "ValidationTextBox")][contains(@aria-invalid,"true")]').send_keys('Rack_')
dr.find_element_by_xpath('//span[3][contains(text(),"Add")][contains(@id,"form")]').click()
sysLoc.click()
addButton.click()
incrNum.click()
addButton.click()
dr.find_element_by_xpath('//input[contains(@id, "contact-field")]').send_keys('Auto_User')
dr.find_element_by_xpath('//input[contains(@id, "location-field")]').send_keys('Auto_loc')
dr.find_element_by_xpath('//span[3][contains(text(),"Create")]').click()
#System managment pattern
manIntCreate.click()
dr.find_element_by_xpath('//input[contains(@id,"managementinterfacetemplate_patternname")]').send_keys('Rack Management Pattern')
dr.find_element_by_xpath('//textarea[contains(@id,"managementinterfacetemplate_description")]').send_keys('rack test description for system managment pattern')
dr.find_element_by_xpath('//span[3][contains(text(), "Custom")]').click()
cusText = dr.find_element_by_xpath('//option[1]')
sysLoc = dr.find_element_by_xpath('//option[2]')
incrNum = dr.find_element_by_xpath('//option[3]')
cusText.click()
addButton = dr.find_element_by_xpath('//img[1][contains(@class, "MoveRightIcon")]')
addButton.click()
dr.find_element_by_xpath('//input[contains(@id, "ValidationTextBox")][contains(@aria-invalid,"true")]').send_keys('Rack_')
temp = dr.find_elements_by_xpath('//span[3][contains(text(),"Add")][contains(@id,"form")]')
isDisplayed(temp).click()
