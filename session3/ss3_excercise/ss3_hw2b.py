from turtle import *

shape("turtle")
speed(0)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for i in range(len(colors)):
    color(colors[i])
    begin_fill()


    for j in range(2):
        left(90)
        forward(100)
        left(90)
        forward(50)
            
    end_fill()
    forward(50)





# for i, mau in enumerate(colors):
#     angle = 360/(i+3)
#     for j in range(i+3):
#         forward(100)
#         left(angle)
#     color(mau)


mainloop()
