import math
import statistics

def area(r):
    """"Are with circle with raduis 'r'. """
    return math.pi * (r ** 2)


raddi = [6, 5, 7.4, 0.7]
# first method
areas = []
for r in raddi:
    a = area(r)
    areas.append(a)

# print(areas)

# secon method

# print(list(map(area, raddi)))

temps = [("Riga", 15), ("Talinn", 18), ("Vilnus", 19), ("Berlin", 20)]

c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)

print(list(map(c_to_f, temps)))

data = [1, 4, 5, 8]
avg = statistics.mean(data)
print(avg)
print(list(filter(lambda x: x > avg, data)))
#remove missing data

city =["Riga", "Talinn", "", "Vilnus", "Berlin", ""]

print(list(filter(None, city)))  
