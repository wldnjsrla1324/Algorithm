#from collections import deque 
def solution(x, y, n):
    answer = 0
    #queue = deque([x])
    s = set([x])
    while y not in s:
        ts=set()
        for i in s:
            if i+n<=y:
                ts.add(i+n)
            if i*2<=y:
                ts.add(i*2)
            if i*3<=y:
                ts.add(i*3)
        answer+=1
        s=ts
        #print(queue, answer)
        if not s:
            return -1
    return answer 