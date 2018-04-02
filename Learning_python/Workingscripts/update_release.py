from selenium import webdriver
import time
import driver

list1 = ['EMC Storage', 'EMS', 'ESW_Automation', 'Eagle', 'EasyStartup', 'EasyUpdate', 'EmbeddedHypervisors', 'Emulex_Ethernet', 'Emulex_FC', 'FPGA', 'GPU', 'GSS_HW', 'GSS_SW', 'Gryphon', 'Gryphon_FC', 'HDD', 'IBM Storwize', 'IFM_BLUE', 'IMM2', 'IMM2GG_BLUE', 'IMM2NGP_BLUE', 'IMM2_BLUE', 'IMM3', 'ISDEV', 'Intel AEP', 'Intel_Flash_PCIe', 'Intel_Network', 'Intel_RAID', 'Internal_Cables', 'Karkinos', 'Kraken', 'LNG_Switches', 'LSI_PCIe_Switch', 'LSI_RAID', 'LSI_SAS_HBA', 'Lenovo Entry SAN', 'Mars', 'Marvell_RAID', 'Materials', 'Mechanical', 'Mellanox_Adapters', 'Mellanox_Switches', 'Memory', 'Mercury', 'NVDIMM', 'NVMe', 'NeoKylin', 'Newport', 'Novell SUSE', 'OB_Video', 'ODD', 'OSPUT', 'OSS_Application', 'OneCli', 'Oracle Linux', 'PCBs', 'PCIe_Slots', 'PMC_SAS_HBA', 'PMTSL', 'Packaging', 'Parallel_Port', 'Pegatron_BLUE', 'Pollux', 'Power Options', 'Power Planner', 'Procyon', 'QLogic_Fibre_Channel_Switches', 'Qlogic_Ethernet', 'Qlogic_FC', 'Qtester', 'RDCLI', 'RHEL', 'SAS_RAID', 'SCCM', 'SCOM', 'SCVMM', 'SD_Card', 'SMM', 'SSD', 'STORAGE_CONTROLLER_PE', 'SV', 'SanDisk_Flash_PCIe', 'Seagate', 'Serial_Port', 'Solarflare', 'Specification', 'System_ECAT', 'System_Power', 'System_grantley 4R1T', 'TCM_DSS', 'TC_ELIE', 'TDM', 'TDM_Diag', 'TMM', 'TPM_TCM', 'TSM', 'TSMCLI', 'TapeDrives', 'Thermal', 'ToolsCenter', 'ToolsCenter_BLUE', 'UEFI2', 'UEFI3', 'UEFI3_BLUE', 'UEFI4', 'UEFI_BLUE', 'USB', 'USB Flash', 'Ubuntu', 'UserManual', 'UxLite', 'UxSP_Master', 'UxSP_Master_BLUE', 'VMWare', 'VSAN', 'Vali', 'Windows', 'XClarity Administrator', 'XClarity_Energy_Manager', 'Xinyi', 'Yilan', 'Z_AMI', 'daan', 'display', 'iBMC', 'keyboard', 'kvm', 'mice', 'rack', 'uEFI', 'vCenter', 'z_Asustek_HW', 'z_Avocent_SW', 'z_Celestica_HW', 'z_Compal_FW', 'z_Compal_HW', 'z_Cubicus_FW', 'z_Cubicus_HW', 'z_Emerson_SW', 'z_Foxconn_HW', 'z_Foxconn_SW', 'z_IEC_FW', 'z_IEC_HW', 'z_MSI_FW', 'z_MSI_HW', 'z_Mitac_HW', 'z_Mitac_SW', 'z_Pegatron_HW', 'z_Pegatron_SW', 'z_USI_FW', 'z_USI_HW', 'z_Wistron_HW', 'z_Wistron_SW', 'AHV', 'AMM', 'Accipiter', 'Audio', 'Avocent_SW_BLUE', 'BIOS', 'Blacktip', 'Bonneville', 'Broadcom', 'Brocade_Switches', 'CMM', 'CMM_BLUE', 'CPU', 'Capacity_Planner', 'Chipsets', 'Cisco_Switch_Products', 'Citrix', 'CoProcessor', 'Compass', 'Compass_FC', 'Compass_Plus', 'Compliance', 'Congo', 'DSA', 'DX8200N', 'Diablo FlashDIMM', 'DiagnosticTool', 'Director_Triage', 'Draco', 'EMC Storage', 'EMS', 'ESW_Automation', 'Eagle', 'EasyStartup', 'EasyUpdate', 'EmbeddedHypervisors', 'Emulex_Ethernet', 'Emulex_FC', 'FPGA', 'GPU', 'GSS_HW', 'GSS_SW', 'Gryphon', 'Gryphon_FC', 'HDD', 'IBM Storwize', 'IFM_BLUE', 'IMM2', 'IMM2GG_BLUE', 'IMM2NGP_BLUE', 'IMM2_BLUE', 'IMM3', 'ISDEV', 'Intel AEP', 'Intel_Flash_PCIe', 'Intel_Network', 'Intel_RAID', 'Internal_Cables', 'Karkinos', 'Kraken', 'LNG_Switches', 'LSI_PCIe_Switch', 'LSI_RAID', 'LSI_SAS_HBA', 'Lenovo Entry SAN', 'Mars', 'Marvell_RAID', 'Materials', 'Mechanical', 'Mellanox_Adapters', 'Mellanox_Switches', 'Memory', 'Mercury', 'NVDIMM', 'NVMe', 'NeoKylin', 'Newport', 'Novell SUSE', 'OB_Video', 'ODD', 'OSPUT', 'OSS_Application', 'OneCli', 'Oracle Linux', 'PCBs', 'PCIe_Slots', 'PMC_SAS_HBA', 'PMTSL', 'Packaging', 'Parallel_Port', 'Pegatron_BLUE', 'Pollux', 'Power Options', 'Power Planner', 'Procyon', 'QLogic_Fibre_Channel_Switches', 'Qlogic_Ethernet', 'Qlogic_FC', 'Qtester', 'RDCLI', 'RHEL', 'SAS_RAID', 'SCCM', 'SCOM', 'SCVMM', 'SD_Card', 'SMM', 'SSD', 'STORAGE_CONTROLLER_PE', 'SV', 'SanDisk_Flash_PCIe', 'Seagate', 'Serial_Port', 'Solarflare', 'Specification', 'System_ECAT', 'System_Power', 'System_grantley 4R1T', 'TCM_DSS', 'TC_ELIE', 'TDM', 'TDM_Diag', 'TMM', 'TPM_TCM', 'TSM', 'TSMCLI', 'TapeDrives', 'Thermal', 'ToolsCenter', 'ToolsCenter_BLUE', 'UEFI2', 'UEFI3', 'UEFI3_BLUE', 'UEFI4', 'UEFI_BLUE', 'USB', 'USB Flash', 'Ubuntu', 'UserManual', 'UxLite', 'UxSP_Master', 'UxSP_Master_BLUE', 'VMWare', 'VSAN', 'Vali', 'Windows', 'XClarity Administrator', 'XClarity_Energy_Manager', 'Xinyi', 'Yilan', 'Z_AMI', 'daan', 'display', 'iBMC', 'keyboard', 'kvm', 'mice', 'rack', 'uEFI', 'vCenter', 'z_Asustek_HW', 'z_Avocent_SW', 'z_Celestica_HW', 'z_Compal_FW', 'z_Compal_HW', 'z_Cubicus_FW', 'z_Cubicus_HW', 'z_Emerson_SW', 'z_Foxconn_HW', 'z_Foxconn_SW', 'z_IEC_FW', 'z_IEC_HW', 'z_MSI_FW', 'z_MSI_HW', 'z_Mitac_HW', 'z_Mitac_SW', 'z_Pegatron_HW', 'z_Pegatron_SW', 'z_USI_FW', 'z_USI_HW', 'z_Wistron_HW', 'z_Wistron_SW']

dr = driver.mycon('bz.labs.lenovo.com')
time.sleep(1)
'''dr.get('https://bz-test.labs.lenovo.com')
time.sleep(2)
dr.find_element_by_id('login_link_top').click()
time.sleep(1)
dr.find_element_by_id('Bugzilla_login_top').send_keys('scripts@lenovo.com')
time.sleep(1)
dr.find_element_by_id('Bugzilla_password_top').send_keys('Auto1234')
time.sleep(1)
dr.find_element_by_id('log_in_top').click()
time.sleep(1)
dr.find_element_by_id('Bugzilla_login').send_keys('scripts@lenovo.com')
dr.find_element_by_id('Bugzilla_password').send_keys('Auto1234')
time.sleep(1)
dr.find_element_by_id('log_in').click()
time.sleep(1)'''

def updaterelease(dr):
    time.sleep(2)
    dr.find_element_by_id('version').clear()
    dr.find_element_by_id('version').send_keys('Async OS Bus - ESXi 6.7 (Apr 2018)')
    dr.find_element_by_id('update').click()
    time.sleep(1)

for product in list1:
    dr.get('https://bz.labs.lenovo.com/editversions.cgi?action=edit&product='+product+'&version=Async%20OS%20Bus%20-%20ESXi%206.7%20(Dec%202017)')
    try:
        dr.find_element_by_id('error_msg')
        continue
    except:
        updaterelease(dr)

dr.exit()
    
    
