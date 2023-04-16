import numpy as np 
#1-
arr = np.array([10,15,30,45,60])
#print(arr)
#2-
arr2 = np.arange(5,15)
#print(arr2)
#3-
arr3 = np.arange(50,100,5)
#print(arr3)
#4- 
arr4 = np.zeros(10)
#print(arr4)
#5- 
arr5 = np.ones(10)
#print(arr5)
#6- 
arr6 = np.linspace(0,100,5)
#print(arr6)
#7-
arr7 = np.random.randint(10,30,5)
#print(arr7)
#8-
arr8 = np.random.randint(-1,1,10)
#print(arr8)
#9-
arr9 = np.random.randint(10,50,15)
arr9 = arr9.reshape(3,5)
#print(arr9)
#10-
arr10 = np.random.randint(10,50,15)
arr10 = arr10.reshape(3,5)
rowTotal = arr10.sum(axis=1)
colTotal = arr10.sum(axis=0)
#print(arr10)
#print(rowTotal)
#print(colTotal)
#11-Üretilen matrisin en büyük ve en küçük , ortalamasınıda bul
arr11 = np.random.randint(10,50,15).reshape(3,5)
enb = arr11.max()
enk = arr11.min()
ort = arr11.mean()
#print(arr11)
#print(enb)
#print(enk)
#print(ort)
#12-Üretilen matrisin en büyük değerinin indisi ve en küçük değerinin indisi nedir ? 
arr12 = np.random.randint(10,50,15).reshape(3,5)
max_indis = arr12.argmax()
min_indis = arr12.argmin()
#print(arr12)
#print(max_indis)
#print(min_indis)
#13-
arr13 = np.arange(10,20)
result = arr[:3]
#print(arr13)
#print(result)
#14-
arr14 = np.arange(10,20)
result = arr14[::-1]
#print(result)
#15-
arr15 = np.arange(10,20)
arr16 = arr15.reshape(2,5)
result = arr16[:,0]
#print(arr16)
#print(result)
#16- 
arr17 = np.arange(10,20)
#print(arr17)
arr17 = arr17*arr17 # veya arr17 = arr17**2
#print(arr17)
#17-Üretilen matrisin hangiis çüft sayıdır ? 
arr18 = np.random.randint(-50,50,10)
result = arr18 >= 0
#print(result) 
