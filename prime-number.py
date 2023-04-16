#Soru - Girilen bir sayının asal olup olmadığını bulma
asalmi = True
num = int(input("Sayıyı girin : "))

if (num==1) :
    print("Sayı asal değildir.")

for i in range(2,(num)):
    if(num%i==0):
        asalmi=False
        break
if asalmi : 
    print("Sayı Asaldır.")
else : 
    print("Sayı asal değil.")