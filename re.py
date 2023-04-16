import re
str = "Python Geliştirici Kursu : İleri Seviye Python Öğreniyorum | 40 saat"

#result = re.findall("Kursu",str)      ==> Aranacak ifadeyi nerede arayacağını söyleyip onu buldurursun.

#result = re.split(" ",str)             ==> Neye Göre bölünecek olduğunu söyleyip işlem yapılacak yerde böler.

#result = re.sub(" ","/",str)                 ==> Değişiklik yapmaya yarar.


result = re.search("Python",str)
#result = result.span()
#result = result.start()
#result = result.end()
#result = result.group()
#result = result.string
#result = re.findall("[abc]",str)
#result = re.findall("...",str)
#result = re.findall("^P",str)
#result = re.findall("t$",str)
#result = re.findall("sa*t",str)
#result = re.findall("sa+t",str)
#result = re.findall("sa?t",str)
#result = re.findall("[0-9]{2}",str)




print(result)