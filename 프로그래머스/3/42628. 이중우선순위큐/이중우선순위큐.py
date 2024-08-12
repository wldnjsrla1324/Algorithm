from collections import deque
def solution(operations):
    answer = []
    queue = deque()
    for oper in operations:
        if oper.startswith('I '):
            queue.append(int(oper[2:]))
        elif oper=='D 1' and queue:
            queue.remove(max(queue))
        elif oper=='D -1' and queue:
            queue.remove(min(queue))
    return [max(queue),min(queue)] if queue else [0,0]