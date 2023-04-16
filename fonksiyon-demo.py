# Gönderilen bir kelimeyi istenilen kez ekrana yazan algoritmayı bulunuz.

def function(times,name):
    while times > 0:
        times-=1
        print("Name : ",name)


#Kendine gönderilen sınırsız parametredeki değerleri listfeye çeviren fonksiyon 

def function2(*args):
    list = []
    for arg in args :
        list.append(arg)
    return list

#print(function2(2,4,5,3,62,"Merhaba"))

#Gönderilen iki sayı arasındaki tüm asalları bulun 

def asalFind(a,b):
    num = int(input("Birinci Sayıyı girin :"))
    num2 = int(input("İkinci Sayıyı girin :"))
    for sayi in range(num, num2+1):
        if sayi>1:
            for i in range(2,sayi):
                if(sayi%i==0):
                    break
            else : 
                print(sayi)


#asalFind(50,70)

#Kendisine verilen bir sayının tam bölenlerini listeleyen fonksiyon

def divisor(num):
    listNumber = []
    i = 2
    for i in range(2,num+1):
        if(num%i==0):
            listNumber.append(i)
            
    return listNumber
    
print(divisor(20))

    