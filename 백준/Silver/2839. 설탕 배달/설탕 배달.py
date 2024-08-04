n = int(input())

if n % 5 == 0: # 5kg 봉지 만으로 배달 가능한 경우
    print(n // 5)
else:
    res = 0
    while True:
        n -= 3
        res += 1

        # 3kg 봉지 만으로 배달 가능한 경우
        if n == 0:
            print(res + n // 3)
            break
        # 3kg 봉지와 5kg 봉지를 모두 사용해 배달 가능한 경우
        elif n % 5 == 0:
            print(res + n // 5)
            break
        # 정확히 n kg을 만들 수 없는 경우
        elif n == 1 or n == 2:
            print(-1)
            break