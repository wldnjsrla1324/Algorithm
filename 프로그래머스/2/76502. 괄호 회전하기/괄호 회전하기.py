def bracket(s):
    stack=[0]
    for i in range(len(s)):
        if s[i] =='(' or s[i] =='{' or s[i] =='[':
            stack.append(s[i])
        elif s[i] == ')' and stack[-1] == '(':
            stack = stack[:-1]
        elif s[i] == '}' and stack[-1] == '{':
            stack = stack[:-1]
        elif s[i] == ']' and stack[-1] == '[':
            stack = stack[:-1]
        else:
            return False
    
    if stack==[0]:
        return True
    else:
        return False

def solution(s):
    answer = 0
    for x in range(len(s)):
        if bracket(s)==True:
            answer+=1
        left = s[0]
        s=s[1:]+left
    return answer

#bracket("[](){}")
#bracket("](){}[")
#bracket("[{}]()")
#bracket("}}}")