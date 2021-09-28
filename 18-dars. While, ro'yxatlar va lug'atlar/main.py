
# ism = input("Ismingizni kiriting: ")
# print(f"Salom {ism}, Taomlarni navbat bilan kiriting:")
# flag = True
# n=1
# taomnoma = []
# while flag:
#     javob = input(f"{n}- taomni kiriting: ")
#     taomnoma.append(javob)
#     n+=1
#     xoxish = input(f"Yana biror nima buyurtma qilasizmi? ha/yo'q(y/n): ")
#     if xoxish == "yo'q" or xoxish=='n':
#         flag = False
# print(taomnoma)

# bozor = {}
#
# while True:
#     mahsulot = input("Mahsulotni kiriting: ")
#     narx = input(f"{mahsulot.title()}ning narxini kiriting: ")
#     bozor[mahsulot]=int(narx)
#     javob = input("Yana mahsulot kiritasizmi: (ha/yo'q) ")
#     if javob != 'ha':
#         break
# print(bozor)

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narx = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narx} so'm")
    else:
        print("Bizda bunday mahsulot yo'q")