def solution(s):
    result = []
    answer = []
    
    answer= list(s[2:-2].split('},{'))
    answer.sort(key = lambda x:len(x))
    temp={}
    for a in answer:
        a = set(list(map(int,a.split(','))))
        
        result.append(list(set.difference(a,temp))[0])
        
        temp = a
    return result