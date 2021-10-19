import random

print("Keling o'ylagan sonni topish o'ynaymiz!")

def son_top(x):
    a = 0
    son = random.choice(range(1,x+1))
    print(f"1 dan {x} gacha son o'yladim. Topa olasizmi?")
    while True:
        f_son = int(input(">>"))
        a+=1
        if son > f_son:
            print("Men o'ylagan son bundan kattaroq. Yana harakat qiling.")
        elif son < f_son:
            print("Men o'ylagan son bundan kichikroq. Yana harakat qiling.")
        else:
            print(f"TOPDINGIZ! {son} sonini o'ylagan edim. {a} ta taxmin bilan topdingiz. Tabriklayman!! ")
            break
    return a

def son_top_pc(x):
    a=0
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topishga harakat qilaman.")
    min_son = 1
    max_son = x
    while True:
        son = random.randint(min_son, max_son)
        f_son = input(f"Siz {son} sonini o'yladingiz: to'g'ri(T), men o'ylagan son bundan kattaroq(+), men o'ylagan son bundan kichikroq(-)??")
        a+=1
        if f_son == 'T':
            print(f"Soningizni {a} ta taxmin bilan topdim!")
            break
        elif f_son =='+':
            min_son = son + 1
        elif f_son == '-':
            max_son = son - 1
    return a

def natija(x=10):
    while True:
        k = son_top(x)
        m = son_top_pc(x)
        if k == m:
            print(f"Durrang! Ikkimiz ham {k} ta taxmin bilan topdik.")
        elif k < m:
            print(f"Siz {k} ta taxmin bilan topdingiz va yutdingiz.")
        else:
            print(f"Men {m} ta taxmin bilan topdim va yutdim")
        yana = input("Yana o'ynaymizmi: ha(1)/yo'q(0): ")
        if yana == '0':
            break

natija()