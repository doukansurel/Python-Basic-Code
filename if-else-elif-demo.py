
""""
print ("Ehliyet Alma Sistemine Hoşgeldiniz..")
name = input("İsminizi giriniz : ")
age = int(input("Yaşınızı giriniz : "))
educationİnformation = input("Eğitim bilgisini giriniz :")

if (age>=18):
    if(educationİnformation=="Üniversite Mezunu".strip() or educationİnformation=="Lise Mezunu".strip()) :
        print("Kişi Ehliyet alabilir.")
    else : 
        print("Eğitim düzeyiniz lise veya üniversite olmalıdır")
else : 
    print("Yaşınız tutmadığımndan dolayı ehliyet alamazsınız....") 
"""
#************************************************************************************************************
""""
print("Not Hesaplama Sistemine Hoşgeldiniz ...")
exam=int(input("Birinci yazılınızı girin :"))
exam2 =int(input("İkinci yazılınızı girin : "))
viva= int(input("Sözlünüzü girin : "))
total = (exam+exam2+viva) / 3 
if(total >0 and total<=24) :
    result = 0
    print(f"Ortalamanızın değeri : {result}")
elif(total>=25 and total<=44 ):
    result = 1 
    print(f"Ortlamanızın değeri : {result}")
elif(total>= 45 and total<=54 ):
    result = 2 
    print(f"Ortlamanızın değeri : {result}")
elif(total>=55 and total <=69):
    result = 3 
    print(f"Ortlamanızın değeri : {result}")
elif(total>=70 and total<=84 ) : 
    result = 4 
    print(f"Ortlamanızın değeri : {result}")
elif(total>=85 and total <=100):
    result = 4 
    print(f"Ortlamanızın değeri : {result}")

"""
#****************************************************************************

day = int(input("Günü girin : "))
month = int(input("Ayı girin : "))
year = int(input("Yılı girin : "))
date =[day,month,year]
currentdate =[]




