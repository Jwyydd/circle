# Area of a Circle
import math

radius_str = input("Enter the radius of the circle: ")
radius = int(radius_str)  # convert string to int
area = math.pi * (radius ** 2)
print("The area of the circle with radius " + str(radius) + " is " + str(area))
