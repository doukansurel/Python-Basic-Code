#Dosya'ya yazma işlemi 

#result = open("newfile.txt","w",encoding="utf-8")
#result.write("Merhaba Ali Doğukan Sürel")
#result.close()

#Dosyaya Ekleme işlemi

#result= open("newfile.txt","a",encoding="utf-8")
#result.write("\n Nasılsın İyi misin ? ")
#result.write("\n Beni merak ediyorsan ben iyiyim... :(")
#result.close()

#Dosya Okuma İşlemi

#1 . For döngüsüyle okutabiliriz.

result = open("newfile.txt","r",encoding="utf-8") 
#for i in result:
#    print(i, end="")

#2 . read() fonksiyonu 

#content = result.read()
#print(content)

#3 . readline() fonksiyonu  => Her seferinde bir satır okur. 
print(result.readline())


#4 . readlines() fonksiyonu => satıları bir diziye aktarır.
list = result.readlines()
print(list)







