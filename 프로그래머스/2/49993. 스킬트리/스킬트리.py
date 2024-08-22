
def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        stack=''
        for s in st:
            if s in skill:
                stack+=s
        if stack == skill or skill.startswith(stack):
            answer+=1

        
    return answer