def solution(n, lost, reserve):
    answer = 0
    for i in range(n):
        if (i+1 in lost) and (i+1 in reserve):
            reserve.remove(i+1)
            lost.remove(i+1)
    for i in range(n):
        if i+1 not in lost:
            answer += 1                
        else:
            if (i in reserve):
                answer += 1
                reserve.remove(i)
            elif (i+2 in reserve):
                answer += 1
                reserve.remove(i+2)
    return answer