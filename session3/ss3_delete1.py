hobbies = ['death note', 'netflix', 'teaching']
hobbies_size = len(hobbies)
print("*"*30)
for index, item in enumerate(hobbies):
    print(index + 1, ". ", item, sep="")
print("*"*30)

pos = int(input("Position you want to remove? "))
if  0 < pos <= hobbies_size:
    hobbies.pop(pos - 1)

    print("*"*30)
    for index, item in enumerate(hobbies):
        print(index + 1,". ", item, sep="")
    print("*"*30)

else:
    print("Your input is incorrect")