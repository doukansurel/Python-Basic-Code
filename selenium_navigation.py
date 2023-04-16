from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "https://github.com/search?q="
driver.get(url)


driver.maximize_window()
searchInput = driver.find_element_by_xpath('//*[@id="search_form"]/div/div/input[1]')
#searchInput = driver.find_element_by_name("q")
time.sleep(2)
searchInput.send_keys("python")
time.sleep(3)
searchInput.send_keys(Keys.ENTER)
time.sleep(4)
result = driver.page_source
print(result)
#result = driver.find_element_by_css_selector(".repo-list-item text-normal a")
#for element in result:
#    print(element.text)

driver.close()