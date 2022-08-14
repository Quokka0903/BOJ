from collections import deque

temp = deque()
stack = deque()
res = deque()

n = int(input())
for i in range(n + 1):
    temp.append(i)

for _ in range(n):
    num = int(input())

    if temp[0] == 1:
        stack.append(temp.popleft())
    if stack[-1] < num:
        while stack[-1] != num:
            stack.append(temp.popleft())
            print('+')
    if stack[-1] == num:
        res.append(stack.pop())
        print('-')
