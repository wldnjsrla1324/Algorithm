def solution(sizes):
    max_w = 0
    max_h = 0
    for i in range(len(sizes)):
        sizes[i][0], sizes[i][1] = min(sizes[i]), max(sizes[i])
    for i in range(len(sizes)):
        if max_w <= sizes[i][0]:
            max_w = sizes[i][0]
        if max_h <= sizes[i][1]:
            max_h = sizes[i][1]
    return max_w*max_h