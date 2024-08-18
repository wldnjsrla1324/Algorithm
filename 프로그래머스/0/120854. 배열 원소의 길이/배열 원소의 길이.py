def solution(strlist):
    answer = []
    for str in strlist:
        cnt = 0
        for s in str:
            cnt+=1
        answer.append(cnt)
    
    return answer