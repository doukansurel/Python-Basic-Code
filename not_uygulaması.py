#Kullanıcıdan isim soyisim ve 3 tane not isteyeceğiz 
#Bu bilgileri bir dosyaya kaydedeceğiz 
#notların ortalarını ve buna karşılık gelen harf karşılıklarını istenilen bir zamanda başka bir dosyaya kaydedilecek

def noteCalculator(line):
    line = line[:-1]
    list = line.split(":")
    
    notes = list[1].split(",")
    
    information = list[0]
    
    note1 = int(notes[0])
    note2 = int(notes[1])
    note3 = int(notes[2])
    
    total = (note1+note2+note3)/3
    
    if total <= 100 and total >= 90 :
        letter = "AA"  
    elif total <= 89 and total >= 80 : 
        letter = "BA"
    elif total <= 79 and total >= 70 : 
        letter = "CC"
    elif total <= 69 and total >= 60 :
        letter = "CD"
    elif total <= 59 and total >= 50 :
        letter = "DD"
    else :
        letter = "FF"
    return  information +" : " + letter+"\n" 
    
  
def  noteRead():
   with open("bilgiler.txt","r",encoding="utf-8") as file:
       for line in file : 
           print(noteCalculator(line))


def noteEnter():
    name = input("Adı Girin : ")
    surname = input("Soyadı Girin : ")
    note1 = input("Vize1 Notunu Girin : ")
    note2 = input("Vize2 Notunu Gİrin : ")
    note3 = input("Final Notunu Girin : ")


    with open("bilgiler.txt","a",encoding="utf-8") as file :
        file.write(name+" "+surname+":"+note1+","+note2+","+note3+"\n")
        
def noteSave():
    with open("bilgiler.txt","r",encoding="utf-8") as file :
        list = [] 
        
        for i in file :
            list.append(noteCalculator(i))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in list:
                file2.write(i)
    print("Notlar Başarıyla Kaydedildi...".center(50,"*"))


while True : 
    islem = input("1-Ortalamaları Oku\n2-Notları Gir\n3-Notları Kaydet\n4-Çıkış\nYapmak İstediğiniz İşlemi Seçin : ")
    if islem == "1" : 
        noteRead()
    elif islem == "2" : 
        noteEnter()
    elif islem == "3" :
        noteSave()
    elif islem == "4" : 
        print("Sistemden Çıkılıyor...")
        break
    else :
        print("Hatalı işlem yaptınız tekrar deneyin... ")
        continue