
try : 

    x = int(input(" x : "))
    y = int(input(" y : "))

    print(x/y)
except(ZeroDivisionError) as e :
    print(e) 
else : 
    print("Herşey yolunda...")

    #Raise Kullanımı 

def checkPassword(psw) : 
    import re
    if len(psw) < 8 : 
        raise Exception("parola en az 7 karakter içermeli.")
    elif not re.search("[a,z]",psw):
        raise Exception("Parolada büyük harfler içermemelidir.")



