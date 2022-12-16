# Rich Immanuel
#71180396

import turtle

s = turtle.Screen()
t = turtle.Turtle()
u = turtle.Turtle()

# R
t.penup()
t.goto(-30,50) 
t.pendown()
t.pensize(10)
t.pencolor("red")
t.right(90)
t.forward(150)
t.goto(-30,50)
t.right(-90)
t.circle(-50,180,100)
t.penup()
t.goto(0,-40)
t.left(135)
t.pendown()
t.forward(70)



u.penup()
#draw straight line
u.goto(50,10) #centering in the screen
u.pendown()

u.circle(30,180)



# u.pendown()
# u.pensize(10)
# u.pencolor("red")
 
# u.right(90)
# u.forward(100)


# def three(d):
#     point = pos()
#     for i in range(2):
#         fd(d)
#         rt(90)
#     fd(d)
#     for i in range(2):
#         bk(d)
#         rt(90)
#     bk(d)
#     pu()
#     goto(point)
#     pd()
#     setheading(0)


s.exitonclick()