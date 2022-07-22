arr = [[0]*1001 for _ in range(1001)]
T = int(input())
for t in range(1, T + 1):
    x, y, xlen, ylen = map(int, input().split())
    for i in range(y, y + ylen):
        arr[i][x:(x + xlen)] = [t] * xlen

cnt = [0] * (T + 1)
for i in range(1001):
    for j in range(1001):
        if arr[i][j]:
            cnt[arr[i][j]] += 1
for i in range(1, T + 1) :
    print(cnt[i])