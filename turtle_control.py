import turtle  

def move_w():
    turtle.setheading(90)
    turtle.stamp()
    turtle.forward(50)  

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(restart, 'Escape')
turtle.onkey(move_w,'w')
turtle.listen()

turtle.mainloop()