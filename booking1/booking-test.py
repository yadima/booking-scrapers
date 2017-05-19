from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.PhantomJS(service_args=['--ssl-protocol=any'])
driver.implicitly_wait(10)
driver.get('http://www.booking.com')
assert "Booking" in driver.title

print driver.title
elem = driver.find_element_by_name("ss")
elem.send_keys("Italy")

WebDriverWait(driver, 1, poll_frequency=0.1).until(lambda drv: len(drv.find_elements_by_css_selector("ul.ui-autocomplete li")) > 0)

elem.send_keys(Keys.ENTER)

print driver.page_source
#driver.implicitly_wait(20)
#elem2 = driver.find_element_by_name("ss")
#print elem2.get_property("placeholder")
assert "properties found" not in driver.page_source

#print(driver.title)
#print driver.page_source
driver.quit()
