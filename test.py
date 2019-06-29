import turtle as tt
for i in range(0,5):
    a = tt.circle(25)
    if i%2 == 0:
        tt.sety(-15)
    else:
        tt.sety(+5)
    tt.forward(25)
tt.forward(100)
tt.done
