from os import name


sayilar = [1,3,5,7,9,12,19,21]

#Soru 1 - While ile sayiları yazdırın 
#num = 0
#while (num < len(sayilar)) :
#    print(sayilar[num]) 
#    num+=1 
  
#Soru 2 -Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın .
#start = int(input("Başlangıç değerini giriniz : "))
#stop = int(input("Bitiş değerini giriniz :"))
#i = start
#while i < stop : 
#    i += 1
#    if ( i % 2 == 1) :
#        print(i) 

#Soru 3 - 1-100 arasındaki sayıları azalan şeklinde yazdırın ekrana 
#start = 1 
#stop = 100
#i = 100 
#while i !=0 : 
#    print(i)
#    i -= 1 

#Soru 4 - Kulanıcıdan aldığımız 5 değeri sıralı bir şekilde yazdırın 
#i = 0
#list = []
#while i <5 :
#    value = int(input("değeri girin : "))   
#    list.append(value)
#    i += 1  
#while i < 5 :
#    print(f"Değerler sırası ile : {list[i]} ")    
#    i +=1

#Soru 5 - Ürün listesi oluşturup kaç tane ekleyeceğini sor ve dictionary ["name" : "price " şeklinde olsun ]
operation = int(input("Kaç tane eleman ekleyeceksiniz ? : "))

i = 0
products= []
while i < operation : 
    productName = input("Ekleyeceyeğiniz ürünün adını girin : ")
    productPrice = input("Ekleyecek ürünün fiyatını girin : ")
    products.append({
        "name":productName,
        "price":productPrice
    })
    i+=1
print("Ürünler Listeleniyor...".center(50,"*"))    
for product in products : 

    print(product)    
