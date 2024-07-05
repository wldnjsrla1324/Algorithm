def solution(n, computers):
    # dfs 탐색
    def dfs(i, visited, computers):
        visited[i] = True #방문 컴퓨터는 방문 처리
        for j in range(n):
            if not visited[j] and computers[i][j] == 1:
                dfs(j, visited, computers)

    visited = [False]*n #초기 방문여부 세팅
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            answer +=1 #dfs 탐색 종료하면 네트워크 하나 추가
    return answer

#case1
#110
#110
#001

#case2
#110
#111
#011
