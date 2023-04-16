
from selenium import webdriver
import time 
from ınstaUserİnfo import username,password
from selenium.webdriver.common.keys import Keys

class Instagram:
    def __init__(self,username , password ):
        self.browser = webdriver.Chrome()
        self.username = username 
        self.password = password
    def SıngIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        sıngIn_button = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        sıngIn_button.click()
        time.sleep(4)

    def getFollowers(self):
        self.browser.get("https://www.instagram.com/doukan.surel/")
        time.sleep(1.5)
        follower = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/ul/li[2]/a')
        follower.click()
        time.sleep(3)
       
        
    
ınsta = Instagram(username,password)
ınsta.SıngIn()
ınsta.getFollowers()