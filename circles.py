"""
circles
file: circles.py
assignment: homework
author: Jesenia Roberts <jtr5657@rit.edu>
language: python3
purpose: draws circles in a recursive pattern based on user input
"""

import turtle as tt

depth = (int(input("Please enter depth: ")))

size = int(input("Please enter size: "))

tt.speed(0)

def draw_circles(s,d):
    """
    :param s: the size of the circle, input by user
    :param d: the depth of the recursion, input by user
    precondition: turtle is facing east, pen down
    post condition: turtle is facing east, pen down
    """
    if d == 0:
        pass
    else:
        tt.circle(s)
        tt.up()
        tt.left(90)
        tt.forward(s)
        tt.left(90)
        tt.forward(s)
        tt.right(180)
        tt.down()
        draw_circles((s / 2), d-1)
        tt.up()
        tt.forward(s *2)
        tt.down()
        draw_circles((s / 2), d-1)
        tt.up()
        tt.forward(-s)
        tt.right(90)
        tt.forward(s)
        tt.left(90)
        tt.down()

draw_circles(size,depth)
tt.done()
