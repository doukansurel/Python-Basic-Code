def cube(): 
    for i in range(5):
        yield i**3

#Bunun yerine ;
"""
generators = cube()
iterator = iter(generators)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""
#Bu Şekilde yapabiliriz ;
#iterator = cube()
#for i in iterator:
#print(i)

#VEYA bu şekildede yapabilirz :
#
#for i in cube():
#    print(i)

#Başka Generator Kullanımı : 
liste = (i**3 for i in range(5))
for i in liste:
    print(i)

