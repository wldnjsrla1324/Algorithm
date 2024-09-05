def solution(s):
    answer = ''
    lst = list(s)
    lst.sort(key = lambda x:ord(x))
    lst = lst[::-1]
    ''.join(lst)
    return ''.join(lst)