def solution(numbers, target):
    answer = 0
    total = 0
    
    def dfs(i,total,n_len):
        i += 1
        nonlocal answer
        if i >= n_len:
            if total == target:
                answer += 1
        else:
            dfs(i,total+numbers[i],n_len)
            dfs(i,total-numbers[i],n_len)
        
    dfs(-1,total,len(numbers))
    
    return answer