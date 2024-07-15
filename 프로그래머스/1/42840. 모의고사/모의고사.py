def solution(answers):
    answer = [0,0,0]
    #최소공배수 길이만큼 설정
    p1 = [1,2,3,4,5]*8
    p2 = [2,1,2,3,2,4,2,5]*5
    p3 = [3,3,1,1,2,2,4,4,5,5]*4
    #정답이면 1씩 추가
    for i in range(len(answers)):
        if answers[i] == p1[i%40]:
            answer[0] +=1
        if answers[i] == p2[i%40]:
            answer[1] +=1
        if answers[i] == p3[i%40]:
            answer[2] +=1
    max_score=max(answer)
    return [i+1 for i, score in enumerate(answer) if score == max_score]