def solution(s, n):
    answer = ''
    '''
    print(ord("A"))#65
    print(ord("Z"))#90
    print(ord("a"))#97
    print(ord("z"))#122
    '''
    for ss in s:
        if ss==" ":
            answer+=' '
        else:
            if ord(ss)+n>122:
                a = ord(ss)+n-26
            elif ord(ss)+n>90 and ss.isupper()==True:
                a = ord(ss)+n-26
            else:
                a=ord(ss)+n
            print(chr(a))
            answer+=(chr(a))
    return answer