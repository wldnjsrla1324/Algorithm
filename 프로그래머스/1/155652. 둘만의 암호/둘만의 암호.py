def solution(s, skip, index):
    answer = ''
    alpha='abcdefghijklmnopqrstuvwxyz'
    for sk in skip:
        alpha=alpha.replace(sk,'')
        
    #print(alpha)
    for ss in s:
        answer+=alpha[(alpha.index(ss)+index)%len(alpha)]
    return answer