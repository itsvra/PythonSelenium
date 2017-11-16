import unittest
from selenium import webdriver
import POM_es
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class ConsistentTurbine(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.PhantomJS()
        
    def test_consistent_turbine(self):
        
        page = POM_es.Page(self.driver)
        page.Launch()
        
        #=======================================================================
        # sites considered in the test are
        # 1. Mi 2.reg-ss 3.reg-ss-2012 4.regss-2003 5.regss-passive 6.regss-v4 7.vintage2003 8.virtualsite 9.reg-2012-nj
        #=======================================================================
                
        self.OverviewPage_TurbineCount = (int(self.driver.find_element_by_xpath('//*[@id="site_2"]').text[0:1]) + #reg-ss
                                            int(self.driver.find_element_by_xpath('//*[@id="site_3"]').text[0:1]) + #regss-2003
                                            int(self.driver.find_element_by_xpath('//*[@id="site_4"]').text[0:1]) + #regss-v4
                                            int(self.driver.find_element_by_xpath('//*[@id="site_7"]').text[0:1]) + #regss-passive
                                            int(self.driver.find_element_by_xpath('//*[@id="site_6"]').text[0:1]) + #virtual site
                                            int(self.driver.find_element_by_xpath('//*[@id="site_8"]').text[0:1]) + #reg-ss-2012
                                            int(self.driver.find_element_by_xpath('//*[@id="site_9"]').text[0:1]) +  #Mi Site
                                            int(self.driver.find_element_by_xpath('//*[@id="site_10"]').text[0:1]) +  #Vintage 2003
                                            int(self.driver.find_element_by_xpath('//*[@id="site_13"]').text[0:1]))  #reg-2012-nj
                                            
                                                                                      
        print "No: Turbine in Overview Page:", self.OverviewPage_TurbineCount
     
        page.go_to_Administration()       
        page.go_to_Performance()
        
        option_element_sites = WebDriverWait(self.driver,10).until(lambda driver: self.driver.find_element_by_id('sites'))
        Select(option_element_sites).select_by_visible_text('Mi Site')
        Select(option_element_sites).select_by_visible_text('reg-2012-nj')
        Select(option_element_sites).select_by_visible_text('reg-ss')
        Select(option_element_sites).select_by_visible_text('reg-ss-2012')
        Select(option_element_sites).select_by_visible_text('regss-2003')
        Select(option_element_sites).select_by_visible_text('regss-passive')
        Select(option_element_sites).select_by_visible_text('regss-v4')
        Select(option_element_sites).select_by_visible_text('Vintage 2003')
        Select(option_element_sites).select_by_visible_text('Virtual Site')
       
        self.driver.find_element_by_id('apply').click()
        
        self.Performancepage_turbine_count = (len(self.driver.find_elements_by_xpath('//td[text()="reg-ss"]/../td/a[text()="TCM Server" != "*"]')) + 
                                                 
                                                len(self.driver.find_elements_by_xpath('//td[text()="regss-passive"]/../td/a[text()="TCM Server" != "*"]')) +
                                                
                                                len(self.driver.find_elements_by_xpath('//td[text()="regss-2003"]/../td/a[text()="TCM Server" != "*"]')) +
                                                
                                                len(self.driver.find_elements_by_xpath('//td[text()="regss-v4"]/../td/a[text()="TCM Server" != "*"]')) +
                                                
                                                len(self.driver.find_elements_by_xpath('//td[text()="Mi Site"]/../td/a[text()="TCM Server" != "*"]')) +
                                                
                                                len(self.driver.find_elements_by_xpath('//td[text()="reg-2012-nj"]/../td/a[text()="TCM Server" != "*"]')) +
                                                
                                                len(self.driver.find_elements_by_xpath('//td[text()="reg-ss-2012"]/../td/a[text()="TCM Server" != "*"]')) +
                                                
                                                len(self.driver.find_elements_by_xpath('//td[text()="Virtual Site"]/../td/a[text()="TCM Server" != "*"]')) +
                                                
                                                len(self.driver.find_elements_by_xpath('//td[text()="Vintage 2003"]/../td/a[text()="TCM Server" != "*"]')) 
                                            
                                                )
                                                
        
        print "No: Turbine in Performance Page:", self.Performancepage_turbine_count
        
        
        page.go_to_DiskUsage()
        
        self.DiskUsagePage_Turbine_count = (int(self.driver.find_element_by_xpath('//*[@id="siteStatistics"]/tbody/tr[2]/td[2]').text) + int(self.driver.find_element_by_xpath('//*[@id="siteStatistics"]/tbody/tr[3]/td[2]').text) 
                                            + int(self.driver.find_element_by_xpath('//*[@id="siteStatistics"]/tbody/tr[4]/td[2]').text) +  int(self.driver.find_element_by_xpath('//*[@id="siteStatistics"]/tbody/tr[5]/td[2]').text)
                                            + int(self.driver.find_element_by_xpath('//*[@id="siteStatistics"]/tbody/tr[6]/td[2]').text) + int(self.driver.find_element_by_xpath('//*[@id="siteStatistics"]/tbody/tr[7]/td[2]').text)                                         
                                            + int(self.driver.find_element_by_xpath('//*[@id="siteStatistics"]/tbody/tr[8]/td[2]').text)
                                            + int(self.driver.find_element_by_xpath('//*[@id="siteStatistics"]/tbody/tr[9]/td[2]').text)
                                            + int(self.driver.find_element_by_xpath('//*[@id="siteStatistics"]/tbody/tr[12]/td[2]').text))
                                                                                                                                                       
        print "No: Turbine in Disk Usage Page:", self.DiskUsagePage_Turbine_count    
        
                         
        self.assertEqual(self.OverviewPage_TurbineCount, self.Performancepage_turbine_count, "No: of turbines are not equal!")
        self.assertEqual(self.OverviewPage_TurbineCount, self.DiskUsagePage_Turbine_count, "No: of turbines are not equal!")
                                                                                    