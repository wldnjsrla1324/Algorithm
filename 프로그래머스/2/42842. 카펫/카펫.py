def solution(brown, yellow):
    answer = []
    #약수 구하기
    for i in range(1, yellow+1):
        if yellow%i == 0 and i <=yellow//i:
            if (i+2)*(yellow//i + 2) == (brown+yellow):
                answer.append(yellow//i+2)
                answer.append(i+2)
    return answer

