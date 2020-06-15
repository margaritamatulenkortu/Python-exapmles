with open('/Users/margarita/Documents/Python-exapmles/text-files/guido_bio.txt') as fobj:
    bio = fobj.read()
print(bio)

f = open('/Users/margarita/Documents/Python-exapmles/text-files/guido_bio.txt')
text = f.read()
f.close()
print(text)


oceans = ["Pacific", "Atlantic", "Indian", "Artic","Artic"]
with open('/Users/margarita/Documents/Python-exapmles/text-files/oceans.txt', "w") as f:
    for i in oceans:
       print(i, file=f)
        # f.write(i)
        # f.write("\n")
numbers = [1, 3, 46, 6, 7]

with open('/Users/margarita/Documents/Python-exapmles/text-files/oceans.txt', "a") as f:
    for i in numbers:
       print(i, file=f)
       print("Jeah!", file=f)
        # f.write(i)
        # f.write("\n")


