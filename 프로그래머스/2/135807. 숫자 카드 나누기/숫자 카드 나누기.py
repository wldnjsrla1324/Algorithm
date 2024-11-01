import math
def solution(arrayA, arrayB):
    if len(arrayA) == 1:
        if arrayA[0] == arrayB[0]:
            return 0
        else:
            return max(arrayA[0], arrayB[0])
    arrA = arrayA[:]
    arrB = arrayB[:]
    a,b=0,0
    while arrayA:
        if a==0:
            a = math.gcd(arrayA.pop(),arrayA.pop())
        else:
            a = math.gcd(a,arrayA.pop())
    while arrayB:
        if b==0:
            b = math.gcd(arrayB.pop(),arrayB.pop())
        else:
            b = math.gcd(b,arrayB.pop())

    if a>b:
        for ar in arrB:
            if ar%a==0:
                return 0
    else:
        for ar in arrA:
            if ar%b==0:
                return 0
    return max(a,b)