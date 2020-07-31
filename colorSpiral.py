import turtle

colors = ['red', 'yellow', 'green', 'purple', 'orange', 'blue']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(200):
    t.pencolor(colors[x%6])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)


