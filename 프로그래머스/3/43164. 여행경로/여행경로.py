def solution(tickets):
    answer = []
    t_len = len(tickets)
    tickets.sort()  # 티켓을 알파벳 순으로 정렬합니다.

    def dfs(cur, visited, path):
        if len(path) == t_len + 1:  # 모든 티켓을 사용한 경우
            return path
            
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == cur:
                visited[i] = True
                next_path = dfs(tickets[i][1], visited, path + [tickets[i][1]])
                if next_path:  # 유효한 경로를 찾은 경우 즉시 반환
                    return next_path
                visited[i] = False  # 다른 경로를 탐색하기 위해 백트래킹
                
        return None  # 유효한 경로를 찾지 못한 경우

    visited = [False] * t_len
    answer = dfs("ICN", visited, ["ICN"])
    return answer

# 예제 테스트 케이스 실행
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
