import numpy as np
def solution(arr1, arr2):
    answer=[[0]*len(arr2[0]) for _ in range(len(arr1))]
    '''
    1 4    3 3
    3 2    3 3
    4 1
    
    1*3+4*3 1*3+4*3
    3*3+2*3
    
    5 4 3
    2 4 1
    3 1 1
    
    523
    441
    311
    '''
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            s=sum(arr1[i][k] * arr2[k][j] for k in range(len(arr2)))
            answer[i][j]=s
    return answer