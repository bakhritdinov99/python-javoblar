class User:
    def __init__(self,name,username,mail,tel):
        self.name = name
        self.username = username
        self.mail = mail
        self.tel = tel

    def get_info(self):
        return (f"Foydalanuvchi: {self.username}, ismi {self.name}, pochtasi {self.mail}, telefon raqami: {self.tel}")

user1 = User("Alijon", "mrc4455", "alijon@samtuit.uz", 995353435)
user2 = User("Zafar", "Mr.ZMX", "zafar@samtuit.uz", 932254742)
print(user1.get_info())
print(user2.get_info())