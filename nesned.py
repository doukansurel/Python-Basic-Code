#def outer(num):
#    print("Outer")
#    def inner(num):
#        print("İnner")
#        return num+1
#    num2 = inner(num)
#    print(num,num2)
#outer(10)

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("number must be an integer")
    if not number >= 0 :
        raise ValueError("Number must be zero or positive number")
    def innerFactorial(number):
        if  number<=1 :
            return 1

        return number * innerFactorial(number-1)
    return innerFactorial(number)

print(factorial(a))