from selenium import webdriver
import time
from bs4 import BeautifulSoup
browser = webdriver.Chrome()
browser.get("https://www.aa.com.tr/en/science-technology")
sayfa_kaynağı = browser.page_source
time.sleep(2)
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
button = browser.find_element_by_xpath("/html/body/div/main/div[9]/div[3]/a")
while True:
    
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    button.click()
    time.sleep(3)

      # Calculate new scroll height and compare with last scroll height
    #new_height = browser.execute_script("return document.body.scrollHeight")
    
    
    
    #if new_height == last_height:

    #    break
    
    # last_height = new_height


soup = BeautifulSoup(sayfa_kaynağı, "html.parser")

links = soup.find_all("div",{"class" : "col-sm-12 col-md-6 col-lg-9 col-xl-9 konu-alt-yazi"})
for link in links : 
  href = link.find("a").get("href")
  print(href)
time.sleep(2)