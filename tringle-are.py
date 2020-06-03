from click._compat import raw_input


def tringle_are(x, y):
    k = 0.5 * x * y
    print(k)


b = int(raw_input("b:  "))
h = int(raw_input("h:  "))
tringle_are(b, h)
