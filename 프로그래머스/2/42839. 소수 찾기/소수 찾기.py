#소수 찾기
from itertools import permutations
def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
def solution(numbers):
    answer=0
    temp=[]
    numbers=list(numbers)
    #print("numbers: ",numbers)
    for i in range(1, len(numbers)+1):
        temp+=list(permutations(numbers,i))
    #print("temp: ",temp)
    #num = [(''.join(t)) for t in temp]
    num = [int(''.join(t)) for t in temp]
    num = list(set(num))
    #print("num: ",num)

    for i in range(len(num)):
        if isPrime(num[i]):
            answer+=1
    return answer

#print(solution("17"))
#3
#print(solution("011"))
#2