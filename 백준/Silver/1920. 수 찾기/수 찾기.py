from sys import stdin

n = int(input())
arr1 = list(map(int, stdin.readline().split()))
m = int(input())
arr2 = list(map(int, stdin.readline().split()))

arr1.sort()


def binary_sort(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


for i in range(m):
    res = binary_sort(arr1, arr2[i], 0, n - 1)
    if res is not None:
        print(1)
    else:
        print(0)