def solution(a, b):
    answer = ''
    m_31 = [1,3,5,7,8,10,12]
    m_30 = [4,6,9,11]
    m_29 = [2]
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    d = 0
    for i in range(1,a):
        if i in m_31:
            d+=31
        elif i in m_30:
            d+=30
        else:
            d+=29
    d+=b
    return day[d%7]