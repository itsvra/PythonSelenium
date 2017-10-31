
        #################################### PAGE OBJECT MODEL FOR ENTERPRISE WEB SERVER WINDOWS ########################################


class Page(object):
    
    
    def __init__(self, driver):
        
        self.driver = driver
        
                  
        
        #################################### URL & CREDENTIALS ##################################################################
    
    
    def Launch(self):
        
        self.driver.get("http://reg-es-cp.gramjuhl")
        self.driver.find_element_by_name("username").send_keys('administrator')
        self.driver.find_element_by_name("password").send_keys('system')
        self.driver.find_element_by_name("Login").click()
               
        assert "Overview for reg-es-cp" in self.driver.page_source
               
               
    def Launch_Disk_usage_per_device(self):
        
        self.driver.get("http://reg-es-cp/tcm_v6/ResourceMonitor/disk-usage/graph/all/1")
        self.driver.find_element_by_name("username").send_keys('administrator')
        self.driver.find_element_by_name("password").send_keys('system')
        self.driver.find_element_by_name("Login").click()
               
        assert "Disk Usage Per Device" in self.driver.page_source
           
         
    
        ##################################### ACCESS TO THE LINKS ############################################################
    
            ####################### FAULT HANDLING TAB ############################
    
    def go_to_Fault_Handling(self):
        
        self.Fault_Handling_link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/a').click()
        
    def go_to_Assigned_Faults(self):
        
        self.Assigned_Faults_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/ul/li[1]/a').click()
        
    def go_to_System_Logs(self):
        
        self.System_Logs_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/ul/li[2]/a').click()
        
    def go_to_Components(self):
        
        self.Components_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/ul/li[3]/a').click()
        
    def go_to_Damage_Categories(self):
    
        self.Damage_Categories_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/ul/li[4]/a').click()
        
    def go_to_Risk_Categories(self):
        
        self.Risk_Categories_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[2]/ul/li[5]/a').click()
        
    
                            ################# REPORTING TAB ################
    
    
    def go_to_Reporting(self):
        
        self.Reporting_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[3]/a').click()
        
    def go_to_CSV_Reports(self):
        
        self.CSV_Reports_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[3]/ul/li[2]/a').click()
        
        
    
                            ################# TCM CONFIGURATION TAB ################################
    
    
    def go_to_TCM_Configration(self):
    
        self.TCM_Configuration_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[4]/a').click()
    
    
    def go_to_Machine_Model(self):
        
        self.Machine_Model_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[4]/ul/li[3]/a').click()
        
    def go_to_Mask_Report(self):
        
        self.Mask_Report_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[4]/ul/li[1]/a').click()
    
    
                            ############## ADMINISTRATION TAB ####################################
    
    
    def go_to_Administration(self):
        
        self.Administration_Link = self.driver.find_element_by_link_text('Administration').click()
        
    def go_to_Users(self):
        
        self.users_link = self.driver.find_element_by_link_text('Users').click()
        
        
    def go_to_Performance(self):
        
        self.Performance_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[5]/ul/li[3]/a').click()
        
        
    def go_to_Resplication_Status(self):
        
        self.Replication_Status_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[5]/ul/li[4]/a').click()
        
    def go_to_Replication_Configuration(self):
        
        self.Replication_Configuration_Link = self.driver.find_element_by_link_text('Replication Configuration').click()
        
    def go_to_Scheduler(self):
        
        self.Scheduler_Link = self.driver.find_element_by_link_text('Scheduler').click()
        
    def go_to_DiskUsage(self):
        
        self.DiskUsage_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[5]/ul/li[8]/a').click()  
        
    def go_to_Licenses(self):
        
        self.Licenses_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[5]/ul/li[9]/a').click()  
        
        #################################### HELP TAB ###########################################################
        
    def go_to_Help(self):
        
        self.Help_Link = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[6]/a').click()
        
    def go_to_OcularDownloads(self):
        
        self.Ocular_Downloads = self.driver.find_element_by_xpath('//*[@id="navigation"]/ul/li[6]/ul/li/a').click()
        
        
        ##################################### VERIFY THAT IT EXISTS ######################################################
    
    
    def check_if_cookies_exists(self):
        
        cookies = self.driver.get_cookie('tcm_v6_sess')
         
        print cookies
      
    def check_if_errors_exists(self):
        
        get_url = self.driver.current_url
        
        print get_url
        
        assert "An error occured, consult the logs for details." not in self.driver.page_source