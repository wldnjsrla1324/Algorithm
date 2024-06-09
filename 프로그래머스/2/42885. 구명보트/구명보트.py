def solution(people, limit):
    answer = 0
    startIndex = 0
    endIndex = len(people) - 1
    
    # 1. 무게순으로 정렬
    people.sort()
    
    # 2. 한 명 당 보트 하나 타고 있다고 가정
    answer = len(people)
    
    # 3. 맨 앞과 맨 뒤 사람의 몸무게 합이 제한 무게보다 큰지 확인
    while (startIndex < endIndex ):
        # 3-1. 크면, 뒤에서 앞으로 이동하며 사람 선택
        if (people[startIndex] + people[endIndex] > limit):
            endIndex -= 1
        # 3-2. 작거나 같으면, 이 두사람은 한 배에 탈 수 있으니 구명보트 하나 제거
        #  앞에서 뒤로 이동하여, 뒤에서 앞으로 이동하여 각각 사람을 선택
        else:
            answer -= 1
            startIndex += 1
            endIndex -= 1 
    # 4. 결과 반환    
    return answer