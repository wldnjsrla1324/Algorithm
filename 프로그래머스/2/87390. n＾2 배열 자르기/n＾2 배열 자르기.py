def solution(n, left, right):
    answer = []
    for k in range(left, right + 1):
        i = k // n
        j = k % n
        answer.append(max(i, j) + 1)
    return answer
""" 규칙 찾기
k   0123 4567 89..
    1234 2234 3334 4444
i   0000 1111 2222 3333
j   0123 0123 0123 0123
"""
#1234
#2234
#3334
#4444
""" 시간초과 풀이법
def solution(n, left, right):
    lst = [[0 for j in range(n)] for i in range(n)]
    arr = []
    for i in range(n): 
        for j in range(n):
            m = max(i+1,j+1)
            lst[i][j]=m
            arr.append(m)
    return arr[left:right+1]
"""
