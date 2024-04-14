def solution(n, times):
    left = 0
    right = n*max(times)
    
    while left < right:
        mid = (left + right) // 2
        tot = sum(mid//time for time in times)
        # print(tot)
        if tot >= n:
            right = mid
            # print(left)
        else: 
            left = mid +1 
            # print(left)
    return left