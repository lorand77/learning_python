import math

class Circle:
    def __init__(self, radius, color):
        self.radius = radius 
        self.color = color

    def get_area(self):
        return math.pi * self.radius ** 2  
    
    def change_color(self, new_color):
        self.color = new_color

    def get_color(self):
        return self.color    


c1 = Circle(10, "red")
c2 = Circle(20, "blue")

print(c1)
print(type(c1))
print(type(1.2))

print(c1.radius)
print(c1.color)
c1.radius = 15
print(c1.radius)

print(c1.get_area())
print(c1.get_color())
c1.change_color("green")
print(c1.get_color())
print(c1.get_color)



