import datetime
import unittest

from selenium import webdriver

import POM_es


class Systemlog(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
    
    def test_system_log(self):
        page = POM_es.Page(self.driver)
        page.launch()
        page.go_to_fault_handling()
        page.go_to_system_logs()
        
        # uncheck the attention rtequired
        self.driver.find_element_by_xpath('//*[@id="showAttentionRequired"]').click()
        
        # apply
        self.driver.find_element_by_xpath('//*[@id="apply"]').click()
        
        # reg-ss
        self.driver.find_element_by_xpath(
            '//td/a[text()="Short Circuit on ICP channel 1"]/../../td/../td/../td[text()="reg-ss"]/../td[text()="REG-SS/Msys35AutTest/Signal2, nu med komma"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Short Circuit on ICP channel 1 reg-ss is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Short Circuit on ICP channel 5"]/../../td/../td/../td[text()="reg-ss"]/../td[text()="REG-SS/Msys35AutTest/Signal6"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since short Circuit on ICP channel 5 reg-ss is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Short Circuit on ICP channel 0"]/../../td/../td/../td[text()="reg-ss"]/../td[text()="REG-SS/Msys35AutTest/Signal"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Short Circuit on ICP channel 0 reg-ss is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        """
        self.driver.find_element_by_xpath('//td/a[text()="Short Circuit on ICP channel 4"]/../../td/../td/../td[text()="reg-ss"]/../td[text()="REG-SS/Msys35AutTest/Signal5"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text 
        current_date = datetime.datetime.today() 
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
       self.assertFalse(difference > 7, 'sys log is not updated for more than a week! Please check the output for more details.')   
        self.driver.back()
        
        """
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Short Circuit on ICP channel 3"]/../../td/../td/../td[text()="reg-ss"]/../td[text()="REG-SS/Msys35AutTest/Signal4"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Short Circuit on ICP channel 3 reg-ss is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Short Circuit on ICP channel 2"]/../../td/../td/../td[text()="reg-ss"]/../td[text()="REG-SS/Msys35AutTest/Signal3"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Short Circuit on ICP channel 2 reg-ss is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 5"]/../../td/../td/../td[text()="reg-2012-nj"]/../td[text()="reg-2012-nj/Msys93/InvalidCurrBeerSens"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 5 reg-2012-nj is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 4"]/../../td/../td/../td[text()="reg-2012-nj"]/../td[text()="reg-2012-nj/Msys93/InvalidCurrSens"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 4 reg-2012-nj is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 3"]/../../td/../td/../td[text()="reg-2012-nj"]/../td[text()="reg-2012-nj/Msys93/CheseProxSens"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 3 reg-2012-nj is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Short Circuit on ICP channel 2"]/../../td/../td/../td[text()="reg-2012-nj"]/../td[text()="reg-2012-nj/Msys93/CheeseSens"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Short Circuit on ICP channel 2 reg-2012-nj is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 1"]/../../td/../td/../td[text()="reg-2012-nj"]/../td[text()="reg-2012-nj/Msys93/ProxSens"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 1 reg-2012-nj is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 0"]/../../td/../td/../td[text()="reg-2012-nj"]/../td[text()="reg-2012-nj/Msys93/Signal"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 0 reg-2012-nj is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        # reg-ss-2003
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 1"]/../../td/../td/../td[text()="regss-2003"]/../td[text()="REG-SS-2003/Msys111AutTest2/Signal2, nu med komma"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 1 regss-2003 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 2"]/../../td/../td/../td[text()="regss-2003"]/../td[text()="REG-SS-2003/Msys111AutTest2/Signal3"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 2 regss-2003 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 3"]/../../td/../td/../td[text()="regss-2003"]/../td[text()="REG-SS-2003/Msys111AutTest2/Signal4"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 3 regss-2003 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 4"]/../../td/../td/../td[text()="regss-2003"]/../td[text()="REG-SS-2003/Msys111AutTest2/Signal5"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 4 regss-2003 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 6"]/../../td/../td/../td[text()="regss-2003"]/../td[text()="REG-SS-2003/Msys111AutTest2/Signal7"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 6 regss-2003 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 7"]/../../td/../td/../td[text()="regss-2003"]/../td[text()="REG-SS-2003/Msys111AutTest2/Signal8"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 7 regss-2003 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 8"]/../../td/../td/../td[text()="regss-2003"]/../td[text()="REG-SS-2003/Msys111AutTest2/Battery"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 8 regss-2003 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 9"]/../../td/../td/../td[text()="regss-2003"]/../td[text()="REG-SS-2003/Msys111AutTest2/Power Supply"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 9 regss-2003 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Short Circuit on ICP channel 0"]/../../td/../td/../td[text()="regss-2003"]/../td[text()="REG-SS-2003/Msys111AutTest2/Signal"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Short Circuit on ICP channel 0 regss-2003 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Short Circuit on ICP channel 5"]/../../td/../td/../td[text()="regss-2003"]/../td[text()="REG-SS-2003/Msys111AutTest2/Signal6"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Short Circuit on ICP channel 5 regss-2003 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        # reg-ss-2012
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 0"]/../../td/../td/../td[text()="reg-ss-2012"]/../td[text()="ss-2012/Aaeon6350/Main bearing"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 0 reg-ss-2012 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 1"]/../../td/../td/../td[text()="reg-ss-2012"]/../td[text()="ss-2012/Aaeon6350/Planet"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 1 reg-ss-2012 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 2"]/../../td/../td/../td[text()="reg-ss-2012"]/../td[text()="ss-2012/Aaeon6350/Highspeed"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 2 reg-ss-2012 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 3"]/../../td/../td/../td[text()="reg-ss-2012"]/../td[text()="ss-2012/Aaeon6350/IMS"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 3 reg-ss-2012 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 4"]/../../td/../td/../td[text()="reg-ss-2012"]/../td[text()="ss-2012/Aaeon6350/Generator DE"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 4 reg-ss-2012 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
        
        self.driver.back()
        
        self.driver.find_element_by_xpath(
            '//td/a[text()="Open Circuit on ICP channel 5"]/../../td/../td/../td[text()="reg-ss-2012"]/../td[text()="ss-2012/Aaeon6350/Generator NDE"]/../td/a').click()
        element = self.driver.find_element_by_xpath('//*[@id="details"]/table/tbody/tr[10]/td').text
        current_date = datetime.datetime.today()
        last_update = datetime.datetime.strptime(element, '%Y-%m-%d %H:%M:%S')
        difference = (current_date - last_update).days
        print "Number of days since Open Circuit on ICP channel 5 reg-ss-2012 is updated:", difference
        self.assertFalse(difference > 7,
                         'sys log is not updated for more than a week! Please check the output for more details.')
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
