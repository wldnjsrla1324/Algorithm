from collections import deque
def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    distance = [float('inf')] * (N+1)
    
    for r in road:
        graph[r[0]].append([r[1],r[2]])
        graph[r[1]].append([r[0],r[2]])
    
    queue = deque([1])
    distance[1] = 0
    
    while queue:
        now = queue.popleft()
        for nei, dis in graph[now]:
            n_dis = distance[now] + dis
            if n_dis < distance[nei]: 
                distance[nei] = n_dis
                queue.append(nei)
    print(distance)
    for d in distance:
        if d<=K:
            answer+=1
    return answer