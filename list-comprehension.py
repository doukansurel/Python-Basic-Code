#list = [1,2,3,4,5,6,7,8,9,10]
#list2 = [i for i in list]
#print(list2)

#list = [3,4,5,6,7,8,9]
#list3 = [i*3 for i in list]
#print(list3)

#list = [(1,2),(3,6),(5,9),(1,8)]
#list2 =[i*j for i,j in list]
#print(list2)

#s = "Merhaba"
#lsit = [i*3 for i in s] 
#print(lsit)

numbers = [x*x for x in range(10) if x%3==0]
print(numbers)


number = [x if x%2==0 else "TEK" for x in range(1,10)]
print(number)