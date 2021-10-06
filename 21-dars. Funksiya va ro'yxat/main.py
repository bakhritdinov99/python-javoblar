# xonadoshlar = ["zafar og'a", "alijon","doniyor","muhriddin","sherzod","bobur aka"]
#
# def bosh_harf(xona):
#     xonadoshlar_b = []
#     while xona:
#         xonadosh = xona.pop()
#         xonadoshlar_b.append(xonadosh.title())
#     return xonadoshlar_b
#
#
# print(bosh_harf(xonadoshlar))

# xonadoshlar = ["zafar og'a", "alijon","doniyor","muhriddin","sherzod","bobur aka"]
#
# def bosh_harf(xona):
#     xonadoshlar_b = []
#     while xona:
#         xonadosh = xona.pop()
#         xonadoshlar_b.append(xonadosh.title())
#     return xonadoshlar_b
#
#
# print(bosh_harf(xonadoshlar[:]))

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)