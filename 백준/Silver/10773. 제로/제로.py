#10773 제로
stack = []
k = int(input())
for i in range(k):
  n = int(input())
  if (n==0):
    stack.pop()
  else:
    stack.append(n)
print(sum(stack))