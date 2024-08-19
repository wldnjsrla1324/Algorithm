def solution(n, words):
    answer = []
    use = []
    pre = "" #직전 단어 저장
    
    for i in range(len(words)):
        if pre and pre[-1] != words[i][0]:
            answer.append(i%n + 1)
            answer.append(i//n + 1)
            return answer
        elif words[i] in use:
            answer.append(i%n + 1)
            answer.append(i//n + 1)
            return answer
        
        pre = words[i]
        use.append(words[i])
    
    if answer==[]:
        answer = [0,0]
    
    return answer 