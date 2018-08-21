favs = ['running', 'dota', 'reading', 'movie']
for i, item in enumerate(favs):
    print(i+1, item)
print("* " * 20)

command = input('What do you want? (C, R, U, D)')
if command == "C":
    newhob = input("Anything else?")
    favs.append(newhob)

elif command == "R":
    pass

elif command == "U":
    pos = int(input("What position you want to update? "))
    cont = input("What favorite you want to update? ")
    favs[pos] = cont

elif command == "D":
    pos = int(input("What position you want to remove? "))
    favs.pop(pos - 1)

for i, item in enumerate(favs):
    print(i+1, item)
print("* " * 20)

