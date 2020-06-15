import time
import math
def in_prime_v1(n):
    """"REturn true if number is prime in range of n-1"""
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
        else:
            return True

# for n in range(1, 21):
#     print(n, in_prime_v1(n))
t0 = time.time()
for n in range(1, 100000):
    in_prime_v1(n)
t1 = time.time()
print("Time requared: ", t1 - t0 )


def is_prime_v2(n):
    """"REturn true if number is prime in range of n-1 just better version faster"""
    if n == 1:
        return False
    max_division = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_division):
        if n % d == 0:
            return False
    return True
# for n in range(1, 21):
#      print(n, is_prime_v2(n))

t0 = time.time()
for n in range(1, 100000):
    is_prime_v2(n)
t1 = time.time()
print("Time requared: ", t1 - t0 )


def is_prime_v3(n):
    """"REturn true if number is prime in range of n-1 just better version much faster"""
    if n ==1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_division = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_division, 2):
        if n % d == 0:
            return False
    return True

# for n in range(1, 21):
#      print(n, is_prime_v3(n))

t0 = time.time()
for n in range(1, 100000):
    is_prime_v3(n)
t1 = time.time()
print("Time requared: ", t1 - t0)
