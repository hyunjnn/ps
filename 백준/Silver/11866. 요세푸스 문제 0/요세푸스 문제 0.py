n, k = map(int, input().split())
queue = [i + 1 for i in range(n)]
idx = 0

res = []
while queue:
    idx += k - 1
    if idx > len(queue) - 1:
        idx = idx % len(queue)

    res.append(str(queue[idx]))
    queue.remove(queue[idx])

print("<", ", ".join(res), ">", sep='')
