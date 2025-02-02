def solution(money):
    N = len(money)
    
    dp1=[-1]*N
    dp1[0]=money[0]
    dp1[1]=max(money[0], money[1])
    for i in range(2,N-1):
        dp1[i]=max(dp1[i], dp1[i-1], dp1[i-2]+money[i])
        
    dp2=[-1]*N
    dp2[0]=0
    dp2[1]=money[1]
    for i in range(2,N):
        dp2[i]=max(dp2[i], dp2[i-1], dp2[i-2]+money[i])
        
    return max(dp1[N-2], dp2[N-1])