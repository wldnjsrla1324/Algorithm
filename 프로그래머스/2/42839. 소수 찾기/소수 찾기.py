from itertools import permutations
#소수 판별 함수
def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    numbers=list(numbers)
    temp=[]

    for i in range(1, len(numbers)+1):
        temp += list(permutations(numbers,i))
    #print(temp) 
    #[('0',), ('1',), ('1',), ('0', '1'), ('0', '1'), ('1', '0'), ('1', '1'), ('1', '0'), ('1', '1'), ('0', '1', '1'), ('0', '1', '1'), ('1', '0', '1'), ('1', '1', '0'), ('1', '0', '1'), ('1', '1', '0')]
    num = [int(''.join(t)) for t in temp]
    #print(num)
    #[0, 1, 1, 1, 1, 10, 11, 10, 11, 11, 11, 101, 110, 101, 110]

    for n in num:
        if prime(n):
            answer.append(n)
    
    answer=len(set(answer))
    return answer