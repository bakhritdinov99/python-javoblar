# ukam = {
#     'ism':'Dilshod',
#     'familya':'Baxritdinov',
#     'maktab':40,
#     'yosh':14,
#     }
#
# print(f"Ukamning ism-sharifi {ukam['familya']} {ukam['ism']}. {ukam['ism'] }ning yoshi {ukam['yosh']} da. {ukam['ism']} {ukam['maktab']}-maktabda tahsil oladi.")

# taom = {
#     'Dadam':'osh',
#     'Ukam':'do\'lma',
#     'bobom':'sho\'rva',
#     'biyim':'manti',
#     'opam':'rollton'
# }
#
# print(f"Dadamning sevimli taomi {taom['Dadam']}, "
#       f"Ukamning sevimli taomi {taom['Ukam']}, "
#       f"Biyim esa {taom['biyim']}ni yoqtiradi.")

key_py = {
    'integer':'butun son',
    'float':'haqiqiy son',
    'string':'matn',
    'if':'agar',
    'else':'aks holda',
    'for':'uchun',
    'list': 'ro\'yxat',
    'tuple':'o\'zgarmas ro\'yxat'
}

kalit = input("Kalit so'z kiriting: ").lower()
# print(key_py.get(kalit,"Bunday kalit so\'z mavjud emas"))

tarjima = key_py.get(kalit)
if tarjima == None:
    print("Bunday kalit so'z yo'q")
else:
    print(f"{kalit.title()} so'zining tarjimasi {tarjima} bo'ladi")