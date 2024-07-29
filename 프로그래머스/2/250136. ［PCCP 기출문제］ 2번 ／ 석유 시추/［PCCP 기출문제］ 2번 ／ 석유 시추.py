#2번/석유 시추
from collections import deque
def solution(land):
    answer = 0
    
    m=len(land[0])
    n=len(land)
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    result = [0 for _ in range(m+1)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    def bfs(x,y):
        cnt=0
        visited[x][y]=True
        queue=deque()
        queue.append((x,y))
        min_y, max_y = y, y
        while queue:
            x,y=queue.popleft()
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            cnt+=1
            for i in range(4):
                nx=dx[i]+x
                ny=dy[i]+y
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if land[nx][ny]==0:
                    continue
                if not visited[nx][ny] and land[nx][ny]==1:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
        
        for i in range(min_y, max_y+1):
            result[i] += cnt
        
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i,j)
    answer = max(result)
    print(result)
        
    return answer