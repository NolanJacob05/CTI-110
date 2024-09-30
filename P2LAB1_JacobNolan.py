# Nolan Jacob
# 9/30/24
# P2LAB1
# Using an imported library, math, and an f string

#import library
import math

#get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate Diameter
diameter = radius * 2

# disply diameter with 1 decimal place
print(f"The diameter of the circle is {diameter:.1f}")
print()

# calculate Circumference
circumference = 2 * math.pi * radius

# display circumference
print(f"The circumference of the circle is {circumference:.2f}")
print()

#calculate area of the circle
area = radius ** 2 * math.pi

# display area
print(f"The area of the circle is {area:.3f}")
