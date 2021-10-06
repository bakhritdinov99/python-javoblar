
# def kopaytma(*sonlar):
#     a=1
#     for i in sonlar:
#         a*=i
#     return a
#
# print(kopaytma(5,6,7))
# print(kopaytma(8,2,-1))

def talabalar(ism,fam,**malumot):
    malumot['ismi'] = ism
    malumot['fam'] = fam
    return malumot

talaba = talabalar('Farrux','Baxritdinov', kursi = 4, guruhi='210-18', xonasi = 207)

print(talaba)