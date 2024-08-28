def solution(food):
    
    answer=''
    
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            answer+=str(i)
    
    r = ''.join(reversed(answer))
    
    answer+='0'
    answer+=r
    return answer