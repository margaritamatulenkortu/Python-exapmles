from math import pi
import math

def circle(r):
    return pi*(r**2)

#tests
radii = [2, 0, -3, 2 +5j, True, "rad"]
message = "Are of circules is r = {radius} is {area}"

for r in radii:
    A = circle(r)
    print(message.format(radius=r, area=A))