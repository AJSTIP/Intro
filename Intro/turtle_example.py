import turtle as t
#
#t.setup(640, 500)
#
#t.bgcolor('red')
#
#t.speed(1)
#
#circlesize = t.numinput('Input circle size', 'What size do you want the circle?', 
#                        default=50, minval=0, maxval=100)
#t.circle(circlesize)
#
#t.exitonclick() #t.done() also does the same thing functionally

t.goto(100,50)
if t.xcor() >  150:
    t.goto(0,0)

t.exitonclick()