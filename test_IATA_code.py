import unittest
from selenium import webdriver
import POM
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchViaCode(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_search(self):
        
        page = POM.Page(self.driver)
        page.launch()
        
        page.check_round_trip_enabled()
        
        page.is_passenger_option_displayed()
        
        page.is_seat_type_displayed()
        
        page.is_default_location_selected()
        
        #=======================================================================
        # verify specified airport appears in a list of options, from the IATA CODE
        #=======================================================================
        
        page.go_to_destination()
        
        self.driver.switch_to_active_element()
        
        self.driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input').send_keys('SAN')
        
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.fsapp-option-city-name"), 'San Diego, USA')
            )
        
        
        self.driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input').clear()
        
        self.driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input').send_keys('PSP')
        
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.fsapp-option-city-name"), 'Palm Springs, USA')
            )
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

        