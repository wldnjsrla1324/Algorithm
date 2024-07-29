def solution(bandage,health,attacks):
    t=bandage[0]
    x=bandage[1]
    y=bandage[2]
    cur_t=0
    end_t=attacks[-1][0]
    cur_h=health
    attack_s=0 #연속 공격 성공 횟수
    attack_i=0
    while cur_t<end_t:
        cur_t+=1
        if cur_t==attacks[attack_i][0]: #공격 시간
            if cur_h-attacks[attack_i][1]>0:
                cur_h-=attacks[attack_i][1]
                attack_i+=1
                attack_s=0
            else:
                return -1
        else: #공격 아님
            attack_s+=1
            if attack_s<t: 
                cur_h+=x
            else:
                cur_h+=(x+y)
                attack_s=0

        #체력 넘칠 경우 최대 체력으로 초기화
        if cur_h>=health:
            cur_h=health

    return cur_h