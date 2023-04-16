from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://www.youtube.com/"

driver.get(url)

time.sleep(2)

driver.maximize_window()
print(driver.title)
url = "https://www.youtube.com/c/Bar%C4%B1%C5%9F%C3%96zcan"

driver.get(url)

time.sleep(2)
if "BarışÖzcan" in driver.title : 
    driver.save_screenshot("deneme.png")
else:
    print("Hatalı")
driver.back()



time.sleep(2) 
driver.close()
