from collections import deque

def solution(board):
    answer = 0
    
    n = len(board)
    m = len(board[0])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def find_nxny(x, y, direction):
        while True:
            x += dx[direction]
            y += dy[direction]
            if x < 0 or y < 0 or x >= n or y >= m or board[x][y] == 'D':
                x -= dx[direction]
                y -= dy[direction]
                break
        return x, y
    
    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y, 0)])  # (x, y, moves)
        visited = set((start_x, start_y))
        
        while queue:
            x, y, moves = queue.popleft()
            
            if board[x][y] == 'G':
                return moves
            
            for i in range(4):
                nx, ny = find_nxny(x, y, i)
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))
                    
        return -1
    
    for i in range(n):
        if 'R' in board[i]:
            for j in range(m):
                if board[i][j] == 'R':
                    return bfs(i, j)
                    
    return -1
