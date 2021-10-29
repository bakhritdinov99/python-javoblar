class Avto:
    def __init__(self,model, rang, korobka, narx, yili):
        self.model = model
        self.rang= rang
        self.korobka = korobka
        self.narx= narx
        self.yili= yili
        self.kilometr = 0

    def get_info(self):
        return (f"Avtomobilning modeli {self.model}, rangi {self.rang}, korobkasi {self.korobka}, {self.yili}-yilda ishlab chiqarilgan. Narxi {self.narx}. Yurgan kilometri {self.kilometr}.")

    def update_km(self,km):
        self.kilometr += km

class Avtosalon:
    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.avtomobillar = []

    def add_avto(self,avtomobil):
        self.avtomobillar.append(avtomobil)

    def avto_info(self):
        return [avto.get_info() for avto in self.avtomobillar]



avto1 = Avto("Cobalt", "Summit White", "avtomat", 12000, 2021)
avto2 = Avto("Gentra", "Black", "mexanika", 10000, 2017)
avto2.update_km(155000)


salon1 = Avtosalon("Regal", "Samarqand")

salon1.add_avto(avto1)
salon1.add_avto(avto2)

print(salon1.avto_info())

print(dir(Avtosalon))
print(dir(str))
print(avto1.__dict__)