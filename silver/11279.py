import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    chk = int(input())
    if chk == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else :
        heapq.heappush(heap, [-chk, chk])