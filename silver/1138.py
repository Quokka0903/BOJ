N = int(input())
men = list(map(int, input().split()))
ans = [0] * N
for i in range(N):
    taller = men[i]
    cnt = 0
    for j in range(N):
        if cnt == taller and ans[j] == 0:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            cnt += 1
print(*ans)