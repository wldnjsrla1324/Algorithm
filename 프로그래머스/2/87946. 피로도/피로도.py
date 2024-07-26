from itertools import permutations
def solution(k, dungeons):
    answer = 0
    origin=k
    perm=list(permutations(dungeons,len(dungeons))) #가능한 모든 순열
    for i in range(len(perm)):
        k=origin #피로도 초기화
        temp=0 #탐험한 던전 개수 초기화
        
        for p in perm[i]:
            if k>=p[0] and k-p[1]>0:
                k-=p[1]
                temp+=1
            else:
                continue
        
        #현재 순열의 탐험한 던전 수와 기존 최대 기록과 비교
        if temp>answer:
            answer=temp
        
    return answer