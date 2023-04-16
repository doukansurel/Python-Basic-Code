""""
with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    file.seek(0)
    print(file.tell())
    content2= file.read()
    print(content2)
"""
# İsteğimiz sıraya ekleme yapma 
""""
with open("newfile.txt","r+",encoding="utf-8") as file : 
    file.seek(40)
    file.write("Naber lan Keklik ?")

with open("newfile.txt","r+",encoding="utf-8") as file : 
    print(file.read(), end ="")
"""
#sayfa başına ekleme yapma
#with open("newfile.txt","r+",encoding="utf-8") as file :
#    content = file.read() 
#    content= "Merhaba canım \n" +content
#    file.seek(0)
#    file.write(content)
#with open("newfile.txt","r",encoding="utf-8") as file : 
#    print(file.read(), end ="")

#Sayfa ortasında Güncelleme Yapmak
#burada readlines() metoduyla list dizisine ekleriz oradan da istediğimiz konu insort() fonksiyonu ile ekelemeyi yaparız
#writelines() fonksiyponu ile listeye eklemek isteğimizi ekleriz .


