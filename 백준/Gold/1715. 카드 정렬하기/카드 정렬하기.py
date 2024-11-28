from heapq import heappush, heappop

N = int(input())

hq = []
for _ in range(N):
    n = int(input())
    heappush(hq, n)

count = 0  

while hq:
    if len(hq) == 1:
        break
    a = heappop(hq)
    b = heappop(hq)
    heappush(hq, a + b)
    count += (a + b)
print(count)