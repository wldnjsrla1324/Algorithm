def solution(n):
    answer = n+1
    
    def jinsu(n):
        #a = ''
        cnt=0
        while n>0:
            r = n%2
            if r==1:
                cnt+=1
            #a+=(str(r))
            n //= 2
        return cnt
    
    while True:
        if jinsu(n)==jinsu(answer):
            return answer
        else:
            answer+=1