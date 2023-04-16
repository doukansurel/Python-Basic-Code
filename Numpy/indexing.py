import numpy as np

numbers = np.array([0, 5, 15, 25, 35, 45, 55, 65, 75])
result = numbers[-5]  # sağdan 5.değeri yazar
result = numbers[:3]  # index 3 olana kadar yazdırır
result = numbers[::]  # hepsini yazdıır
result = numbers[::-1]  # tersten yazdırır.
result = numbers[::-2]  # tersten ikili atlayarak yazdırır.


numbers2 = numbers.reshape(3, 3)  # 3e 3 lük bir matris oluşturdu.
result = numbers2
result = numbers2[:, 1]  # tüm satırları alırken sadece 2. sütunu alır.
result = numbers2[0, 2]
result = numbers2[2]  # 3.satırı alır direk
result = numbers2[:, 0:2]
# sağdan birinci satırı alır ve 0 ile 2 arasındaki indis değerlerini döndürür.
result = numbers2[-1, 0:2]


arr1 = np.arange(0, 10)  # belirtilen sınır arasında değer üretir.

arr2 = arr1  # referans kopyalama.

arr2[0] = 20  # iki dizidede değer güncellenir.


# eğer copy metodunu kullanarak yaparsak belirtilen değer iki dizidede değişmez
arr = arr1.copy()
arr2[2] = 30
print(arr)
print(arr1)
