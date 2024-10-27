def solution(scores):
    answer = 0
    #[[2,2],[1,4],[3,2],[3,2],[2,1]]	4
    wanho = scores[0]
    
    s_scores=sorted(scores,key=lambda x:(-x[0],x[1]))
    #print(s_scores)
    ta, tb = s_scores[0][0], s_scores[0][1]
    n_scores=[]
    for a,b in s_scores:
        if a>wanho[0] and b>wanho[1]:
            return -1
        if ta>a and tb>b:
            continue
        else:
            n_scores.append([a,b])
            ta, tb = a, b
    n_scores.sort(key = lambda x:(-x[0]-x[1]))
    
    return n_scores.index(wanho)+1