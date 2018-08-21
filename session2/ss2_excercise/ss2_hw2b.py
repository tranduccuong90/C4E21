from turtle import *
shape("turtle")
speed(0)

for i in range(3,7):
    angle = 360/i
    if i % 2 == 0:
        color("red")
    else:
        color("blue")
    for j in range(i):
        forward(100)
        left(angle)

mainloop()
