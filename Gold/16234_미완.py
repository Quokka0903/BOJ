def my_df (s, nodes, union, border):
    stack = []
    border[s] = union
    while True:
        for w in nodes[s]:
            if border[w] == 0:
                stack.append(s)
                border[w] = union
                s = w
                print(border)
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break


N, L, R = map(int, input().split())

sum_ingu = 0
ddang = []
for _ in range(N):
    temp = list(map(int, input().split()))
    sum_ingu += sum(temp)
    ddang.append(temp)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
while True:
    dfs = [[] * N for _ in range(N**2)]
    sum_temp = 0
    sum_cnt = 0
    border = [0] * N**2
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if i + dy[k] < 0 or j + dx[k] < 0 or i + dy[k] >= N or j + dx[k] >= N:
                    continue

                cha = abs(ddang[i][j] - ddang[i + dy[k]][j + dx[k]])
                if cha >= L and cha <= R:
                    dfs[i * N + j].append((i + dy[k]) * N + j + dx[k])
    
    union = 1
    for i in range(N**2):
        if dfs[i]:
            if border[i] == 0:
                my_df(i, dfs, union, border)
                union += 1
                
    
    print(dfs)
    print(ddang)
    print(border)
    
    bk_cnt = 0
    for i in range(N):
        for j in range(N):

            if border[i][j] == 0:
                ddang[i][j] = sum_temp // sum_cnt
            else : 
                bk_cnt += 1
    
    if bk_cnt == N**2:
        break

    cnt += 1
    chk = 0
    for i in range(N):
        for j in range(N):
            if ddang[i][j] == sum_ingu // N **2:
                chk += 1
    if chk == N**2:
        break

    print(ddang)


print(cnt)