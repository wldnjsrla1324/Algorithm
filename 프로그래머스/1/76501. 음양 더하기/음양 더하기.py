def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True: #양수
            answer+=absolutes[i]
        else: #홀수
            answer-=absolutes[i]
    return answer