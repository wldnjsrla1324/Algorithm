def solution(n, money): #DP 예제..
    answer = 0
    
    dp = [0 for i in range(n + 1)] #합 갱신할 리스트
    dp[0] = 1
    #print(dp)
    
    for m in money:
        for p in range(m, n + 1):
            #print(p)
            if p >= m:
                dp[p] += dp[p - m]
        #print(dp)
    
    return dp[-1]