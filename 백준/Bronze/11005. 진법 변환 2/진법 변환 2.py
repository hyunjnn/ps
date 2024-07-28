def solution(n, q):
    
    rev_base = ''
    arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += arr[mod]
        
    return rev_base[::-1]


n, b = map(int, input().split())
print(solution(n, b))