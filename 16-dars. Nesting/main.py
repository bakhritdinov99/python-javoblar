# acc0 = {
#     'name':'Mark',
#     'age':35,
#     'company':'facebook',
#     'coutry':'USA',
#     'asarlari':['facebook haqida','ijtimoiy tarmoq', 'internet va bugun']
# }
#
# acc1 = {
#     'name':'Stive',
#     'age':56,
#     'company':'Microsoft',
#     'country':'USA',
#     'asarlari':['iMac','Macbook','iPhone']
# }
#
# acc2 = {
#     'name':'Pavel',
#     'age':28,
#     'company':'Telegram',
#     'country':'United Arab Emirates',
#     'asarlari':['Tarmoqda tezlik','Internet olami','Tarmoq xavfsizligi']
# }
#
# acc3 = {
#     'name':'Snouden',
#     'age':37,
#     'company':'freelancer',
#     'country':'Russia',
#     'asarlari':[]
# }
# accounts = [acc0,acc1,acc2,acc3]
#
# for account in accounts:
#     print(f"Ismi: {account['name']}, yoshi {account['age']}da, hozirda {account['company']}da ishlaydi. U quyidagi kitoblarni yozgan: ")
#
#     for x in account['asarlari']:
#         print(x)
#     print('\n')
#

# dostlar = {
#     'Savlat':['Shamol ortidan yugurib', 'Ming quyosh shu\'lasi', 'Tog\'lar ham sado berdi'],
#     'Hasan':['acer', 'asus', 'lenovo'],
#     'Husan':['nexia', 'spark', 'lacetti']
# }
#
# for ism, kinolar in dostlar.items():
#     print(f"{ism}ning yoqtirgan narsalari: ")
#     for kino in kinolar:
#         print(kino)
#     print('\n')


davlatlar = {
    "o'zbekiston":{
        'poytaxt':'Toshkent',
        'aholisi':'35 mln',
        'Prezidenti':'Mirziyoyev'
    },
    "aqsh":{
        'poytaxt':'Washington',
        'aholisi':'300 mln',
        'Prezidenti':'Bayden'
    },
    "rossiya":{
        'poytaxt':'Moskva',
        'aholisi':'150 mln',
        'Prezidenti':'Putin'
    }
}

# for davlat, xususiyat in davlatlar.items():
#     print(f"{davlat}ning poytaxti {xususiyat['poytaxt']}, aholisi {xususiyat['aholisi']}ta, Hozirgi vaqtda davlat rahbari {xususiyat['Prezidenti']}.")

davlat = input("Davlatni kiriting: ").lower()

if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"{davlat.capitalize()}ning poytaxti {info['poytaxt']}, aholisi {info['aholisi']}ta, Hozirgi rahbari {info['Prezidenti']}.")

else:
    print("Bizda bu davlat haqida ma'lumot yo'q")
