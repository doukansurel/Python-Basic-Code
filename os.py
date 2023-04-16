import os
from datetime import datetime
#result = os.name        # Dosyanın Kullanılıp Kullanılmadığını Gösterir.
#result = os.getcwd()   #Dosya Yolunu Gösterir.
#os.chdir("C:\\")         #Oluşturulacak Dosyanın Konumu Belirler.
#os.mkdir("newFile")   # Dosya oluşturur.
#os.makedirs("C:\\newFile\deneme1")   #Dosyanın içinde Dosya oluşturur. Konum belirterek.
#os.rename()     Bize dosya adını değiştirmemize olanak sağlar.
#os.rmdir()   Bize dosyayı kaldırmamızı sağlar.




#result = os.listdir("C:\\")   # İStedğimiz konumdaki dosyaları listeler.

#result = os.stat("date.py")    # İstedğimiz dosya hakkında bize bilgi verir.
#result = result.st_size/1024   # Dosyanın Boyutu 
#result = datetime.fromtimestamp(result.st_ctime)   # Oluşturulma tarihi
#result = datetime.fromtimestamp(result.st_atime)   # son erişim tarihi
#result = datetime.fromtimestamp(result.st_mtime)    # Son değiştirilme tarihi 


# path kullanımı 

#result = os.path.abspath(dosya adı) iie   ==> Bize dosya konumunu verir.
#result = os.path.dirname(dosya yolu ) ile ==> Bize dosyanın dizinini verir.
#result = os.path.exits(dosya adı )   ile ==> Bize dosyanın var olup olmadığını boolean türüyle döner.
#result = os.path.isdir(dosya yolu)   ile ==> Bize klasör olup olmadığını söyler
#result = os.path.isfile(dosya yolu)  ile ==> Dosya olup olmadığını söyler.



print(result)