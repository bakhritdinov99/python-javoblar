# ismlar = ['Zafar', 'Alijon', 'Savlat']
# print("Salom " + ismlar[0]+" aka. Darsni ko'rdizmi?")
# print(ismlar[1]+", Siz nega bugun ishga kelmadingiz?")
# print("O'qishing natijasi yaxshi bo'ldimi, " + ismlar[2]+"?")

# sonlar = [48,50,-15,6.58]
#
# print(sonlar[0]+sonlar[2])
# sonlar[3] = 7
# print(sonlar[3]*156)

# t_shaxslar = ["Imom Buxoriy", "Ibn Sino", "at-Termiziy", "al-Xorazmiy"]
# z_shaxslar = ["Stive Jobs", "Bill Gates", "Mark Zukerberk", "Gvido Van Russom"]
#
# print(f"{t_shaxslar[3]} o\'z zamonasining buyuk namoyondasi bo'lgani kabi, {z_shaxslar[2]} ham bugungi zamonning buyuk shaxslaridan biridir. ")

friends =[]
friends.append("Zafar aka")
friends.append("Madina")
friends.append("Alijon")
friends.append("Doniyor")
friends.append("Sherzod")
friends.append("Sug'diyona")

print(friends)

friends.remove("Madina")
friends.remove("Sug'diyona")

print(friends)

mehmonlar = []

meh1 = friends.pop(0)
meh2 = friends.pop(0)
mehmonlar.append(meh1)
mehmonlar.append(meh2)
print(mehmonlar)
print(friends)