from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://www.aa.com.tr/tr/search/?s=kanser"
driver.get(url)
time.sleep(2)

driver.maximize_window()

url = "https://www.aa.com.tr/tr/gundem"

driver.get(url)
#driver.save_screenshot("anadoluhaber.png")
print(driver.title)
driver.back()

time.sleep(2)

driver.close()