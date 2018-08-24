from random import shuffle, choice

word = "champion"
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
