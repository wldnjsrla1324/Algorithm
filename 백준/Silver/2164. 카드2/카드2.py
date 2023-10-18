#2164 카드2
from collections import deque

n = int(input())
queue = deque(range(1,n+1))
#print(queue)
for i in range(2*n-2):
  if(i%2==0):
    queue.popleft()
    #print(queue)
  else:
    queue.append(queue.popleft())
    #print(queue)
  #print(len(queue))
print(queue.popleft())