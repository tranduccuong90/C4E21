from collections import OrderedDict

import pyexcel

r1 = {
    "#": 1,
    "name": "Huy",
    "level": 25,
    "hour": 14,
}

r2 = {
    "#": 2,
    "name": "Hoa",
    "level": 20,
    "hour": 7,
}

r3 = {
    "#": 3,
    "name": "Tam",
    "level": 15,
    "hour": 30,
}

table = [r1, r2, r3]
print(table)

total = 0
wage_list = []
for salary in table:
    name = salary["name"]
    hour = salary["hour"]
    level = salary["level"]
    wage_info = OrderedDict({
        "name": name,
        "wage": hour * level
    })
    wage_list.append(wage_info)

    wage = hour * level
    total += wage

print("Total Budget is: ", total)
print(wage_list)

pyexcel.save_as(records = wage_list, dest_file_name = "wage_list.xlsx")




