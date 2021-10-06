#
# def oraliq(min,max,step=1):
#     while min<max:
#         sanoq.append(min)
#         min += step
#     return  sanoq
#
# sanoq = []
#
# print(oraliq(0,11,2))

#
# def full_data(ism,fam,t_yil,t_joy,mail='',tel=None):
#     user = {
#         'ismi':ism,
#         'familyasi':fam,
#         'tugilgan yili':t_yil,
#         'tug\'ilgan joyi':t_joy,
#         'elektron pochtasi':mail,
#         'telefon raqami':tel
#     }
#     return user
#
# mijozlar = []
#
# while True:
#     ism = input("Ismingizni kiriting: ")
#     fam = input("Familyangizni kiriting: ")
#     t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#     t_joy = input("Tug'ilgan joyingizni kiriting: ")
#     mail = input("Elektron pochtangiznki kiriting: ")
#     tel = input("Telefon raqamingizni kiriting: ")
#     mijozlar.append(full_data(ism,fam,t_yil,t_joy,mail,tel))
#     javob = input("Yana mijoz kiritishni xoxlaysizmi(ha/yo'q): ")
#     if javob == 'yo\'q':
#         break
#
# for mijoz in mijozlar:
#     print(f"{mijoz['ismi']} {mijoz['familyasi']}, {mijoz['ismi']} {mijoz['tugilgan yili']}-yilda tug'ilgan")

# def maksimum(x,y,z):
#     if x>y and x>z:
#         return x
#     elif y>x and y>z:
#         return y
#     elif z>x and z>y:
#         return z
#     else:
#         return ("Sonlar teng")
#
# x=float(input("Son kiriting: "))
# y=float(input("Son kiriting: "))
# z=float(input("Son kiriting: "))
#
# katta = maksimum(x,y,z)
# print(katta)


# def aylana(r):
#     umumiy = {
#         'radius':r,
#         'diametr':2*r,
#         'uzunligi':2*3.14*r,
#         'yuzi':3.14*r*r
#     }
#     return umumiy
#
# x=float(input("Aylana radiusini kiriting: "))
#
# lugat = aylana(x)
#
# print(lugat['yuzi'])


# x = int(input("Sonni kiriting: "))
# y = int(input("Sonni kiriting: "))
#
# def tub_son(min,max):
#     tub_sonlar = []
#     for n in range(min, max+1):
#         tub = True
#         if (n == 1):
#             tub = False
#         elif (n == 2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if (n%x == 0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar
# a = tub_son(x,y)
# print(a)

x = int(input("Sonni kiriting: "))
fibb = []
def fibbonaci(s):
    for x in range(s):
        if x == 0 or x == 1:
            fibb.append(1)
        else:
            fibb.append(fibb[x - 1] + fibb[x - 2])
    return fibb

print(fibbonaci(x))