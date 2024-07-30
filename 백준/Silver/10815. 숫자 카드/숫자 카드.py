from sys import stdin

n = int(input())
cards = set(list(map(int, stdin.readline().split())))
m = int(input())
numbers = list(map(int, stdin.readline().split()))

for i in numbers:
    if {i} - cards == set():
        print(1, end=' ')
    else:
        print(0, end=' ')