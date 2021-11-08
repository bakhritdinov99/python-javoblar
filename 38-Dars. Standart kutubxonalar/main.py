# -Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring
# -Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
# -Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing
# -Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring
# -Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan namuna sifatida foydalanishingiz mumkin:
# Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test

from datetime import date,datetime,timedelta
# 1-masala
hozir  = datetime.now()
# for x in range(10):
#     print(hozir.date())
#     hozir += timedelta(days=14)

# 2-masala
# t_k = date(2022,7,25)
# vaqt = (t_k-hozir.date()).days
# print(f"Tug'ilgan kunimgacha {vaqt} kun qoldi!")

# 3-masala


# t_kunim = date(1999,7,25)
# kun  = (hozir.date()-t_kunim)
# print(f"Tug'ilgan kuningizga {kun.days} kun bo'ldi")


# 4-masala

import re

andoza = "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
matn = "Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"

web_link = re.findall(andoza,matn)
print(web_link)