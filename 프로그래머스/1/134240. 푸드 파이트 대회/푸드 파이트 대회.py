def solution(food):
    
    answer=''
    
    for i in range(1,len(food)):
        if food[i]>1:
            for j in range(food[i]//2):
                answer+=str(i)
    r=reversed(answer)
    r=''.join(r)
    answer+='0'
    answer+=r
    return answer