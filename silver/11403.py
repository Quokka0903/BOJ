import sys

input = sys.stdin.readline

N = int(input())

nodes = [[] for _ in range(N)]
possible = [list(map(int, input().split())) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if possible[y][x] == 1:
            nodes[y].append(x)

for y in range(N):
    for x in range(N):
        visited = [0] * N
        
        flag = 0

        stack = []
        stack.append(y)
        while stack:
            s = stack.pop()
            visited[s] = 1
            for unit in nodes[s]:
                if unit == x:
                    print('1', end= ' ')
                    flag = 1
                    break
                if visited[unit] == 0:
                    stack.append(unit)    

            if flag:
                break
        if flag :
            continue
        print('0', end= ' ')
    print()