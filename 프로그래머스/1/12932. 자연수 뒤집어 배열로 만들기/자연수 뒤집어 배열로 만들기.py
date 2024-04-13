def solution(n):
    answer = []
    n = str(n) #문자열로 변환
    for i in n:
        i=int(i) # 다시 정수형으로 변환
        answer.append(i)
    answer.reverse() # sort가 아닌 이유는 단순히 뒤집어서 출력하라고했기 때문에 정렬문제 X
    return answer