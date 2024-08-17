from itertools import permutations, combinations
def solution(elements):
    answer = 0
    ele = ''
    s = set()
    
    l = len(elements)
    
    elements+=elements
    print(elements)
    
    for i in range(l) : 
        for j in range(l) : 
            s.add(sum(elements[j:j+i+1]))
            
        
    return len(s)