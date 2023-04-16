#Rastgele 1 den 100 e kadar sayı oluşturulacak 
#can sayısı olacak
#yakınlaşma ve uzaklaşmaya göre sıcak soğuk diye bilgi verecek
#doğru yaptığı her soru 20 puan toplamda 100 puan

remainingRight = 5 
point = 100
import random 
num =random.randint(0,10)
sayac = 0
while remainingRight > 0 : 
    remainingRight-=1
    point-=20
    
    sayac +=1
    selection = int(input("tahmin girin : "))
    if(num>selection):
        print("YUKARI")
       
    elif(num==selection):
        print(f"Tebrikler.{sayac} tahmininizde doğru bildiniz...Toplam Puanınız : {point}".center(50,"*"))
        sayac+=1
        break
    else:
        print("AŞAĞI")
        sayac+=1
    if(remainingRight==0):
        print("Hakkınız Bitti. ")
        break

























