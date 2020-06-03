from click._compat import raw_input

a = int(raw_input("Lengt of side a = "))
b = int(raw_input("Lengt of side b = "))
c = int(raw_input("Lengt of side c = "))
if a > 0 and b > 0 and c > 0:
    if a == b and b == c:
        print("equalatteral tringle")
    elif a != b and b != c and c != a:
        print("Salene tringle")
    else:
        print("Isoscale tringle")
else:
    print("negative numbers are not allowed")

