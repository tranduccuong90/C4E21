from random import shuffle, choice

library = ["champion","international", "intelligence", "skyscrapper"]

word = choice(library)
chars = list(word)
length = len(chars)

shuffle(chars)
for i in range(length):
    print(chars[i], end=' ')
print()
answer = input("Your answer: ")
if answer == word:
    print("Hura")
else:
    print(":(")
