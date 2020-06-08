from functools import lru_cache
#simple slown version
def fibonocci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonocci(n - 1) + fibonocci(n - 2)


for n in range(1, 11):
    print(n, ":", fibonocci(n))


fibonoci_cache = {}


# example with memorizing last number in dictionaries


def fib(x):
    if x in fibonoci_cache:
        return fibonoci_cache[x]
    if x == 1:
        value = 1
    elif x == 2:
        value = 1
    elif x > 2:
        value = fib(x - 1) + fib(x - 2)
    fibonoci_cache[x] = value
    return value


for x in range(1, 101):
    print(x, ":", fib(x))


#simple fast version with lru cache module
@lru_cache(maxsize=1000)
def fi(y):
    if type(y) != int:
        raise TypeError("Must be int")
    if y < 1:
        raise ValueError("must be positive number")

    if y == 1:
        return 1
    elif y == 2:
        return 1
    elif y > 2:
        return fi(y - 1) + fi(y - 2)


for y in range(1, 101):
   # print(y, ":", fi(y))
    print(fi(y+1)/fi(y))

