def solution(elements):
    answer = 0
    
    n = len(elements)
    elements = elements*2
    s = set()
    
    #print(elements)
    for i in range(n):
        for j in range(n):
            s.add(sum(elements[i:i+j+1]))
    
    #print(s)
    return len(s)