# def usalma(number):
#   def inner(power):
#       return number**power
#   return inner
#three = usalma(5)
#print(three(3))

#def islemsorgula(page):
#    def yetkisorgula(role):
#        if role == "Admin" : 
#            return "{0} rolü {1} işlemine ulaşabilir.".format(role,page)
#        else : 
#            return "{0} rolü {1} işlemine ulaşamaz.".format(role,page)
#    return yetkisorgula 

#user1 = islemsorgula("Product Edit")
#print(user1("Admin"))

def operationMake(claim):
    def addition(*args):
        total=0
        for i in args:
            total += i 
        return total

    def multiplication(*args):
        total = 1
        for i in args:
            total *=i
        return total
    if claim == "toplama":
        return addition
    else :
        return multiplication
toplama = operationMake("toplama")
print(toplama(1,2,3,4,5,6,7,9,10))

carpma = operationMake("çarpma")
print(carpma(1,2,4,53,4,6))



