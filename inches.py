from click._compat import raw_input


def cm(feet=0, inches=0):
    inches_to_cm = inches * 2.54
    feet_to_inches = feet * 12 * 2.54
    print(inches_to_cm + feet_to_inches)
    return inches_to_cm + feet_to_inches


cm(feet=6, inches=5)


def g(y, x=0):
    print(x + y)
    return x + y


g(5)
g(5, x=4)
