# key_py = {
#     'integer':'butun son',
#     'float':'haqiqiy son',
#     'string':'matn',
#     'if':'agar',
#     'else':'aks holda',
#     'for':'uchun',
#     'list': 'ro\'yxat',
#     'tuple':'o\'zgarmas ro\'yxat',
#     'dictonary':'lug\'at',
#     'error':'xatolik'
# }
#
#
#
# for key,value in sorted(key_py.items()):
#     print(f"{key.title()} so\'zining ma\'nosi {value}ni anglatadi.")
#
# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     'ozarbayjon':'baku',
#     'eron':'tehron',
#     "afg'oniston":'qobul',
#     'germaniya':'berlin'
# }
#
# davlat = input("Davlat nomini kiriting: ")
#
# print(davlatlar.get(davlat,"Bizda bunday ma\'lumot yo\'q").title())


# print("Davlatlar ro\'yxati:")
# for key in sorted(davlatlar):
#     print(key.title())
#
# print("\nPoytaxtlari:")
#
# for value in sorted(davlatlar.values()):
#     print(value.title())


# mavjudligi = davlatlar.get(davlat)

# print(mavjudligi)


# if mavjudligi == None:
#     print("Bunday mamlakat bazada yo'q")
# else:
#     print(f"{davlat.upper()}ning poytaxti {mavjudligi.title()} shahri")

taomlar = {
    'osh': 25000,
    'norin': 12000,
    "sho'rva": 20000,
    'non': 3500,
    'suv': 2000,
    'olma': 8000,
    'nok': 6000,
    'mayiz': 40000,
    "lag'mon": 33000,
    'makaron': 6000,
    'manti': 40000
}
buyurtmalar = []

print("3 ta taom buyurtma bering: ")

for n in range(3):
    buyurtmalar.append(input(f"{n+1} - taomni kiriting: "))

for buyurtma in buyurtmalar:
    if buyurtma in taomlar:
        print(f"{buyurtma.title()}ning narxi {taomlar[buyurtma]} so\'m")
    else:
        print(f"Bizda {buyurtma} yo'q")