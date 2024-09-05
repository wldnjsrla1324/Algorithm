def solution(s):
    answer = True
    s = s.upper()
    p, y = 0, 0
    
    for i in range(len(s)):
        if s[i] == 'P':
            p+=1
        elif s[i] == 'Y':
            y+=1
    
    return True if p==y else False