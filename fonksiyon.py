def selamla():
    print("merhaba")
    print("nasılsın")

def ogren(isim):
    print("Merhaba : "+ isim)

def total(a,b,c):
    print("Totamları : ", a+b+c)

def factoriel(num): 
    total = 1
    while num >=1 : 
        total *= num
        num-=1
    print("Faktöriyel sonucu : ",total)

factoriel(7)

#Return ifadesi 

def toplam(a,b,c):
    return a+b+c 

def karesiniAl(a):
    return a**2


toplama = toplam(2,5,4)
print(karesiniAl(toplama))

def bilgi(isim="Bilgi Yok",numara ="Bilgi Yok",iş ="Bilgi Yok"):
    print("İSİM : " ,isim , "NUMARA : ",numara,"İŞ : "+iş)


bilgi("Ali","lafkasfklwk","SŞFLASŞLF")


print("aLİ","sÜREL",sep="*")


etiket = lambda x : x*2 

print(etiket(5))

def fonk(a,d):
    return sum((2,5))

print(fonk(10,20))



#map Kullanımı
square = lambda num : num **2  
numbers = [1,2,4,5,6]
result = list(map(square,numbers))
print(result)