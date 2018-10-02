from turtle import *

colors = ['red','blue','brown','yellow','gray']

for i in range(3,8):
    for j in range(i):
        forward(50)
        left(360/i)
        color(colors[i-3])


mainloop()
