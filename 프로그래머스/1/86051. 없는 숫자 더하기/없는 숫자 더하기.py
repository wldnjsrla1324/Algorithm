def solution(numbers):
    answer = 45
    for n in numbers:
        answer = answer - n
    
    return answer