

#===============================================================================
# the code will scroll down 30 time till the bottom of the page and clicks exactly the x and y cordinates of the element
#===============================================================================
import time
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys


#===============================================================================
# ignore the errors you have to add setup method and unittest
#===============================================================================


for _ in range(30):
        
            ActionChains(self.driver).key_down(Keys.DOWN).perform()
            time.sleep(1)
        
            time.sleep(5)
        
            elem = self.driver.find_element_by_link_text("Sync/MaskDeploySync")
        
            ac = ActionChains(self.driver)
            ac.move_to_element(elem).move_by_offset(108, 5607).click(elem).perform()
        
        
            self.driver.find_element_by_id('runsoon').click()
        
            time.sleep(5)
        
            self.driver.find_element_by_id('Save').click()
        
            time.sleep(5)
    
            
