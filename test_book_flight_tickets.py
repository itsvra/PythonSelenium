import unittest
from datetime import datetime
from time import sleep

import POM
from dateutil.relativedelta import relativedelta

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BookFlightTicket(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_generate_itenary(self):
        
        page = POM.Page(self.driver)
        page.launch()
        
        #=======================================================================
        # check primary &secondary conditions (other fields are validated as part of the test)
        #=======================================================================
        page.check_round_trip_enabled()
        
        page.is_passenger_option_displayed()
        
        page.is_seat_type_displayed()
        
        page.is_default_location_selected()
        
        # =======================================================================
        # Enter Destination
        # =======================================================================
        page.go_to_destination()
        
        self.driver.switch_to_active_element()
        
        # =======================================================================
        # make sure empty search with default date works
        # =======================================================================
        
        self.driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input').send_keys('London')
        sleep(1)
        
        for _ in range(2):
            ActionChains(self.driver).key_down(Keys.ENTER).perform()
        
        # from date
        self.driver.implicitly_wait(10)  # this will execute as soon as the element is available, 10 sec is timneout
        
        page.go_to_calender()
        
        self.driver.switch_to_active_element()
        
        # =======================================================================
        # date calculation strategy
        # =======================================================================
        
        date_after_month = datetime.today() + relativedelta(months=1)
        date_after_month_plus_two_weeks = datetime.today() + relativedelta(months=1, weeks=2)
        
        print 'Todays date:', datetime.today().strftime('%d/%m/%Y')
        print 'After a Month from todays date:', date_after_month.strftime('%d/%m/%Y')  # this goes to departure date
        print 'After a Month + 2 weeks:', date_after_month_plus_two_weeks.strftime(
            '%d/%m/%Y')  # this goes to arrival date
        
        departure_date = date_after_month.strftime('%d/%m/%Y')
        return_date = date_after_month_plus_two_weeks.strftime('%d/%m/%Y')
        
        # =======================================================================
        # Enter departure and return date
        # =======================================================================
        
        sleep(1)
        
        self.driver.find_element_by_xpath(
            '//div[2]/div[1]/date-input/input').send_keys(departure_date)
        
        sleep(1)
        
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        
        sleep(1)
        
        self.driver.find_element_by_xpath(
            '//div[2]/div[3]/date-input/input').send_keys(return_date)
        sleep(1)
        
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        
        elem = self.driver.find_element_by_xpath('//jsl')
        
        ac = ActionChains(self.driver)
        ac.move_to_element(elem).move_by_offset(842, 575).click(elem).perform()
        
        sleep(5)
        
        # =======================================================================
        # expand best departure flight
        # =======================================================================
        page.expand_best_departure_flights()
        
        # =======================================================================
        # check list of best flights & other flights are populated
        # =======================================================================
        try:
            self.driver.find_element_by_xpath("//jsl[contains(text(), 'Bedste udrejseafgange')]")
            self.driver.find_element_by_xpath("//jsl[contains(text(), 'Andre udrejseafgange')]")
        except:
            raise NoSuchElementException("information obtained is not as expected!")
        
        # =======================================================================
        # An expanded itinerary appears, telling me about the flight
        # =======================================================================
        self.assertTrue(self.driver.find_element_by_xpath('//span[text()="Afgang"]'),
                        'Departure flight information not found!')
        
        sleep(5)
        
        # =======================================================================
        # select the departure flight after expanding the best flights
        # =======================================================================
        page.select_flight()
        
        sleep(5)
        
        # =======================================================================
        # expand best returning flight
        # =======================================================================
        page.expand_best_return_flights()
        
        # =======================================================================
        # options of return flights are shown
        # =======================================================================
        self.assertTrue(self.driver.find_element_by_xpath('//span[text()="Hjemrejse"]'),
                        'Return flight information not found!')
        
        sleep(5)
        # =======================================================================
        # select the returning flight after expanding the best flights
        # =======================================================================
        page.select_flight()
        
        # =======================================================================
        # check if itenary is issued
        # =======================================================================
        self.assertTrue(self.driver.find_element_by_xpath('//span[text()="Rejseoversigt"]'),
                        'Itenary is not generated successfully')
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
