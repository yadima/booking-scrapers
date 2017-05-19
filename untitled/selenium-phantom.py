from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS(service_args=['--ssl-protocol=any'])
driver.implicitly_wait(10)
driver.get('http://www.python.org')
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
#driver.implicitly_wait(20)
elem2 = driver.find_element_by_name("q")
print elem2.get_property("value")
assert "No results" not in driver.page_source
# print(driver.title)
#print driver.page_source
driver.quit()
