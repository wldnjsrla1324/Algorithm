def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0: #짝수
            answer.append(num+1)
        else: #홀수
            temp = '0'+bin(num)[2:]
            r_idx = temp.rfind('0')
            
            temp_list = list(temp)
            
            temp_list[r_idx] = '1'
            temp_list[r_idx+1] = '0'
            
            temp_str = "".join(temp_list)
            
            answer.append(int(temp_str,2))
    return answer