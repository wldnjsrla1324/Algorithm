def solution(s):
    answer = 0
    
    a, b = 0, 0
    start=s[0]
    for i in range(len(s)):
        if a!=0 and a==b:
            answer+=1
            start=s[i]
            print(s[i])
        if s[i]==start:
            a+=1
        elif s[i]!=start:
            b+=1
        
    return answer+1