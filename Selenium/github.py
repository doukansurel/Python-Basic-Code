
from selenium import webdriver
from githubUserİnfo import username,password
import time 

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username 
        self.password = password 
        self.followers = []

    def loadFollowers(self):
        item = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        for i in item: 
            self.followers.append(i.find_element_by_css_selector(".Link--secondary").text)   


    def SingIn(self):
        url = "https://github.com/login"
        self.browser.get(url)
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()
        time.sleep(2)

    def getFollowers(self): 
        url = "https://github.com/sadikturan?tab=followers"
        self.browser.get(url)
        time.sleep(2)
     
        while True : 
            links = self.browser.find_element_by_class_name("pagination").find_elements_by_tag_name("a")
            if(len(links) == 1 ) :
                if(links[0] =="Next"): 
                    links[0].click()
                    time.sleep(2)
                    self.loadFollowers()
                else : 
                    break 
            else :
                for link in links : 
                    if(link.text == "Next"):
                        link.click()
                        time.sleep(2)
                        self.loadFollowers()
                    else : 
                        continue




github = Github(username , password)
github.SingIn()
github.getFollowers()
print(github.followers)
print(len(github.followers))