import unittest
from datetime import datetime
from time import sleep

from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BookFlighTicket(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_generate_itenary(self):
        
        self.driver.get('https://www.google.com/flights/beta')

        #=======================================================================
        # Enter Destination 
        #=======================================================================
        self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[3]').click()

        self.driver.switch_to_active_element()

        #=======================================================================
        # Empty search without a date
        #=======================================================================
        
        self.driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input').send_keys('Chennai')
        sleep(1)
        
        for _ in range(2):
            ActionChains(self.driver).key_down(Keys.ENTER).perform()

        #from date
        self.driver.implicitly_wait(10) #this will execute as soon as the element is available, 10 sec is timneout
        self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[1]/div/div[2]/div[5]/div[1]/div[3]/span').click()

        self.driver.switch_to_active_element()

        # date calculation strategy
        date_after_month = datetime.today()+ relativedelta(months=1)
        date_after_month_plus_two_weeks = datetime.today()+ relativedelta(months=1, weeks=2)

        print 'Today: ',datetime.today().strftime('%d/%m/%Y')
        print 'After a Month from todays date:', date_after_month.strftime('%d/%m/%Y') #this goes to departure date
        print 'After a Month + 2 weeks:', date_after_month_plus_two_weeks.strftime('%d/%m/%Y') #this goes to arrival date

        departure_date = date_after_month.strftime('%d/%m/%Y') 
        return_date = date_after_month_plus_two_weeks.strftime('%d/%m/%Y')

        
        #=======================================================================
        # Enter departure and return date
        #=======================================================================
        
        sleep(1)
        
        self.driver.find_element_by_xpath('//*[@id="flt-modaldialog"]/div/div[4]/div[2]/div[1]/date-input/input').send_keys(departure_date)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="flt-modaldialog"]/div/div[4]/div[2]/div[1]/date-input/input').send_keys(Keys.ENTER)
        
        sleep(1)
    
        self.driver.find_element_by_xpath('//*[@id="flt-modaldialog"]/div/div[4]/div[2]/div[3]/date-input/input').send_keys(return_date)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="flt-modaldialog"]/div/div[4]/div[2]/div[1]/date-input/input').send_keys(Keys.ENTER)


        elem = self.driver.find_element_by_xpath('//*[@id="flt-modaldialog"]/div/div[5]/g-raised-button/div/jsl')

        ac = ActionChains(self.driver)
        ac.move_to_element(elem).move_by_offset(842, 575).click(elem).perform()

        sleep(5)

        #expand best departure flights
        self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[2]/ol/li[1]/div/div[1]/div[2]/div[2]/div').click()
        
        print 'Travel Type Selected by default in google flight page:', self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[2]/ol/li[1]/div/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]').text
        
        is_rountrip_enabled = self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[2]/ol/li[1]/div/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]').text
    
        self.assertEqual(is_rountrip_enabled, 'returrejse', 'Round trip is not enabled by default')

        
        # final result! check if the user has best flights & other flights available if not fail the test :(
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[2]/h4/span/jsl[3]/jsl[1]/jsl[1]').text, 'Bedste udrejseafgange', 'Best flights not found!)')

        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[4]/div[1]/div[1]/h4/span/jsl[1]/jsl[2]/jsl[1]/jsl[1]').text, 'Andre udrejseafgange', 'Other flights not found!')
        
        # departure details is generated?
        if self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[2]/ol/li[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]/span[3]').text == 'Afgang':
            print 'Best Departure Flight Details Generated!'
        else:
            raise Exception("Departure Details are not generated as expected!")
        
        #selected departure date
        selected_departure_date = self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[1]/div/div[2]/div[5]/div[1]/div[3]/span').text
        
        #selected return date
        selected_return_date = self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[1]/div/div[2]/div[5]/div[3]/div[2]/span').text
        
        # date in departure flight 
        date_in_departure_best_flights = self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[2]/ol/li[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/span[3]').text
        
        #make sure that selected date is equal to the departure date in best flights option
        self.assertEqual(selected_departure_date, date_in_departure_best_flights, 'The selected date and date in selected departure flight does not match!')
                                                              
        sleep(5)
        
        #select the departure flight after expanding the best flights
        self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[2]/ol/li[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/jsl[1]').click()
        
        sleep(5)
        
        # expand best returning flight
        self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[2]/ol/li[1]/div/div[1]/div[2]/div[2]/div').click()
        
       
        if self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[2]/ol/li[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]/span[4]').text == 'Hjemrejse':
            print 'Best Return Flight Details Generated!' 
        else:
            print 'Return flight info are not generation as expected!'   
                
        
        # date in return_flight
        date_in_return_best_flights =  self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[2]/ol/li[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/span[3]').text
        
        #make sure that selected date is equal to the departure date in best flights option
        self.assertEqual(selected_return_date, date_in_return_best_flights, 'selected return date does not match the date in selected return flight does not match!')
        
        sleep(5)
        #select the returning flight after expanding the best flights
        self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[5]/div[1]/div[2]/div[5]/div[2]/ol/li[1]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/jsl[1]').click()
        
        
        if self.driver.find_element_by_xpath('//*[@id="flt-app"]/div[2]/div[2]/div[3]/div[1]/ol/li[3]/span').text == 'Rejseoversigt':
            print 'Test completed! Intenary Generated!'
        else:
            raise Exception('Itenary is not generated successfully!')
         
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()