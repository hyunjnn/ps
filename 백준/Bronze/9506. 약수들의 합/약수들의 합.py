while True:
    n = int(input())
    if n == -1:
        break

    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)

    if sum(arr) == n:
        print(f"{n} = ", end="")
        for k in arr:
            print(k, end="")
            if k != arr[-1]:
                print(" + ", end="")
        print()
    else:
        print(f"{n} is NOT perfect.")