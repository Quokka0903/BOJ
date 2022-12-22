from collections import defaultdict
N, M = map(int, input().split())

put = defaultdict()
for _ in range(N):
    put[input()] = 1

cnt = 0
for _ in range(M):
    if input() in put:
        cnt += 1

print(cnt)