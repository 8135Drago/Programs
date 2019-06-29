from turtle import *

def main():
    c = ('violet','indigo','blue','green','yellow','orange','red')
    reset()
    Screen()
    up()
    goto(-320,-195)
    width(68)
    for pcolor in c:
        color(pcolor)
        down()
        forward(620)
        up()
        backward(620)
        left(90)
        forward(65)
        right(90)
    width(10)
    color('white')
    goto(0,-170)
    down()

    circle(170)
    left(90)
    forward(340)
    up()
    left(180)
    forward(170)
    right(45)
    down()
    forward(170)
    up()
    backward(170)
    left(90)
    down()
    forward(170)
    up()
    goto(0,300)
    
if __name__ == "__main__":
         main()
         mainloop()
    
