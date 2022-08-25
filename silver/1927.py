import sys
import heapq

input = sys.stdin.readline

T = int(input())

temp = []
for t in range(T):
    n = int(input())
    if n == 0:
        if temp:
            print(heapq.heappop(temp))
        else:
            print(0)
    else:
        heapq.heappush(temp, n)