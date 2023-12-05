import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = 2 * radius
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Specify radius or diameter")

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle with radius: {self.radius} and diameter: {self.diameter}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)
circle3 = Circle(radius=3)

print(circle1.area)
print(circle2)

combined_circle = circle1 + circle3
print(combined_circle.radius)


print(circle1 < circle2)
print(circle1 > circle3)

circle_list = [circle1, circle2, circle3]
sorted_circles = sorted(circle_list, key=lambda x: x.radius)
print([str(circle) for circle in sorted_circles]) 