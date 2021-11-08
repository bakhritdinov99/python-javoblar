# Quyidagi funksiyalarni yarating, va ularning har biri uchun test dasturlarini yozing:
#
# 1. Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya
# 2. Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya
# 3. Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya
# 4. Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) qaytaruvchi funksiya yozing.

# 1-masala
def katta_son(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

# 2-masala

def katta_harf(a):
    k_h = []
    for x in a:
        k_h.append(x.title())
    return k_h


# 3 - masala
from math import sqrt
def juft(r):
    juftlari = []
    for x in r:
        if x%2 == 0:
            juftlari.append(x)
    return juftlari

# 4-masala

def fibbonacci(n):
    if (sqrt(5*(n**2)-4)%1 == 0 or sqrt(5*(n**2)+4)%1 == 0):
        return True
    else:
        return False