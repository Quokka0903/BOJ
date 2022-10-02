import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pyo = [list(map(int, input().split())) for _ in range(N)]
hap = [list(map(int, input().split())) for _ in range(M)]

for y in range(N):
    for x in range(N):
        if 0 <= y - 1:
            pyo[y][x] += pyo[y - 1][x]
        if 0 <= x - 1:
            pyo[y][x] += pyo[y][x - 1]
        if 0 <= y - 1 and 0 <= x - 1:
            pyo[y][x] -= pyo[y - 1][x - 1]

for y1, x1, y2, x2 in hap:
    res = pyo[y2 - 1][x2 - 1]
    if 0 <= y1 - 2:
        res -= pyo[y1 - 2][x2 - 1]
    if 0 <= x1 - 2:
        res -= pyo[y2 - 1][x1 - 2]
    if 0 <= y1 - 2 and 0 <= x1 - 2:
        res += pyo[y1 - 2][x1 - 2]
    
    print(res)
