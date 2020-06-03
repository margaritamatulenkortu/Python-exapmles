from click._compat import raw_input
input = raw_input("Isert name: ")

if len(input) < 6:
    print("too short")
else:
    print("good")

input1 = raw_input("insert number: ")
number = int(input1)
if number % 2 == 0:
    print("its even")
else:
    print("its odd")