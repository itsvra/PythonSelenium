import unittest
from selenium import webdriver
import POM_SS2003

class DiskUsage(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.PhantomJS()
         
    def test_disk_usage(self):
        
        page = POM_SS2003.Page(self.driver)
        page.Launch() 
        page.go_to_Administration()
        
        
        self.database_size = self.driver.find_element_by_xpath('//*[@id="systemstatus"]/table/tbody/tr[4]/td').text
        self.freedisk_size = self.driver.find_element_by_xpath('//*[@id="systemstatus"]/table/tbody/tr[5]/td').text
        
        self.total_disk_size = float(self.database_size) + float(self.freedisk_size)
        
        print 'Total disk size is:', self.total_disk_size
        
        self.disk_usage_element = self.driver.find_element_by_xpath('//div[@class="contentBoxContent"]/script').get_attribute('text')
        
        print self.driver.find_element_by_xpath('//div[@class="contentBoxContent"]/script').get_attribute('text')
        
        current_axis = self.disk_usage_element.strip()
        
        self.disk_usage =  float(current_axis[-20:].replace('"]]}};',"")) # if error occurs change it to -19 0r -21
        
        print 'Total disk usage is:', self.disk_usage
        
        #=======================================================================
        # Disk Usage should not be greater than total disk size
        # 
        #=======================================================================
        
        self.assertGreater(self.total_disk_size, self.disk_usage, 'Current disk usage is greater than total disk size')
        
        
        
    def tearDown(self):
       
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()  
    