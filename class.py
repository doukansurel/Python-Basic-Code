class Circle :
    pi = 3.14

    def __init__(self , yaricap = 1):
        self.yaricap = yaricap

    
    def alanHesapla(self):
        return self.pi*(self.yaricap**2)
    
    def cevreHesapla(self):
        return 2*(self.pi*self.yaricap)
        

c1 = Circle()
c2 = Circle(7.4)
c3 = Circle(5)

print(f"c1 in alanı {c1.alanHesapla()}  \n")
print(f"c2 in alanı {c2.alanHesapla()}  \n")
print(f"c3  ün çevresi {c3.cevreHesapla()} \n")

