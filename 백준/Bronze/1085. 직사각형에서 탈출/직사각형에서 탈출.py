x, y, w, h = map(int, input().split())
dist = [x - 0, w - x, y - 0, h - y]
print(min(dist))