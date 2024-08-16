import math
def solution(arr):
    answer = 0
    
    def multi(a, b):
        return abs(a * b) // math.gcd(a, b)
        
    a = arr.pop()
        
    while arr:
        
        b = arr.pop()
        a = multi(a,b)
        
    return a