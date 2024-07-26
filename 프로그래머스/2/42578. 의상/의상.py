def solution(clothes):
    answer = 1

    dic = {}

    for clo in clothes:
        if clo[1] not in dic.keys():
            dic[clo[1]] = 1
        else:
            dic[clo[1]] += 1

    for key, value in dic.items():
        answer *=(value + 1)
    
    return answer-1