from turtle import *
shape("turtle")
speed(0)
distance = 10
for i in range (100):
    forward(10 + distance)
    left(90)
    distance = distance + 5 # distance +=5
mainloop()


