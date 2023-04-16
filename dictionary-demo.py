"""students = {"128": {
    "name" : "Ali " , 
    "surname" : "Sürel", 
    "phone" : "05356000000"
},
"120" : {
  "name" : "Zehra", 
  "surname" : "Sireli",
  "phone" : "02520530463"

},
"125" : {
    "name" : "Ahmet",
    "surname" : "Salihli",
    "phone" : "053262510251"
}}"""
#***************************************
"""
students.update({number : {
    "name" : name ,
    "surname"  :surname , 
    "phone" : phone 
}}) """    #Şeklindede yapılabilir...
#*****************************************


students = {}
number = input("Numarasını giriniz : ")
name = input("Adını giriniz : ")
surname = input ("Soyadını giriniz : ")
phone = input ("Telefonunu giriniz : ")

students[number]  = {
   "name" : name,
   "surname" : surname , 
   "phone " : phone 
}

print(students)

#Ögrenci numberdan bilgileri almak 

studentNumber = input("Ögrenci Numarası gir : ")
print(students[studentNumber])