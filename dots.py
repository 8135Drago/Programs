import turtle as tt
a = tt.Turtle()
c = ['violet','indigo','blue','green','yellow','orange','red']
dd = 5
w = 10
h = 15
a.penup()
for x in range(h):
    a.pencolor(c[x%7])
    for i in range(w):
        a.dot()
        a.forward(dd)
    a.left(180)
    a.forward(dd*w)
    a.right(180)
tt.done()
