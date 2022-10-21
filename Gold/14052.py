import sys, collections
input = sys.stdin.readline

N, M = map(int, input().split())
zido = [list(map(int, input().split())) for _ in range(N)]

max_bang = 0
min_virus = N * M
for y1 in range(N):
    for x1 in range(M):
        if zido[y1][x1] == 0:
            zido[y1][x1] = 1
        
            for y2 in range(y1, N):
                for x2 in range(M):
                    if zido[y2][x2] == 0:
                        zido[y2][x2] = 1

                        for y3 in range(y2, N):
                            for x3 in range(M):
                                if zido[y3][x3] == 0:
                                    zido[y3][x3] = 1
                                    
                                    stack = collections.deque([])
                                    virus = 0
                                    for y in range(N):
                                        for x in range(M):
                                            if zido[y][x] == 2:
                                                stack.append([y, x])
                                                virus += 1

                                    temp_zido = []
                                    for unit in zido:
                                        temp_zido.append(unit[:])

                                    #print(temp_zido)

                                    def check(stack, min_virus, cnt, virus):
                                        while stack:
                                            y, x = stack.popleft()
                                            for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                                                sy, sx = y + dy, x + dx
                                                if 0 <= sy < N and 0 <= sx < M:
                                                    if temp_zido[sy][sx] == 0:
                                                        temp_zido[sy][sx] = 2
                                                        virus += 1
                                                        
                                                        if virus > min_virus:
                                                            return -1

                                                        stack.append([sy, sx])

                                        for y in range(N):
                                            for x in range(M):
                                                if temp_zido[y][x] == 0:
                                                    cnt += 1

                                        return cnt
                                    #print(temp_zido, cnt)

                                    cnt = check(stack, min_virus, 0, virus)
                                    if max_bang < cnt:
                                        max_bang = cnt

                                    zido[y3][x3] = 0

                        zido[y2][x2] = 0

            zido[y1][x1] = 0


print(max_bang)