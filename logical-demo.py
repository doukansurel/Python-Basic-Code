#Soru 1 -
#i = int(input("Bir Sayı Giriniz :"))
#result = (i>0) and (i<100)
#print(result)

#Soru 2 - 
# i = int(input("Bir sayı giriniz : "))
#result = (i%2==0)
# print(f"Sayı çiftmidir ? {result}")
 
#Soru 3 -
# email = input("Email i giriniz : ")
# password = input("Şifreyi giriniz : ")
# result= (email=="doukan.surel@gmail.com".strip())and(password=="123456")  
# print(result)

#Soru 4 - 
# i = int(input("1.Sayıyı girin : "))
# i2 = int(input("2.Sayıyı girin : "))
# i3 = int(input("3.Sayıyı girin : "))
# result = [i,i2,i3]
# result.sort()
# print(result)

#Soru 5 - 
#vize1 = int(input("Vize notu giriniz : "))
#vize2 = int(input("Vize 2.ci notunuzu giriniz :"))
#final = int(input("Final notunu giriniz : "))
#average = (vize1*0.6)+(vize2*0.6)+(final*0.4)
#finalResult = (final>=50)
#print(f"Öğrencini vize1 notu {vize1} olup , vize2 notu {vize2} , final notu ise {final} dir. \n Öğrencini dersten geçebilme durumu : {finalResult}")

#Soru 6 - 
name = input("Adı girin : ")
surname = input("Soyadı girin : ")
hg = float(input("Boyu girin : "))
kg = float(input("Kiloyu girin :"))
index = (kg) / (hg**2) 
zayıf= (index >=0) and (index<=18.4)
normal = (index >=18.5) and (index<= 24.9)
kilolu = (index>=24.9) and (index <=29.9)
obez = (index >=29.9) and (index <= 34.9)
print(f"{name} {surname}  adlı kişinin indexi : {index} tir. Zayıf mmıdır ? : {zayıf} ")
print(f"{name} {surname}  adlı kişinin indexi : {index} tir. Normal midir ? : {normal} ")
print(f"{name} {surname}  adlı kişinin indexi : {index} tir. Kilolu mudur ? : {zayıf} ")
print(f"{name} {surname}  adlı kişinin indexi : {index} tir. Obez midir ? : {zayıf} ")


