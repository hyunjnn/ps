n = int(input())
num_arr = []
for _ in range(n):
    num_arr.append(int(input()))
num_arr.sort()   
for i in num_arr:
    print(i)