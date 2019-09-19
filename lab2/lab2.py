# James Park
# Sept. 12 2019
# Slope, dist between two points

import math

x1Str = input("Enter x1:")
y1Str = input("Enter y1:")
x2Str = input("Enter x2:")
y2Str = input("Enter y2:")

x1 = float(x1Str)
y1 = float(y1Str)
x2 = float(x2Str)
y2 = float(y2Str)

slope = (y2 - y1) / (x2 - x1)
dist = math.sqrt(abs((x2 - x1)**2 + (y2 - y1)**2))

print("The slope for the line that connects two points")
print("(", x1, ", ", y1, ") and (", x2, ", ", y2, ") is ", slope, ".", sep="")
print("The distance between the two points is", dist)

