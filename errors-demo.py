list = ["1","2","5a","10b","abc","10","50"]

# Soru  -1-  Liste elemanları içindeki sayısal değerleri bulunuz.
""""
for i in list :
    try:
        result = int(i)
        print(i)
    except ValueError as e : 
        continue
"""     
#Soru  -2- Kullanıcı "q" değerini girmedikçe alacağınız  her inputun sayı olacağından emin olun aksi halde hata mesajı yazın 
'''
while True:
    num = input("number : ")
    if num =="q":
        print("Sistemden çıkılıyor...")
        break
    try: 
        result = float(num)

    except ValueError as e : 
        print("Geçersiz Karakter.")
        continue
'''

#Soru  -3- Faktöriyel fonk oluşturup fonksiyona gelen değer için hata mesajları verin 





# Girilen parolada türkçe karakter hatası verin 
def passwordControl(psw):
    turkish_characters = "ş,ğ,ç,ö,i,ü"
    for i in password:
        if i in turkish_characters:
            raise TypeError("Parolada türkçe karakter olmamalıdır.")
        else : pass

    print("geçerli paorla")

password = input ("password : ")
try: 
    passwordControl(password)
except TypeError as e : 
    print(e)
