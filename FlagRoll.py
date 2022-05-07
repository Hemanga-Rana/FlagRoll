from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
    color('green')
    circle(i)
    color('white')
    circle(i*0.8)
    color('darkorange')
    circle(i*0.5)
    right(3)
    forward(6)
done()