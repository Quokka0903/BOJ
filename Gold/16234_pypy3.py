import sys

input = sys.stdin.readline

def my_df (s, nodes, union, border, ddang):
    stack = []
    border[s] = union
    unions[border[s] - 1] += ddang[s]
    union_cnt[border[s] - 1] += 1
    while True:
        for w in nodes[s]:
            if border[w] == 0:
                stack.append(s)
                border[w] = union
                unions[border[w] - 1] += ddang[w]
                union_cnt[border[w] - 1] += 1
                s = w

                #print(unions)
                #print(union_cnt)
                #print(border)
                #print(ddang)
                #print(dfs)
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
    ddang.extend(temp)

print(ddang)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
while True:
    dfs = [[] * N for _ in range(N**2)]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if i + dy[k] < 0 or j + dx[k] < 0 or i + dy[k] >= N or j + dx[k] >= N:
                    continue

                cha = abs(ddang[i * N + j] - ddang[(i + dy[k]) * N + j + dx[k]])
                if cha >= L and cha <= R:
                    dfs[i * N + j].append((i + dy[k]) * N + j + dx[k])
    
    unions = [0]
    union_cnt = [0]
    union = 1
    border = [0] * N**2
    for i in range(N**2):
        if dfs[i]:
            if border[i] == 0:
                my_df(i, dfs, union, border, ddang)
                union += 1
                unions.append(0)
                union_cnt.append(0)
    
    #print(unions)
    #print(union_cnt)
    #print(border)
    #print(ddang)
    #print(dfs)


    if union_cnt[0] == 0: 
        break

    cnt += 1
    chk = 0
    for i in range(N):
        for j in range(N):
            if border[i * N + j] != 0:
                ddang[i * N + j] = unions[border[i * N + j] - 1] // union_cnt[border[i * N + j] - 1]
            if ddang[i * N + j] == sum_ingu // N **2:
                chk += 1
    if chk == N**2:
        break

print(cnt)