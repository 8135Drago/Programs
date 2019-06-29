from turtle import *
import random

for n in range(50):
    penup()
    goto(random.randint(-100,100),random.randint(-100,100))
    pendown()

    ra = random.randint(50,100)/100
    ba = random.randint(0,30)/100
    ga = random.randint(0,10)/100

    pencolor((ra,ba,ga))

    cs = random.randint(10,40)
    pensize(random.randint(4,6))

    for i in range(6):
        circle(cs)
        left(60)
