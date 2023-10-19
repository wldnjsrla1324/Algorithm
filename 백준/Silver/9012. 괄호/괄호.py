t = int(input())
for i in range(t):
  lst = input()
  stack = [-1]
  vps = "YES"
  for j in range(len(lst)):
    if stack == []:
      vps = "NO"
    elif(stack != [] and lst[j]==')'):
      stack.pop()
    else: 
      stack.append('(')
  if stack != [-1]:
    vps = "NO"
  print(vps)


