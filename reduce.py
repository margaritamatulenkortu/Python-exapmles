from functools import reduce
#multiplay all numbers in list
data = [1, 2, 3]
multiplayer = lambda x, y: x*y
print(reduce(multiplayer,data))

#old verison
value = 1
for i in data:
    value = value * i
print(value)