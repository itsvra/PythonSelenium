import unittest
from selenium import webdriver
import POM_CP

class Administration_Resource(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.PhantomJS()
          
    def test_administration_resource(self):
        
        page = POM_CP.Page(self.driver)
        page.Launch()
        page.go_to_Administration()
        page.check_if_errors_exists()
        page.go_to_Performance()
        page.check_if_errors_exists()
        page.go_to_Resplication_Status()
        page.check_if_errors_exists()
        page.go_to_Replication_Configuration()
        page.check_if_errors_exists()
        
    def tearDown(self):
       
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main()