from collections import deque

def find_person(winner, loser, node):
    queue = deque()
    visited = [False] * (len(winner)+1)
    
    for i in winner[node]:
        queue.append(i)
    
    while queue:
        x = queue.popleft()
        for i in winner[x]: 
            if not visited[i]: # 아직 탐색하지 않은 선수라면
                visited[i] = True
                winner[node].add(i) # 내가 이길 수 있는 사람에 i를 추가
                loser[i].add(node) # i가 지는 사람에 나를 추가
                queue.append(i)

def solution(n, results):
    winner = [set([]) for _ in range(n+1)] # 내가 이길 수 있는 사람을 저장
    loser = [set([]) for _ in range(n+1)] # 나보다 잘하는 사람을 저장
    
    for w,l in results:
        winner[w].add(l)
        loser[l].add(w)
        
    #print(winner,loser)
        
    for i in range(1,n+1):
        find_person(winner, loser, i)
        #print(winner, loser)
        
    answer = 0
    for i in range(1,n+1):
        if len(winner[i])+len(loser[i])+1 == n:
            answer+=1
    
    return answer