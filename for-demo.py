numbers = [1,3,5,7,9,12,19,21]

#Soru 1 - Hangileri 3'ün katlarıdır ? 
#for num in numbers : 
 #   if(num%3==0):
 #        print(f"{num} sayısı 3'ün katıdır.")

#Soru 2 - Listedeki Sayılar Toplamı ?
#total = 0
#for num in numbers : 
#    total += num
#print("Total : ",total)

#Soru 3 - Tek Sayıların Karesini Almak ?
#for num in numbers : 
#    if(num%2!=0):
#        square=num**2
#        print(f"{num} sayısı tek sayıdır ve kareside {square} 'dir.")

cities = ["kocaeli","istanbul","izmir","ankara","rize"]
#Soru 1 - Hangileri 5 karakterlidir ?
#for city in cities :
#    if(len(city)==5):
#        print(f"{city} 5 karakterlidir.")


products = [
    {"name" : "samsung s6" ,"price":"3000"},
    {"name":"samsung s7","price":"4000"},
    {"name":"samsung s8","price":"5000"},
    {"name":"samsung s9","price":"6000"},
    {"name" : "samsung s10","price":"7000"}
]
#Soru 1 -Ürünlerin Toplamı nedir ?
#total = 0 
#for product in products : 
#    fiyat = int(product["price"])
#    total += fiyat
#print("Total : ", total)

#Soru 2 -Ürünlerden Fiyatı en fazla 5000 olan ürünleri gösterin ?
for product in products:
    if(int(product["price"])<=5000):
        names = product["name"]
        print(f"Fiyatı en fazla 5000 ve 5000 den düşük olanlar : {names} ")


