from click._compat import raw_input


def tringle_are(x, y):
    k = 0.5 * x * y
    print(k)


b = int(raw_input("b:  "))
h = int(raw_input("h:  "))
tringle_are(b, h)

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
print(odds.union(evens))
print(odds.intersection(evens))
print(8 in evens)
print(8 not in evens)

