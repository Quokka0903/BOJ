from collections import deque

temp = deque()
stack = deque()
ans = ''
flag = True

n = int(input())
for i in range(1, n + 1):
    temp.append(i)

for _ in range(n):
    num = int(input())

    while temp and temp[0] <= num:
        stack.append(temp.popleft())
        ans += '+'
        
    if stack and stack[-1] == num:
        stack.pop()
        ans += '-'
    else :
        flag = False

if flag :
    for ch in ans:
        print(ch)
else:
    print('NO')