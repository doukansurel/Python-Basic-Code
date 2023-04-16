import numbers
import numpy as np 
arr = np.random.randint(0,100,6)
arr2 = np.random.randint(0,100,6)

print(arr)
print(arr2)

total = arr + arr2 # iki diziyi toplayabilir.
total = arr +10 # dizinin her elemanına 10 ekler
total = arr*100 # dizinin her elemanını bir sayı ile çarpabilir. 
total = arr* arr2 # iki dizinin elemanlarını çarpabilir.

total = np.sin(arr) # dizideki elemanların sinüsünü alır.
total = np.cos(arr2)# dizideki elemanların cosunu alır.
total = np.log(arr) # dizideki elemanların logaritmasını alır.

#print(total)

arr3 = np.vstack((arr,arr2)) # dizileri bir dikey olarak birleştirir. 
arr3 = np.hstack((arr,arr2)) # dizileri yatay olarak birleştirir. 

#print(arr3)

result = arr >= 5  # koşula göre dizideki elemanları karşılaştırıp ona göre değer döner. 
result = arr2 % 2 == 0 


print(arr2[result])
