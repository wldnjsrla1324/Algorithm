def solution(k, ranges):
    answer = []
    area = []
    #정적분(넓이) 구하기
    while k>1:
        pre_k = k
        if k%2==0:
            k = k//2
        else:
            k = 3*k + 1
        area.append((pre_k+k)/2)
    print(area)
    n = len(area)
    for ran in ranges:
        a=ran[0]
        b=n+ran[1]
        print(a, b)
        if a<=b:
            answer.append(sum(area[a:b]))
        else:
            answer.append(-1.0)
    return answer