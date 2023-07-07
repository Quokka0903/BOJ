from sys import stdin

n, m  = map(int, stdin.readline().split(' '))
zido = [list(map(int, stdin.readline().split(' '))) for _ in range(n)]
distance = [ [0 for _ in range(m)] for _ in range(n)]

def find_destination():
    for i in range(n):
        for j in range(m):
            if zido[i][j] == 2:
                return i, j

def check_denied(sx, sy):
    for i in range(n):
        for j in range(m):
            if zido[i][j] == 1 and not distance[i][j]:
                distance[i][j] = -1
    return

i, j = find_destination()
stack = [[i, j, 0]]
while stack:
    now = stack.pop(0)
    if not distance[now[0]][now[1]] or distance[now[0]][now[1]] > now[2]:
        distance[now[0]][now[1]] = now[2]
        for nx, mx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ny = now[0] + nx
            my = now[1] + mx
            if 0 <= ny < n and 0 <= my < m and zido[ny][my] and not (ny == i and my == j):
                if not distance[ny][my] or distance[ny][my] > now[2] + 1:
                    stack.append([ny, my, now[2] + 1])

check_denied(i, j)
for hang in distance:
    for yeol in hang:
        print(yeol, end=" ")
    print()