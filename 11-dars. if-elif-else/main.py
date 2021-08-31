# son = float(input("Iltimos juft son kiriting: "))
#
# if son%2 ==0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas!")

# yosh = int(input("Yoshingizni kiriting: "))
#
# if yosh <= 4 or yosh >= 60:
#     narx = 0
# elif yosh < 18:
#     narx = 10000
# else:
#
# print(f"Siz {narx} so\'m to\'lashingiz kerak")

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
#
# if son1 == son2:
#     print("Sonlar teng")
# elif son1<son2:
#     print("Ikkinchi son katta")
# else:
#     print("Birinchi son katta")

# mahsulotlar = ['sabzi', 'kartoshka', 'piyoz', 'makaron', 'qovoq', 'pomidor', 'bodiring', 'karam', 'baqlajon', 'gugurt']
# savat = []
#
# for mahsulot in range(5):
#     savat.append(input("Mahsulot kiriting: "))
#
# print(savat)
#
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         print(f"Bizda {mahsulot} bor")
#     else:
#         print(f"Bizda {mahsulot} yo\'q")


# mahsulotlar = ['sabzi', 'kartoshka', 'piyoz', 'makaron', 'qovoq', 'pomidor', 'bodiring', 'karam', 'baqlajon', 'gugurt']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
#
# for mahsulot in range(5):
#     savat.append(input("5 ta mahsulot kiriting: "))
#
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
#
# if len(savat) == len(bor_mahsulotlar):
#     print("Siz so\'ragan barcha mahsulotlar do\'konimizda bor")
# else:
#     print("Quyidagi mahsulotlar do\'konimizda yo'q: ")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)

# foydalanuvchilar = ['anvar', 'zafar', 'alijon', 'farrux', 'doniyor']
#
# new_login = input("Loginni kiriting: ")
#
# if new_login.lower() in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print("Xush kelibsiz, foydalanuvchi!")

son = float(input("Butun son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"Kiritilgan son {n} ga qoldiqsiz bo\'linadi")