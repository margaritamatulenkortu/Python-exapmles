import random
# for i in range(10):
#     print(random.random())
#
# def myrandom():
#     #to genereaite random number between [3, 7)
#     return 4 * random.random() + 3
#
#
# for i in range(10):
#     print(myrandom())
#vienm'erigs sadalijums pec bella
for i in range(10):
    print(random.uniform(3,7))

#main'iga string randoms
outcoms = ["papirs", "skeres", "akmens"]
for i in range(10):
    print(random.choice(outcoms))
#metamais kaulins
for i in range(10):
    print(random.randint(1, 6))
#ap vertibu 5 saurs spektrs vai plasaks
for i in range(10):
    print(random.normalvariate(5, 0.02))