from collections import deque

N = int(input())

zips = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
q = deque()
unions = deque()

union = 0
for y in range(N):
    for x in range(N):
        if zips[y][x] == '1':
            if visited[y][x] == 0:
                q.append((y, x))
                visited[q[0][0]][q[0][1]] = 1
                union += 1
                cnt = 1
                while q:
                    s = q.pop()
                    for k in range(4):
                        if 0 <= s[0] + d[k][0] < N and 0 <= s[1] + d[k][1] < N:
                            if zips[s[0] + d[k][0]][s[1] + d[k][1]] == '1':
                                if visited[s[0] + d[k][0]][s[1] + d[k][1]] == 0:
                                    visited[s[0] + d[k][0]][s[1] + d[k][1]] = 1
                                    q.append((s[0] + d[k][0], s[1] + d[k][1]))
                                    cnt += 1
                unions.append(cnt)

print(union)
for unit in sorted(unions):
    print(unit)