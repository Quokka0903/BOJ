import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))

for i in range(n):
    p = queue.popleft()
    print(p[0], end=' ')
    if p[1] > 0:
        queue.rotate(-(p[1] - 1))
    else:
        queue.rotate(-p[1])