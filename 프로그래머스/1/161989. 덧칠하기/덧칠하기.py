def solution(n, m, section):
    answer = 0
            
    cur = 0
    for sec in section:
        if sec>cur:
            answer+=1
            cur = sec+m-1
            
        
    return answer