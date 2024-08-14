def solution(n):
    answer = []
    
    def hanoi(n, start, inter, end):
        if n==1:
            answer.append([start,end])
        
        else:
            hanoi(n-1, start, end, inter)
            hanoi(1, start, inter, end)
            hanoi(n-1, inter, start, end)
    
    hanoi(n, 1, 2, 3)
    return answer


