import collections
import sys
input = sys.stdin.readline

def johab(i, stack):
    if len(stack) == M:
        res.append(stack)
        return
    
    if i >= len(hubo):
        return

    johab(i + 1, stack)
    johab(i + 1, stack + hubo[i])

N, M = map(int, input().split())
zido = [list(map(int, input().split())) for _ in range(N)]

hubo = []
for y in range(N):
    for x in range(N):
        if zido[y][x] == 2:
            hubo.append([[y, x]])
            zido[y][x] = N ** 2 + 1
        if zido[y][x] == 1:
            zido[y][x] = -1
        else:
            zido[y][x] = N ** 2 + 1

res = []
johab(0, [])


min_cnt = N ** 2 + 1
for unit in res:
    
    imsi_zido = []
    for i in range(N):
        imsi_zido.append(zido[i][:])

    stack = collections.deque([])
    for y, x in unit:
        stack.append((y, x, 0))
        imsi_zido[y][x] = 0

    while stack:
        a, b, v = stack.popleft()
        for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            sy, sx = dy + a, dx + b
            if 0 <= sy < N and 0 <= sx < N:
                if imsi_zido[sy][sx] != -1 and v + 1 < imsi_zido[sy][sx]:
                    imsi_zido[sy][sx] = v + 1
                    stack.append((sy, sx, v + 1))

    cnt = 0
    flag = 0
    for y in range(N):
        for x in range(N):
            if imsi_zido[y][x] == N**2 + 1 :
                flag = 1
                break
            if imsi_zido[y][x] > cnt:
                cnt = imsi_zido[y][x]
        if flag:
            break
        
    if flag:
        continue
    if min_cnt > cnt:
        min_cnt = cnt

if min_cnt == N ** 2 + 1:
    print(-1)
else:
    print(min_cnt)