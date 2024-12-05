n = 1000 - int(input())
count = 0
for i in [500, 100, 50 ,10, 5, 1]:
    if n // i > 0:
        count += (n // i)
        n -= (n // i) * i  
print(count)    