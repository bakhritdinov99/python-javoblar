# def yil_hisobla(ism,yosh):
#     print(f"Salom {ism.title()}, Siz {2021-yosh} - yilda tug'ilgansiz.")
#
#
# ism = input("Ismizngizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
#
# yil_hisobla(ism,yosh)

# def daraja_hisoblash(x):
#     print(f"{x} ning kvadrati - {x*x} ga teng")
#     print(f"{x} ning kubi - {x ** 3} ga teng")
#
# son = float(input("Son kiriting: "))
#
# daraja_hisoblash(son)

# def aniqla(x):
#     if x%2 == 0:
#         print("Juft")
#     else:
#         print("Toq")
#
# son = int(input("Sonni kiriting: "))
#
# aniqla(son)

# def taqqosla(x,y):
#     if x>y:
#         print(x)
#     elif x<y:
#         print(y)
#     else:
#         print("Sonlar teng")
#
# son1 = float(input("1- sonni kiriting: "))
# son2 = float(input("2- sonni kiriting: "))
#
# taqqosla(son1,son2)


# def daraja(x,y=2):
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")
#
# daraja(5)

def bulinish(son):
    for x in range(2,11):
        if son%x == 0:
            print(f"{son} {x} ga qoldiqsiz bo'linadi")


son = int(input("Sonni kiriting: "))

bulinish(son)