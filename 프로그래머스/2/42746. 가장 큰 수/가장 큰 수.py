def solution(numbers):
    answer = ''
    
    # numbers = [0,0,0,0]
    if sum(numbers) == 0:
        return '0'
        
    lst = list(map(str, numbers))
    
    #3을 곱한 값을 기준으로 정렬
    #ex. 34>3>30 -> '343'434 > '333' > '303'030
    #   333,303,343,555,999 => 9>5>34>3>30
    lst.sort(key=lambda x:x*3, reverse = True)
    
    answer = answer.join(lst)
    
    return answer