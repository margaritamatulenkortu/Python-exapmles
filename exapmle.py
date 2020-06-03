from click._compat import raw_input

print("Hello Wrold")
massage = "\"'Meet me\' tonight'\""
print(massage)
a = 443656
b = 34.55
c = 2j
print(type(a))
print(type(b))
print(type(c))


input = raw_input("Isert ss: ")

if len(input) < 6:
    print("too short")
else:
    print("good")

input1 = raw_input("Ievadi skaitli ")
number = int(input1)
if number % 2 == 0:
    print("its even")
else:
    print("its odd")