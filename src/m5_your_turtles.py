"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Tyler Nottingham.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
Tyler = rg.SimpleTurtle("turtle")
Tyler.speed = 5

TD =  rg.SimpleTurtle("turtle")
TD.speed = 5

Tyler.right(90)
Tyler.forward(150)
Tyler.left(90)

TD.backward(150)
TD.right(90)
TD.forward(150)
TD.left(90)

Tyler.pen = rg.Pen('green', 5)
TD.pen = rg.Pen('blue', 5)

circle = 150
square = 300
for k in range (15):

    Tyler.draw_circle(circle)
    TD.draw_square(square)

    Tyler.pen_up()
    Tyler.left(90)
    Tyler.forward(10)
    Tyler.right(90)

    TD.pen_up()
    TD.backward(10)
    TD.right(90)
    TD.forward(10)
    TD.left(90)

    TD.pen_down()
    Tyler.pen_down()
    circle = circle - 10
    square = square + 20

window.close_on_mouse_click()


