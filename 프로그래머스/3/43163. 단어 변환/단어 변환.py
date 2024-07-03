from collections import deque

def solution(begin, target, words):
    # words에 target없으면 0반환
    if target not in words:
        return 0
    
    #bfs함수
    def bfs(begin, target, words):
        queue = deque()
        queue.append([begin,0]) #초기값 초기화
        
        while queue:
            temp, step = queue.popleft()
            
            if temp == target:
                return step
            
            for word in words:
                count = 0
                for i in range(len(temp)):
                    if temp[i] != word[i]:
                        count +=1
                if count ==1:
                    queue.append([word,step+1])
    
    
    answer = bfs(begin, target, words)
    return answer