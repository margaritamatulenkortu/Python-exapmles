import math

from click._compat import raw_input


def volume(r):
    v = (4.0/3.0) * math.pi * r**3
    print("volume of ball is ", v)
    return v
volume(int(raw_input("Radiouss of ball:  ")))