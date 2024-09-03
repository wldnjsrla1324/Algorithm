def solution(n):
    answer = [0]*(n+1)
    answer[1] = 1
    answer[2] = 2
    for i in range(3,n+1):
        answer[i] = (answer[i-2] + answer[i-1])% 1000000007
    return answer[-1]