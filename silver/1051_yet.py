import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pan = [input() for _ in range(N)]

max_dukke = 0
for y in range(N):
    for x in range(M):
        while True:
            dukke = 1
            flag = 0
            for dy, dx in [[1, 0], [1, 1], [0, 1]]:
                if 0 <= y + dukke * dy < N and 0 <= x + dukke * dx < M:
                    if not pan[y + dukke * dy][x + dukke * dx] == pan[y][x]:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            else:
                dukke += 1
            if flag:
                break
        
        if max_dukke < dukke:
            max_dukke = dukke

print(max_dukke**2)
