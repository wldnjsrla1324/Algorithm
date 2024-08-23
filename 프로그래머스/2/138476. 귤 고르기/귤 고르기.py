from collections import Counter
def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    tangerine.sort(key = lambda x:(count[x], x), reverse=True)
    return len(set(tangerine[0:k]))