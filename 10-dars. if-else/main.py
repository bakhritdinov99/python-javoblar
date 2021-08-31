# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# login = input("Loginingizni kiriting: ")
#
# if login.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x == y:
#     print("Sonlar teng.")

# x = float(input("Son kiriting:"))
# if x>0:
#     print("Musbat son")
# else:
#     print("Manfiy son")

x = float(input("Son kiriting:"))
if x>0:
    print(x**(1/2))
else:
    print("Musbat son kiriting")