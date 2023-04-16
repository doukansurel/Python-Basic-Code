import json
import os
class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        #load users from .json file 
        self.loadUser()

    def loadUser(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file : 
                users = json.load(file)
                for user in users : 
                    user = json.loads(user)
                    newUser = User(username = user["username"],password = user["password"] , email = user["email"])
                    self.users.append(newUser)
            print(self.users)

    def register(self ,user : User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı Başarıyla oluşturuldu.")

    def login(self, username,password):
        for user in self.users :
            if user.username == username and user.password == password:
                self.isLoggedIn = True 
                self.currentUser = user
                print("Login is succesfull")
                break
    def logout(self):
        self.isLoggedİn = False
        self.currentUser = {}
        print("Çıkış Yapıldı..")

    def identity(self):
        if self.isLoggedIn : 
            print(f"username : {self.currentUser.username}")
        else : 
            print("Giriş Yapılmadı...")
    
    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open("users.json","w",encoding="utf-8") as file :
            json.dump(list,file)


repository = UserRepository()
while True:
    print("Menü".center(50,"*"))
    operation = input("1-Register\n2-Login\n3-Logout\n4-İdentity\n5-Exit\nYapmak İstediğiniz İşlemi Seçin : ")
    if operation == "5" : 
        print("Sistemden Çıkılıyor...")
        break
    else : 
        if operation == "1":
            username = input("Username : ")
            password = input("Password : ")
            email = input("E-mail :")

            user = User(username=username,password=password,email=email)
            repository.register(user)

            print(repository.users)
        elif operation == "2":
            if repository.isLoggedIn :
                print("Zaten Giriş Yaptınız.")
            else :
                    username = input("Username : ")
                    password = input("Password : ")
                    repository.login(username,password)
             
        elif operation == "3":
            repository.logout()
        elif operation == "4":
            repository.identity()
        else : 
            print("Yanlış Tuşlama Yaptınız. Lütfen Tekrar Deneyiniz ... ")


