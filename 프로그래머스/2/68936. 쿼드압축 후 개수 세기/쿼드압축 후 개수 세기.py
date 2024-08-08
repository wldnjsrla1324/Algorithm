def solution(arr):
    answer = [0,0]
    leng = len(arr) #행/열의 길이
    
    def quadtree(n_start, n_end, m_start, m_end):
        nonlocal answer
        ini = arr[n_start][m_start]
        for i in range(n_start,n_end):
            for j in range(m_start,m_end):
                if arr[i][j]!= ini:
                    mid_n = (n_start + n_end) // 2
                    mid_m = (m_start + m_end) // 2
                    quadtree(n_start, mid_n, m_start, mid_m)  # 2사분면
                    quadtree(mid_n, n_end, m_start, mid_m)  # 3사분면
                    quadtree(n_start, mid_n, mid_m, m_end)  # 1사분면
                    quadtree(mid_n, n_end, mid_m, m_end)  # 4사분면
                    return 
                    
        if ini==0:
            answer[0]+=1
        else:
            answer[1]+=1
        
        
    quadtree(0, leng, 0, leng)
    
    return answer