"""
28/01/2021
Dasturlash asoslari
#30-DARS. VORISLIK VA POLIMORFIZM
Muallif: Anvar Narzullaev
Web sahifa: https://python.sariq.dev
"""


class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    def fanga_yozil(self, fan_n):
        self.fanlar.append(fan_n)

    def remove_fan(self, rm_fan):
        if rm_fan in self.fanlar:
            self.fanlar.remove(rm_fan)
        else:
            print(f"Siz {rm_fan.fan_nomi} faniga yozilmagansiz")

    def get_fan(self):
        return [fan.fan_nomi for fan in self.fanlar]


class Manzil:
    """Manzil saqlash uchun klass"""

    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil


class Fan:
    def __init__(self, fan_nomi, fan_soati):
        self.fan_nomi = fan_nomi
        self.fan_soati = fan_soati

    def get_fanlar(self, fan=None):
        return (f"{self.fan_nomi} nomli fan, {fan.fan_soati} soat")


talaba1_manzil = Manzil(12, "Olmazor", "B`og'bon", "Samarqand")
talaba1 = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", talaba1_manzil)
fan1 = Fan("Matematika", 60)
fan2 = Fan("Tarix", 40)
talaba1.fanga_yozil(fan2)
talaba1.fanga_yozil(fan2)
talaba1.remove_fan(fan1)


class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, kafedrasi):
        super().__init__(ism, familiya, passport, tyil)
        self.kafedrasi = kafedrasi

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan. "
        info += f"{self.familiya} {self.kafedrasi} kafedrasida ishlaydi"
        return info


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, akkount_id):
        super().__init__(ism, familiya, passport, tyil)
        self.id = akkount_id

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan. IDsi {self.id}"
        return info


class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil):
        super().__init__(ism, familiya, passport, tyil)


class Mijoz(Shaxs):
    def __init__(self, ism, familiya, passport, tyil):
        super().__init__(ism, familiya, passport, tyil)

class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, akkount_id):
        super().__init__(ism, familiya, passport, tyil,akkount_id)

    def ban_user(self):
        return (f"{self.ism} bloklandi.")


# print(talaba1.get_info(), talaba1.get_fan())


mijoz1 = Mijoz("Bobur", "Ashurov", "AB4225327", 1995)
pro1 = Professor("Shuhrat", "Asrorov", "AA0070707", 1960, "Tabiiy fanlar")

# print(mijoz1.get_info())

# print(pro1.get_info())
# print(pro1.get_age(2021))

user1 = Foydalanuvchi("Farrux", "Baxritdinov", "AB4225327", 1999, 3525475)
user2 = Foydalanuvchi("Dilshod", "Baxritdinov", "1548749", 1999, 7842145)
print(user2.get_info())

blok1 = Admin("Farrux", "Baxritdinov", "AB4225327", 1999, 1547474)
print(blok1.get_info())
print(blok1.ban_user())

