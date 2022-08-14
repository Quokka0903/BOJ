from collections import deque

T = int(input())

stack = deque()
for t in range(T):
    num = int(input())
    if num == 0:
        stack.pop()
        continue
    stack.append(num)

res = 0
for i in stack:
    res += i

print(res)