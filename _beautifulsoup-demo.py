from re import findall
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/toptv/"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find("tbody",{"class":"lister-list"}).find_all("tr")
result = ""
count = 1
for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text 
    if (float(rating) > 9 ):
        result = rating
        print(f"{count} - Film Adı : {title.ljust(50)} Çıkış Yılı : {year} Değerlendirme : {result}")

    
    count +=1
#print(list)
