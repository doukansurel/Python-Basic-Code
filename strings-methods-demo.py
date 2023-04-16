
webSite= "http://www.sadikturan.com"

course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#Soru 1 -
#greeting = " Hello World ".strip()
#print(greeting)

#Soru 2 -
result= "www.sadikturan.com".strip("w.com")

#Soru 3 -
result = course.lower()

#Soru 4 - 
result = course.count("a")

#Soru 5 - 
result = webSite.startswith("www")
result = webSite.endswith(".com") 

#Soru 6 - 
result = webSite.find(".com")

#Soru 7 - 
result = course.isalpha()         #Hepsinin alfabetik olup olmadığını sorguladık.  
result = course.isdigit()         #Hepsinin sayı olup olmadığını sorguladık.

#Soru 8 - 
result = "Contents".center(50)

#Soru 9 -
result = course.replace(" ","*")

#Soru 10 - 
result = "Hello World".replace(" World", " There")

#Soru 11 -
result = course.split(" ")































print(result)