def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def solution(numer1, denom1, numer2, denom2):
    # 두 분수의 합을 계산
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    
    # 최대공약수를 이용하여 기약분수로 만들기
    g = gcd(numer, denom)
    
    # 최대공약수로 나누어 기약분수 형태로 만듦
    answer = [numer // g, denom // g]
    return answer