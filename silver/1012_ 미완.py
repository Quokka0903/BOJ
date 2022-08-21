def my_dfs(s, nodes):
    visited = [[0] * M for _ in range(N)]
    stack = []
    while True:
        for w in nodes[s]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(s)
                s = w
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    ddang = [[0] * M for _ in range(N)]
    dfs = [[] for _ in range(M * N)]

    for _ in range(K):
        x, y = map(int, input().split())
        ddang[y][x] = 1
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for y in range(N):
        for x in range(M):
            for k in range(4):
                if y + dy[k] < 0 or x + dx[k] < 0 or y + dy[k] >= N or x + dx[k] >= M:
                    continue

                if ddang[y][x] == 1 and ddang[y + dy[k]][x + dx[k]] == 1:
                    dfs[y * N + x].append((y + dy[k]) * N + (x + dx[k]))
                    dfs[(y + dy[k] * N) + (x + dx[k])].append(y * N + x)

    unions = 
    for i in range(M * N):
        if dfs[i]:
            my_dfs(i, dfs)
            

    print(ddang)
    print(dfs)
