from random import randint,choice
from calc import calculate
x = randint(0,9)
y = randint(0,9)
op = choice(["+","-","*","/"])
dif = randint(-1,1)
r = calculate(x, y, op) + dif


# if op == "+":
#     r = x + y + dif
# elif op == "-":
#     r = x - y + dif
# elif op == "*":
#     r = x * y + dif
# elif op == "/":
#     r = x / y + dif

print(x, op, y, "=", r)

user_ans = input("(Y,N) ?").upper()

if dif == 0:
    if user_ans == "Y":
        print("Yeah")
    else:
        print("Nah")


if dif != 0:
    if user_ans == "N":
        print("Yeah")
    else:
        print("Nah")

