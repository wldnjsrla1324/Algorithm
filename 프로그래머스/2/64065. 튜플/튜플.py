def solution(s):
    result = []
    answer = []
    s_split = list(s[2:-2].split('},{'))
    #print(s_split)
    s_split.sort(key = lambda x:len(x))
    #print(s_split)
    for sp in s_split:
        temp = set(list(map(int,sp.split(','))))
        
        result = result + list(set.difference(temp,answer))
        answer=temp
    return result