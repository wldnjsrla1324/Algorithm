def solution(number, k):
    answer = ''
    length = len(number) - k #만들어야할 문자열 길이
    
    # 앞 k+1 str 잘라서 첫째자리 숫자 만들어야 함
    sub = number[:k+1]
    max_digit = max(sub)
    answer += max_digit
    tempIdx = number.index(max_digit)
    number = number[tempIdx+1:]
    
    # 남은 number의 길이 == answer의 길이 아닌 경우
    while len(answer) < length:
        # 남은 부분에서 다음 최댓값을 찾기 위한 범위 설정
        remaining_length = len(number) - (length - len(answer) - 1)
        if remaining_length > 0:
            sub = number[:remaining_length]
            max_digit = '0'
            for char in sub:
                if char > max_digit:
                    max_digit = char
                if max_digit == '9':  # 최댓값을 찾았으므로 더 이상 탐색할 필요 없음
                    break
            answer += max_digit
            tempIdx = number.index(max_digit)
            number = number[tempIdx + 1:]
        else:
            break
        
    return answer