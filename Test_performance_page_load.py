from selenium import webdriver

source = "http://www.babycenter.com/"
driver = webdriver.Chrome()
driver.get(source)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart

print "Back End: %s" % backendPerformance
print "Front End: %s" % frontendPerformance

driver.quit()
