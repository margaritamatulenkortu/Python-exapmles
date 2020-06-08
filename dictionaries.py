import sys
import timeit
import logging

post = {"username": "Nikpik", "password": "Pi", "age": 23}
post["year"] = 1999
print(post)
print(post["username"])
post2 = dict(username="Bulvkas", password="Pipiko", age=2, massage="boooko")
print(post2)

if "massage" in post2:
    print(post2['massage'])
else:
    print("no message")

try:
    print(post2['password'])
except KeyError:
    print("NO NO")

try:
    print(post['massage'])
except KeyError:
    print("NO massage")

for key in post:
    value = post[key]
    print(key, "=", value)

print("--------------")
print(post2.pop("massage"))
post2.update(messege="Hello Wrold")
for key, value in post2.items():
    print(key, "=", value)

list_eg = [1, 2, 34, 45, "a", "b"]
tuple_eg = (1, 2, 34, 45, "a", "b")
print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

list_test = timeit.timeit(stmt="[1,2,3,4]", number=100000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4)", number=100000000)
print("List time:", list_test, "tuple time: ", tuple_test)
