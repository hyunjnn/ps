a = int(input())
b = int(input())
c = int(input())
if sum([a, b, c]) == 180:
    if a == 60 and b == 60 and c == 60:
        print("Equilateral")
    elif a != b and a != c and b != c:
        print("Scalene")
    elif a == b != c or b == c != a or a == c != b:
        print("Isosceles")
else:
    print("Error")