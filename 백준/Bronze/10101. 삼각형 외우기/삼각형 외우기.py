a = int(input())
b = int(input())
c = int(input())
if sum([a, b, c]) == 180:
    if a == b == c:
        print("Equilateral")
    elif a != b and a != c and b != c:
        print("Scalene")
    elif a == b != c or b == c != a or a == c != b:
        print("Isosceles")
else:
    print("Error")