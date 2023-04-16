from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time 

def scrol():
  lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
  match=False
  #while(match==False):
  for i in range(8): 
    lastCount = lenOfPage  
    button = browser.find_element_by_xpath("/html/body/div[2]/main/div[4]/div[4]/a")
    button.click()
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    
  if i == 7: 
    match = True

  #if lastCount == lenOfPage:
  #    match=True

prostat_kanser_url = "https://www.aa.com.tr/tr/search/?s=prostat+kanseri"
browser = webdriver.Chrome()
browser.get(prostat_kanser_url)
scrol()