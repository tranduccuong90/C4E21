from turtle import *

shape("turtle")
speed(0)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

# for i in range(len(colors)):
#     angle = 360/(i+3)
#     for j in range(i+3):
#         forward(100)
#         left(angle)
#     color(colors[i])



for i, mau in enumerate(colors):
    angle = 360/(i+3)
    for j in range(i+3):
        forward(100)
        left(angle)
    color(mau)


mainloop()
