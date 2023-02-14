from turtle import*
speed('fast')
pencolor('blue')

# hexagon
for i in range(6):
    pensize(5)
    fd(100)
    for i in range(6):
        pensize(3)
        fd(50)
        for i in range(6):
            pensize(1)
            fd(25)
            dot(10)
            rt(60)
        rt(60)
    rt(60)

hideturtle()
mainloop()