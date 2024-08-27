def solution(routes):
    answer = 0
    routes.sort(key = lambda x:(x[1])) 
    print(routes)
    cur = -30001
    
    for r in routes:
        if r[0]>cur:
            answer+=1
            cur = r[1]
    return answer