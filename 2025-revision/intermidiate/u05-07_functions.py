# Defines a function with one required parameter and one default parameter
# Uses a loop
# Prints a repeated character pattern
# Uses string multiplication
# Calls the function at least once

from math import sqrt

def draw_square(height, paint="X"): #only works well for specific squares
    for i in range(height):
        print(paint * int(height * 2.2))

def draw_circle(radius, paint="X"):
    scale = 2.2    
    for y in range(radius, -radius-1, -1):
        x = round(scale * sqrt(radius ** 2 - y ** 2))
        print(" " * round(radius * scale - x) + paint * 2 * x)


draw_square(10)
draw_square(10, "X")
draw_square(10, "O")
draw_square(4)
draw_square(8)

draw_circle(8)
draw_circle(16)
