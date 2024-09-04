def solution(land):
    answer = 0
    dp = [[0] * 4 for _ in range(len(land))]
    
    for i in range(4):
        dp[0][i]=land[0][i] 
        
    for i in range(len(land)):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i-1][k] for k in range(4) if k != j)
    
    return max(dp[-1])