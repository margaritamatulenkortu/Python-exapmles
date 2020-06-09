import random
def random_walk_2(n):
    x, y =0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return x, y


for i in range(25):
    walk = random_walk_2(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))
# monte carlo
numbers_of_walks = 10000
for walk_length in range(1, 31): # take 30 walks
    no_transport = 0 # number of walsk 4 of fewer block from home
    for i in range(numbers_of_walks):
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_pr = float(no_transport) / numbers_of_walks
    print("Walks size = ", walk_length, "/% of no transport = ", 100 * no_transport_pr)
