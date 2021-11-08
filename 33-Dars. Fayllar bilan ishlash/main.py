import pickle

# with open('fayl.txt') as file:
#     bilim = file.read().replace('\n',' ')
# print(bilim)

# with open('pi_million_digits.txt') as file:
#     PI =file.read().replace('\n','')
# PI = PI.replace(' ','')
# PI = PI.rstrip()
# PI = float(PI)

# birthdate = '25071999'
#
# if birthdate in PI:
#     print('bor')
# else:
#     print('yo\'q')

# PI = float(PI)
#
# with open('PI_pkl','wb') as file:
#     pickle.dump(PI,file)
#
# with open('PI_pkl','rb') as file:
#     new_pi = pickle.load(file)
#
# print(new_pi)
i = 1
while True:
    book = input("Uyingizda mavjud kitoblarni kiriting (kiritib bo'lgach enterni bosing): ")
    if not book: break
    with open('kitoblar.txt','a') as file:
        file.write(str(i) + '.' + book + '\n')
    i = int(i)
    i+=1