"""
Bow Ties
file: bowties.py
author: Jesenia Roberts
language: python3
description: lab 03 solution
program draws bow ties based on user input
"""

import turtle as tt


depth = int(input("Please enter a depth "))


def draw_one_bowtie(size):

    """ creates a single bow tie shape composed of two purple triangles with a red circle in the center
    pre-condition: turtle is facing east, pen down
    post-condition: turtle is facing east, pen down
    """

    tt.color("purple")
    tt.left(30)
    tt.forward(size)
    tt.right(120)
    tt.forward(size)
    tt.right(120)
    tt.forward(2 * size)
    tt.left(120)
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.up()
    tt.right(120)
    tt.forward(size/4)
    tt.left(90)
    tt.down()
    tt.fillcolor("red")
    tt.begin_fill()
    tt.circle(size/4)
    tt.end_fill()
    tt.up()
    tt.left(90)
    tt.forward(size/4)
    tt.right(90)

def draw_bowties(size, depth):
    """
       :param size: determines length of triangle sides
       :param depth: input by user, determines how many times draw_one_bowtie is called
       draws bow ties by calling the draw_one_bowtie until the depth variable is satisfied
       """
    if depth == 0:
       pass

    else:
       draw_one_bowtie(size)
       tt.up()
       tt.left(30)
       tt.forward(2 * size)
       tt.down()
       draw_bowties(size / 3, depth - 1)
       tt.up()
       tt.forward(-2 * size)
       tt.right(60)
       tt.up()
       tt.forward(size*-2)
       tt.down()
       draw_bowties(size / 3, depth - 1)
       tt.up()
       tt.forward(2 * size)
       tt.right(150)
       tt.down()
       draw_one_bowtie(size)
       tt.up()
       tt.left(30)
       tt.forward(size*2)
       tt.down()
       draw_bowties(size / 3, depth - 1)
       tt.up()
       tt.forward(-2*size)
       tt.right(60)
       tt.forward(-2*size)
       tt.down()
       draw_bowties(size / 3, depth - 1)
       tt.up()
       tt.forward(size * 2)
       tt.left(210)



draw_bowties(100, depth)
tt.setup(1000, 1000)
tt.done()
