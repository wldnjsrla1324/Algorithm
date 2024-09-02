def solution(keymap, targets):
    answer = []
    
    for target in targets:
        cnt = 0
        for t in target:
            temp = 100 
            for i in range(len(keymap)):
                key = keymap[i]
                if t in key and temp == -1:
                    #print(key.index(t)+1)
                    temp = key.index(t)+1
                elif t in key:
                    #print(key.index(t)+1)
                    temp = min(key.index(t)+1,temp)
                elif t not in key and temp ==100:
                    #print("-1")
                    temp = -1
            print(temp)
            if temp == -1:
                cnt = -1
                break
            else:            
                cnt += temp
        print()
        answer.append(cnt)
    return answer