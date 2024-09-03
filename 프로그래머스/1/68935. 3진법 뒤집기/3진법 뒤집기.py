def solution(n):
    answer = 0
    n3 = ''
    while n>0:
        r = n%3
        n3+=(str(r))
        n//=3
    
    print(n3)
    print(int(n3,3))
    return int(n3,3)