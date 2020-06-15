planets = [
    ('Merury', 1234, 4.4, 0.6542),
    ('Venus', 14334, 5.4, 0.6542),
    ('Neptun', 8234, 1.4, 0.6542),
    ('Uranus', 2234, 9.4, 0.6542),
    ('Jupiter', 234, 6.4, 0.6542),
    ('Erth', 6234, 11, 0.6542)]
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print(planets)

density = lambda planet: planet[2]
planets.sort(key=density)
print(planets)

planets = [
    'Merury'
    'Venus',
    'Neptun',
    'Uranus',
    'Jupiter',
    'Erth']
soreted_planetes = sorted(planets)
print(soreted_planetes)

data = (5, 65, 7, 89, 76)
print(sorted(data, reverse=True))
print(sorted("Alfabetically"))
