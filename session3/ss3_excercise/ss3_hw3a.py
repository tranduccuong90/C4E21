items = ['T-Shirt', 'Sweater']


while True:
    command = input('Welcome to our shop, what do you want? (C, R, U, D) ').upper()
    if command == "C":
        new_item = input("Enter new item: ")
        items.append(new_item)

    elif command == "R":
        pass

    elif command == "U":
        pos = int(input("Update position? "))
        cont = input("New item? ")
        items[pos] = cont

    elif command == "D":
        pos = int(input("Delete position? "))
        items.pop(pos - 1)

    print(*items,sep=', ')