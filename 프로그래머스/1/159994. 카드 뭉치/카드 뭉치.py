def solution(cards1, cards2, goal):
    answer = 'No'
    li, ri = 0, 0
    for g in goal:
        if li < len(cards1) and cards1[li] == g:
            li += 1
        elif ri < len(cards2) and cards2[ri] == g:
            ri += 1

    if li + ri == len(goal):
        return "Yes"
    
    return answer