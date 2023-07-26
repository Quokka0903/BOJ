import sys

N, M = map(int, input().split())
ban = sys.stdin.read().splitlines()

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

cnt = 0
visited = [[False] * M for _ in range(N)]

def here():
    for x in range(N):
        for y in range(M):
            if ban[x][y] == 'I':
                return (x, y)

stack = [here()]
while stack:

    dx, dy = stack.pop()
    for x, y in direction:
        nx = dx + x
        ny = dy + y

        if (0 <= nx < N) and (0 <= ny < M):
            if (ban[nx][ny] != 'X') and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True

                if ban[nx][ny] == 'P':
                    cnt += 1

print(cnt) if cnt else print('TT')