import json
#
# data = {
#     "Model" : "Malibu",
#     "Rang" : "Qora",
#     "Yil":2020,
#     "Narh":40000
# }

# data_json = json.dumps(data)

# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
#
# talaba = json.loads(talaba_json)

# print(data_json)

# print(talaba['ism'], talaba['familiya'])

# with open('data.json','w') as file:
#     json.dump(data,file)
#
# with open('talaba.json','w') as file:
#     json.dump(talaba,file)

# with open('students.json') as file:
#     talabalar = json.load(file)
#
# # print(talabalar)
# # print(talabalar['student'])
#
# for x in talabalar['student']:
#     print(f"{x['name']} {x['lastname']}, {x['year']}-kurs, {x['faculty']} fakulteti talabasi")

with open('api-result.json') as file:
    python_wiki = json.load(file)

print(python_wiki['query']['pages']['13801']['title'])
print(python_wiki['query']['pages']['13801']['extract'])