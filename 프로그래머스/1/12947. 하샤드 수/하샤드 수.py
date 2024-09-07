def solution(x):
    
    s = str(x)
    su = 0
    for ss in s:
        su+=int(ss)
    
    return True if x%su==0 else False