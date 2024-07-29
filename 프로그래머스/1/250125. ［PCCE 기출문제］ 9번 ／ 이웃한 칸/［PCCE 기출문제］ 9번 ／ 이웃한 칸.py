def solution(board, h, w):
    answer = 0
    color=board[h][w]
    
    n=len(board)
    m=len(board[0])
    
    dh=[1,-1,0,0]
    dw=[0,0,1,-1]
    
    for i in range(4):
        nh=h+dh[i]
        nw=w+dw[i]
        if nh<0 or nw<0 or nh>=n or nw>=m:
            continue
        if board[nh][nw]==color:
            answer+=1
    return answer