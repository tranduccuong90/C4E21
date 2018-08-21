
n = int(input("Enter a number: "))
for i in range(n+1):
    if i % 2 != 0:
        print("* ", end = ' ')
    else:
        print("x ", end = ' ')
print()
