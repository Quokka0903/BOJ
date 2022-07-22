arr = [[0]*1002 for _ in range(1002)]
T = int(input())
if T == 0 :
    print(T)

else :
    for t in range(1, T + 1):
        x, y, xlen, ylen = map(int, input().split())
        for i in range(x, x + xlen):
            for j in range(y, y + ylen):
                arr[i][j] = t
    cnt = [0] * (T + 1)
    for i in range(1002):
        for j in range(1002):
            if arr[i][j]:
                cnt[arr[i][j]] += 1
    for i in range(1, T + 1) :
        print(cnt[i])