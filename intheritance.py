class Person():
    def __init__(self, fname , lname ) :
        self.fname = fname
        self.lname = lname
        print("Person classı çalıştı...")

class Student(Person):
    def __init__(self , fname , lname ):
        Person.__init__(self , fname, lname )
        print("Student Classı Çalıştı..")
           

p1= Person("Ali","Sürel")
s1 = Student("Cahit","Sürel")
print(p1.fname + " " +p1.lname )
print(s1.fname + " " +s1.lname )



