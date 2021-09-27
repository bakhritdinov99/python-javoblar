# ism = input("Ismingizni kiriting: ")
#
# print(f"Salom {ism}, Yoqtirgan kitoblaringizni navbat bilan kiriting: ")
#
# flag = True
#
# while flag:
#     kitob = input(f"Kitob nomini kiriting: ")
#     if kitob == 'stop':
#         break

# flag = True
#
# while flag:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh == 'exit' or yosh == 'quit':
#         print("Dastur to'xtatildi")
#         break
#     else:
#         yosh = int(yosh)
#         if yosh <= 7:
#             narx = 2000
#         elif yosh > 7 and yosh <= 18:
#             narx = 3000
#         elif yosh >= 18 and yosh <65:
#             narx = 10000
#         else:
#             narx = 0
#     print(f"Siz uchun bilet narxi {narx} so'm")


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")