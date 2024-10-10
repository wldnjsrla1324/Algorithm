def solution(n, s):
    if n > s: return [-1]
    result = []
    ini = s//n
    for _ in range(n):
        result.append(ini)
    res = s%n
    print(res)
    for i in range(n-1,-1,-1):
        if res==0:
            break
        result[i]+=1
        res-=1
    return result