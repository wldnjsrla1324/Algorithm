def solution(elements):
    answer = 0
    s=set()
    
    l = len(elements)
    
    elements+=elements
    
    
    for i in range(l):
        for j in range(l):
            s.add(sum(elements[j:j+i+1]))
    
        
    return len(s)