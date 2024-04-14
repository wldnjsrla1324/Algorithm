def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0]
        j = c[1]
        k = c[2]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
        
    return answer