import turtle  

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(restart, 'Escape')
turtle.listen()

turtle.mainloop()