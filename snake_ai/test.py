from turtle import *
import math
import numpy as np

line_array = [[0, 0, ]]

def draw_triangle(start_pos, start_heading, length):
    penup()
    setpos(start_pos)
    pendown()
    setheading(start_heading)
    for i in range(3):
        forward(length)
        left(120)

def iteration(bases, max_it, it, length):
    new_bases = []
    for i in range(3 * (4 ** it)):
        k = (bases[i][1] - bases[i][3]) / (bases[i][0] - bases[i][2]) # Calculate Ration
        d = (bases[i][1] - k * bases[i][0]) # Calculate d

        # Calculate starting point of new triangle
        x = bases[i][0] + ((bases[i][2] - bases[i][0]) / 3)
        y = k * x + d
        draw_triangle((x, y), bases[i][4] - 60, length / 3)  # Draw Triangle

        # Calculate new bases
        new_bases.append([bases[i][0], bases[i][1], bases[i][0] + ((bases[i][2] - bases[i][0]) / 3), bases[i][1] + ((bases[i][3] - bases[i][1]) / 3), bases[i][4]])
        new_bases.append([bases[i][0] + 2 * ((bases[i][2] - bases[i][0]) / 3), bases[i][1] + 2 * ((bases[i][3] - bases[i][1]) / 3), bases[i][2], bases[i][3], bases[i][4]])

        new_bases.append([x, y, x + math.cos(math.radians(bases[i][4] - 60)) * length / 3, y + math.sin(math.radians(bases[i][4] - 60)) * length / 3, bases[i][4] - 60])
        new_bases.append([x + math.cos(math.radians(bases[i][4] - 60)) * length / 3, y + math.sin(math.radians(bases[i][4] - 60)) * length / 3, ])
        print(new_bases)


    it += 1
    if max_it != it:
        iteration(new_bases, max_it, it, length / 3)

def koch_snowflake(iterations, length):
    # Start Cords, End Cords, angle
    bases = [[0, 0, length, 0, 0], # AB
              [length, 0, length / 2,  math.sin(math.radians(60)) * length, 120], # BC
              [length / 2,  math.sin(math.radians(60)) * length, 0, 0, 240]] # CA

    draw_triangle((0, 0), 0, length)
    iteration(bases, iterations, 0, length)

koch_snowflake(3, 120)

