#스택/큐
#프로세스
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    order = []

    length = len(priorities)
    i = 0
    
    while len(order) < length:
      pri = queue.popleft()
      if (len(queue)==0):
        # print(i)
        order.append(i%length)
        queue.append(0)
        break
      elif (pri < max(queue)):
        queue.append(pri)
      else:
        # print(i)
        order.append(i%length)
        queue.append(0)
      i += 1
      # print(queue)

    answer = order.index(location) +1
    # print(order)
    return answer

