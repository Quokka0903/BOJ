N, L = map(int, input().split())

start = 0
res = -1
idx = 0

for i in range(L, 101):
    start = (i * i - i) / 2
    if (N - start) % i == 0 and (N - start) // i >= 0:
        res = (N - start) // i
        idx = i
        break


if res == -1:

    print(-1)
else:
    for i in range(idx):
        print(int(res + i), end=' ')