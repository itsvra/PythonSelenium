import unittest
from selenium import webdriver
import time





class SpinUp(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        
        
    def test_spin_up(self):
        
        self.driver.get('http://192.168.3.21')
        
        if self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[2]').text != "iso_rms":
            
            return None
            
        elif self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[2]').text == "iso_rms":
            
            print 'The web is running in iso_rms mode'
        
        
        self.driver.get('http://192.168.3.21/data/index.php?mode=iso_rms')
        
        refresh_time_in_seconds = 1
        
        t_end = time.time() + 60 * 30
        
        #The test will run for 1800 seconds if the site is in iso_rms mode
        
        while time.time() < t_end:
            self.driver.refresh()
            time.sleep(refresh_time_in_seconds)
        
        
            print self.driver.find_element_by_tag_name('body').text
            
    
    def tearDown(self):
       
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()