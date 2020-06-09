v = [1, -4, 6]
print(4*v)
print([4*x for x in v])
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
certesian_product = [(a, b) for a in A for b in B]
print(certesian_product)
print(len(certesian_product))