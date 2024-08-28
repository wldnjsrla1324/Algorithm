def solution(s):
    answer = ''
    lst = []
    temp = ''
    
    for i in range(len(s)):
        if s[i]==" ":
            lst.append(int(temp))
            temp = ''
        elif i == (len(s)-1):
            temp+=s[i]
            lst.append(int(temp))
        elif s[i]!=" ":
            temp+=s[i]
    
    answer+=str(min(lst))
    answer+=' '
    answer+=str(max(lst))
    return answer