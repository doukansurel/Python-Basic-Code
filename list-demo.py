
carList = ["BMW","Mercedes","Opel","Mazda"]
#Soru 1 - 
result =len(carList)

#Soru 2 -
#print(carList[0])
#print(carList[3])

#Soru 3 -
carList[3]="Toyata"
result = carList

#Soru 4 - 
result = "Mercedes" in carList  

#Soru 5 -
result = carList[-2] 

#Soru 6 -
result = carList[0:3] 

#Soru 7 -
carList[3] = "Renault"
result = carList

#Soru 8 -
result = carList + ['Nissan','Auidi']

#Soru 9 - 
del carList[-1]
result = carList

#Soru 10 -  
result = carList[: : -1]

#Soru 11 - 
studentA = ["Yigit Bilginer",2010,[70,60,70]]
studentB = ["Sena Turan",1999,[80,80,70]]
studentC = ["Ahmet Çakıcı",1998,[80,70,90]]

studentsList = [[studentA]+[studentB]+[studentC]]
result = studentsList
print(result)