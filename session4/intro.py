# person = ["Quan", 20, "Hanoi", "Thang Long", 3, "Da Nang"]
# print(person)

# person = {

# }

# print(person)

# person = {
#     "name": "Quan"

# }
# print(person)


person = {
    "name": "Quan",
    "age": 20,
    "city": "Hanoi",
}

# print(person["status"])
# person["status"] = "complicated"
# print(person)

# del person["age"]
# print(person)

for k in person: #for x in person.keys():
    print(k)

for v in person.values():
    print(v)

for k,v in person.items():
    print(k,":", v)

# print(person)
# print(person["city"])
# person["city"] = "Da Nang"
# print(person)

# key = "city"
# print(person[key])