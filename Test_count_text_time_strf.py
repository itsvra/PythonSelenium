from selenium import webdriver
from time import sleep

from datetime import datetime

print datetime.today().strftime('%Y%m%d')

date = datetime.today().strftime('%Y%m%d')

driver = webdriver.Firefox()

driver.get('http://reg-ss/tcm_logs/httpd')



driver.find_element_by_partial_link_text(date).click()

b = driver.find_element_by_tag_name('body').text
        
print b.count("database.php")

driver.quit()