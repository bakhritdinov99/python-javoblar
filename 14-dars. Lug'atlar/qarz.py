qarz = int(input("Qarz: "))
foiz = float(input("Yillik foiz stavkasi(%): "))
tulov = int(input("To'lov miqdori: "))
# stavka = (qarz-tulov)+qarz*foiz/12
i=1
summa=0
while True:
    stavka = (qarz - tulov) + qarz * (foiz / 100) / 12
    summa += tulov
    print(f"{i}-oy to'lov summasi {tulov}, qoldiq {int(stavka)}")
    qarz = stavka
    i+=1
    if qarz<tulov:
        stavka = (qarz - tulov) + qarz * (foiz / 100) / 12
        print(f"{i}-oy to'lov summasi {int(stavka+tulov)}, to'lov yakunlandi, Umumiy to'langan summa: {int(summa+stavka+tulov)}")
        break

