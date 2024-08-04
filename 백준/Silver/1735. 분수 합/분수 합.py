import math

a, b = map(int, input().split())
c, d = map(int, input().split())
GCD = math.gcd(a * d + b * c, b * d)

# 분모, 분자를 각각 최대공약수로 나눈 것이 기약분수
print((a * d + b * c) // GCD, (b * d) // GCD)
