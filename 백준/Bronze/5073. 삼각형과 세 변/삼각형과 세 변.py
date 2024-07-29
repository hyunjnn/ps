while True:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    min_val = min(arr)
    max_val = max(arr)
    mid_val = sum(arr) - min_val - max_val
    if min_val + mid_val <= max_val:
        print("Invalid")
    elif min_val == mid_val == max_val:
        print("Equilateral")
    elif (min_val == mid_val != max_val or
          min_val == max_val != mid_val or
          max_val == mid_val != min_val):
        print("Isosceles")
    else:
        print("Scalene")