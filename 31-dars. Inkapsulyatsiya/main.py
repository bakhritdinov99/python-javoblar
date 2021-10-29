class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odamlar_soni = 0
    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.__passport = passport
        self.tyil = tyil
        Shaxs.__odamlar_soni+=1

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.tyil}-yilda tug`ilgan"
        return info

    def get_passport(self):
        return self.__passport

    @classmethod
    def get_soni(cls):
        return cls.__odamlar_soni

class Talaba(Shaxs):
    """Talaba klassi"""
    __talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.__idraqam = idraqam
        self.bosqich = 1
        Talaba.__talabalar_soni +=1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        return info

    def get_id(self):
        return self.__idraqam

    def update_id(self,id):
        self.__idraqam = id
        return self.__idraqam
    @classmethod
    def get_soni(cls):
        return cls.__talabalar_soni




shaxs1 = Shaxs("Dilshod", "Baxritdinov", "AB4225327", 2008)
shaxs2 = Shaxs("Ali", "Vali", "AC4587242", 2012)
# print(shaxs1.get_info())
# print(shaxs1.get_passport())

talaba1 = Talaba("Farrux", "Baxritdinov", "AB4225327", 1999, 4225327)
talaba2 = Talaba("Farrux", "Baxritdinov", "AB4225327", 1999, 4225327)

# print(talaba1.get_id())
# talaba1.update_id(5478484)
# print(talaba1.get_id())

print(Shaxs.get_soni())
print(Talaba.get_soni())

