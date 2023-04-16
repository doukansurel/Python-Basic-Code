""""
def myDecorators(func):
    def wrapper():
        print("fonksiyondan önceki işlemler")
        func()
        print("Fonksiyondan sonraki işlemler")
    return wrapper()
    
def sayHello():
    print("Hello")

@myDecorators
def sayGreeting():
    print("Hi, Welcome My Friend.")

sayGreeting()
"""
import math
import time
def calculateTime(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        finish = time.time()
        print("fonksiyon "+func.__name__+" "+str(finish-start)+ "saniye sürdü.")
    return inner

@calculateTime
def usalma(a,b):
    print(math.pow(a,b))
   
@calculateTime
def factorielMake(a):
    print(math.factorial(a))
   
usalma(5,6)
factorielMake(5)





