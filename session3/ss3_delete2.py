hobbies = ['death note', 'netflix', 'teaching']
hobbies_size = len(hobbies)
print("*" * 30)
for index, item in enumerate(hobbies):
    print(index + 1, ". ", item, sep="")
print("*" * 30)

cont = input("What favorite you wanna remove? ")
if cont in hobbies:
    hobbies.remove(cont)
else:
    print("Nah")

print("*" * 30)
for index, item in enumerate(hobbies):
    print(index + 1,". ", item, sep="")
print("*" * 30)
