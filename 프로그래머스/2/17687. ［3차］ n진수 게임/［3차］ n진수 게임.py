def solution(n, t, m, p):
    answer = ''
    
    #n진수 구하기
    def n_number(num, n):
        rest = []
        while num>=n:
            r = num%n
            rest.append(r)
            #print(rest)    
            num //= n
            #print(num)
        rest.append(num)
        #print(rest)
        b = ["A", "B", "C", "D", "E", "F"]

        for i in range(len(rest)):
            idx = rest[i] - 10
            if idx >=0:
                rest[i] = b[idx]
            else:
                rest[i] = str(rest[i])

        
        return "".join(rest[::-1])
        
    
    game = ''
    cur = p - 1
    for num in range(t * m):
        game += n_number(num, n)
    while 1:
        if len(answer) == t:
            break
        answer += game[cur]
        cur += m
            
    
    return answer