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

    def __repr__(self):
        return f"{self.ism} {self.familiya}"


class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.bosqich = 1


    def update_bosqich(self):
        self.bosqich +=1

    def get_bosqich(self):
        return self.bosqich

    def __eq__(self, other):
        return self.bosqich == other.bosqich

    def __gt__(self, other):
        return self.bosqich > other.bosqich

    def __ge__(self, other):
        return self.bosqich >= other.bosqich


class Fan:
    def __init__(self,nomi):
        self.fan_nomi = nomi
        self.talabalar = []

    def add_student(self, *talaba):
        for x in talaba:
            self.talabalar.append(x)

    def __add__(self, other):
        if isinstance(other,Talaba):
            self.talabalar.append(other)


    def __sub__(self, other):
        self.talabalar.remove(other)
    def talaba(self):
        for x in self.talabalar:
            return (x)

    def __repr__(self):
        return self.fan_nomi
    def __len__(self):
        return len(self.talabalar)

    def __call__(self):
        return f"{math.fan_nomi} fanida quyidagi talabalar bor: {self.talabalar}"

shaxs1 = Shaxs("Farrux", "Baxritdinov", "AB4225327", 1999)
shaxs2 = Shaxs("Alijon", "Kuvondikov", "AA4225327", 1999)
shaxs3 = Shaxs("Zafar", "Xazratkulov", "AA1200202", 1999)

talaba1 = Talaba("Doniyor", "Kamolov", "AA100000", 1998)
talaba2 = Talaba("Bobur", "Ashurov", "BB42214145", 1995)
talaba3 = Talaba("Ro'zimboy", "Sobirov", 'AA4758484',1988)
# print(shaxs1)
talaba1.update_bosqich()
# print(talaba1.get_bosqich())
# print(talaba2.get_bosqich())
# print(talaba1>=talaba2)

math = Fan("Matematika")
math.add_student(talaba2,talaba1,shaxs3)



# print(math, math.talabalar)

# print(len(math))
# print(math.talabalar[1])
# math.talabalar[1]="Zafar Xazratkulov"
# print(math.talabalar[1]

print(math())
math+talaba3
print(math())
math-talaba2
print(math())
