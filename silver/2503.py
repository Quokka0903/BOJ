n = int(input())
baseball = [list(map(int, input().split())) for _ in range(n)]
count = 0

stack = []
def dfs(now):
  if now == 3:
    global count
    
    for i in range(n):
      strike, ball = 0, 0
      
      for j in range(3):
        target = str(baseball[i][0])
        if int(target[j]) == stack[j]:  strike += 1
        elif int(target[j]) in stack:  ball += 1

      if strike != baseball[i][1] or ball != baseball[i][2]:
        return
      
    count += 1
    return     
  
  for i in range(1, 10):
    if i not in stack:    
      stack.append(i)
      dfs(now + 1)
      stack.pop()

dfs(0)
print(count)