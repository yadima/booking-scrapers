from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox()
#driver.implicitly_wait(10)
driver.get('http://booking.com')
elem = driver.find_element_by_name("ss")
elem.send_keys("Berlin")
#WebDriverWait(driver, 1, poll_frequency=0.1).\
#    until(lambda drv: len(drv.find_elements_by_css_selector("ul.ui-autocomplete li")) > 0)
driver.find_element_by_css_selector("ul.ui-autocomplete li").click()
driver.find_element_by_css_selector("#availcheck").click()
driver.find_element_by_css_selector("#searchbox_btn").submit()
for link in driver.find_elements_by_css_selector("a.hotel_name_link"):
    print(link.text)
