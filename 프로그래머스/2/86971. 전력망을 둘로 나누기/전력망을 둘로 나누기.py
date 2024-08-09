from collections import deque
def solution(n, wires):
    answer = 100000
    
    graph = [[] for i in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs(start):
        visited = [False]*(n+1)
        queue=deque()
        queue.append(start)
        visited[start] = True
        cnt=0
        while queue:
            c = queue.popleft()
            for i in graph[c]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    cnt+=1
        return cnt
    
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        print(graph)
        print(a,b)
        print()
        answer= min(abs(bfs(a)-bfs(b)),answer)
        
        graph[a].append(b)
        graph[b].append(a)
        
    return answer