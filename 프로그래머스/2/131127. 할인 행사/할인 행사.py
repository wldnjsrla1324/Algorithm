def solution(want, number, discount):
    answer = 0
    want_d = dict(zip(want, number))
    #print(want_d)
    for i in range(len(discount)-9):
        d=discount[i:i+10]
        s_key = list(set(d))
        s_value=[]
        for s in s_key:
            s_value.append(d.count(s))
        discount_d = dict(zip(s_key, s_value))
        #print(discount_d)
        if want_d==discount_d:
            answer+=1
        
    return answer