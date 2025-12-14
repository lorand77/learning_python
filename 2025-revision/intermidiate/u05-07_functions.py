# Defines a function with one required parameter and one default parameter
# Uses a loop
# Prints a repeated character pattern
# Uses string multiplication
# Calls the function at least once

def draw_square(height, paint="X"): #only works well for specific squares
    for i in range(height):
        print(paint * int(height * 2.2))

print(draw_square(10))
print(draw_square(10, "X"))
print(draw_square(10, "O"))
print(draw_square(4))
print(draw_square(8))
