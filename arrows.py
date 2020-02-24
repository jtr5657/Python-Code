"""
Arrows
file: arrows.py
author: Jesenia Roberts
language: python3
description: lab 04 solution
"""

import turtle as tt
import math
import random

MAX_FIGURES = 500
MAX_DISTANCE = 30
MAX_ANGLE = 30
MAX_SIZE = 30
BOUNDING_BOX = 200


tt.colormode(255)
tt.speed(0)

seg = float(input("Please enter desired number of triangles between the numbers 0 and 500 : "))

if seg > 500:
    print(" Triangles must be between 0 and 500 inclusive ")


elif seg < 0:
    print(" Triangles must be between 0 and 500 inclusive ")

def triangle(length):
    """
    creates randomly colored triangles and moves turtle right or left 1
    :param length: length of sides of triangle
    """
    r = int(random.random()*255)
    g = int(random.random()*255)
    b = int(random.random()*255)
    tt.pencolor(r,g,b)
    tt.fillcolor(r,g,b)
    tt.begin_fill()
    tt.down()
    tt.forward(length)
    tt.left(120)
    tt.forward(length)
    tt.left(120)
    tt.forward(length)
    tt.left(120)
    tt.end_fill()
    tt.up()
    tt.left(random.randint(-MAX_ANGLE,MAX_ANGLE))




def draw_figures_rec(seg, total):
    length = random.randint(1, MAX_SIZE)
    if seg == 0:
        print("The total area painted is " + str(total) + " units")

    else:
        if tt.xcor() == 200 or tt.xcor() == -200 or tt.ycor() == 200 or tt.ycor == -200:
            tt.left(MAX_ANGLE)

        triangle(length)
        tt.forward(random.randint(1, MAX_DISTANCE))
        tt.left(random.randint(-MAX_ANGLE,MAX_ANGLE))
        area = calculate_area(length)
        total += area


        return draw_figures_rec(seg - 1, total)

def draw_figures_iter(seg):
    total = 0
    while seg > 0:
        length = random.randint(1, MAX_SIZE)
        triangle(length)
        tt.forward(random.randint(1, MAX_DISTANCE))
        tt.left(random.randint(-MAX_ANGLE, MAX_ANGLE))
        area= calculate_area(length)
        total+=area
        seg -= 1

    print("The total area painted is " + str(total) + " units")



def calculate_area(length):
    area = float((math.sqrt(3) / 4)*(length ** 2))
    return area


def main() :
    draw_figures_iter(seg)
    tt.reset()
    draw_figures_rec(seg, 0)
    tt.done()

if seg >=0 and seg <=500:
    main()


