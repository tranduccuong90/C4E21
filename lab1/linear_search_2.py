items = [1, 3, 6, 7,4,32, -45, -3]
x = int(input('Enter a number: '))
if x in items:
    print("Found")
    found_index = items.index(x)
    print(found_index)
else: 
    print("Not found")