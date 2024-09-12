#from itertools import permutations
import math
def solution(n, k):
    answer = []
    lst = list(_ for _ in range(1,n+1))
    while n>0:
        idx = (k-1)//math.factorial(n-1)
        answer.append(lst.pop(idx))
        k = k % math.factorial(n-1)
        n-=1
        print(answer, lst, k)
    return answer