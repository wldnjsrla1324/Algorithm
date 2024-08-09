from collections import deque
def solution(maps):
    answer = []
    
    n=len(maps)
    m=len(maps[0])
    
    s = 0
    
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    visited = [[False for _ in range(m)] for _ in range(n)]
            
    def bfs(x,y,s):
        queue=deque()
        queue.append((x,y))
        visited[x][y]=True
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if maps[nx][ny] != "X" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    s += int(maps[nx][ny])
                    queue.append((nx, ny))
        return s
                    
    
    
    cnt=0
    for i in range(n):
        for j in range(m):
            if maps[i][j]=="X":
                cnt+=1
            elif not visited[i][j]:
                answer.append(bfs(i,j,int(maps[i][j])))
                
                
    #모두 X인 경우
    if cnt==n*m:
        return [-1]
    
    answer.sort()
    return answer