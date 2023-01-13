T = int(input())
cnt = [0, 0, 0]

if T >= 300:
    cnt[0] += T // 300
    T %= 300
if T >= 60:
    cnt[1] += T // 60
    T %= 60
if T >= 10:
    cnt[2] += T // 10
    T %= 10

if T > 0:
    print(-1)
else:
    print(*cnt)