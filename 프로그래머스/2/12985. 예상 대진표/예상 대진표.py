def solution(n,a,b):
    answer = 0
    lst = [_ for _ in range(1,n+1)]
    
    while True:
        if a%2==1:
            a+=1
        if b%2==1:
            b+=1
        if a==b:
            answer+=1
            break
        else:
            a=a//2
            b=b//2
            answer+=1
    return answer