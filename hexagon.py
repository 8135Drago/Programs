import turtle as t
c = ['violet','indigo','blue','green','yellow','orange','red']
a = t.Turtle()
for x in range(360):
    a.pencolor(c[x%7])
    a.width(x/100+1)
    a.forward(x*0.55)
    a.left(59)
t.done()
