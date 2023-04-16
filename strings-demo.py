
webSite= "http://www.sadikturan.com"

course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#soru 1 - 
#print("Course Character number : ",len(course))

#soru 2 -
#print( webSite[7:10])        #İstenilen kelimeyi bulma

#soru 3 -
#print(webSite[22:25])       #İstenilen kelimeyi bulma

#soru 4 -
result = course[0:15]       #İstenilen Konumdan yazma
#print(result)
result = course[-15:]
#print(result)

#soru 5 -               #Tersten Yazma
#print(course[::-1])

#soru 6 - 
name , surname , age , job = ("Bora","Yılmaz",35,"Mühendis")
greeting = "Benim adım " + name +" "+ surname+", "+"Yaşım "+str(age)+" ve mesleğim "+job
greeting = "Benim adım {}  {}, Yaşım {} ve mesleğim  {} ." .format(name,surname,age,job)
greeting = f"Benim adım {name}  {surname}, Yaşım {age} ve mesleğim  {job} ."
#print(greeting)

#soru 7 -
#s = "Hello world"
#print(s[0:6]+"W"+s[-4:])

#soru 8 - 
s = "abc"
print(s*3)


