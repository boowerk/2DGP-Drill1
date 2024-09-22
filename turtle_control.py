import turtle  

def move_w():
    turtle.setheading(90)
    turtle.stamp()
    turtle.forward(50)  

def move_a():
    turtle.setheading(180)
    turtle.stamp()
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(restart, 'Escape')
turtle.onkey(move_w,'w')
turtle.onkey(move_a,'a')
turtle.listen()

turtle.mainloop()