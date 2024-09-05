def solution(n):
    answer = 0
    
    for i in range(1,n//2+1):
        s = 0
        while s<n:
            s+=i
            if s==n:
                answer+=1
                break
            i+=1
    
    return answer+1