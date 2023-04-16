from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome()
url = "https://github.com/"
driver.get(url)

time.sleep(1)

searchInput = driver.find_element_by_name("q")
time.sleep(2)
driver.maximize_window()
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
#result = driver.find_elements_by_css_selector(".repo-list-item h3 a")
result = driver.find_elements_by_xpath("//*[@id='js-pjax-container']/div/div[3]/div/ul/li[1]")
for element in result:
    print(element.text)
driver.minimize_window()
time.sleep(1)
driver.close()