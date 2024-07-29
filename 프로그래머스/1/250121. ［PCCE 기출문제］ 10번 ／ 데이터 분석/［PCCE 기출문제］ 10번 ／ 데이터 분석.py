def solution(data, ext, val_ext, sort_by):
    answer = []
    if ext=="code":
        idx_e=0
    elif ext=="date":
        idx_e=1
    elif ext=="maximum":
        idx_e=2
    else:
        idx_e=3
        
    if sort_by=="code":
        idx_s=0
    elif sort_by=="date":
        idx_s=1
    elif sort_by=="maximum":
        idx_s=2
    else:
        idx_s=3
        
    for i in range(len(data)):
        if data[i][idx_e]<val_ext:
            answer.append(data[i])
    answer.sort(key=lambda answer:answer[idx_s])
        
    
    return answer