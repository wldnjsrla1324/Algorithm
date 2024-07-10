def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        start = commands[i][0] #i
        end = commands[i][1] #j
        k = commands[i][2] #k
        
        arr = array[start-1:end] # 리스트 슬라이스
        
        #정렬
        arr = sorted(arr)
        answer.append(arr[k-1]) 
        
    return answer