def solution(n):
    answer = [[0 for _ in range(1, i + 1)] for i in range(1, n + 1)]
    ans = []
    
    l = sum(range(n + 1))
    i, j = 0, 0
    direction = 0
    k = 1
    
    while k <= l:
        answer[i][j] = k
        k += 1
        
        if direction == 0:  # 아래로 이동
            if i+1 < n and answer[i+1][j] == 0:
                i += 1
            else:
                direction = 1
                j += 1
        elif direction == 1:  # 오른쪽으로 이동
            if j+1 < len(answer[i]) and answer[i][j+1] == 0:
                j += 1
            else:
                direction = 2
                i -= 1
                j -= 1
        elif direction == 2:  # 대각선 위로 이동
            if i-1 >= 0 and j-1 >= 0 and answer[i-1][j-1] == 0:
                i -= 1
                j -= 1
            else:
                direction = 0
                i += 1
    
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            ans.append(answer[i][j])
    
    return ans
