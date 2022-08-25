def chk(a, n, y, x):
    d = a[y][x]
    flag = 1
    for i in range(y, y + n):
        for j in range(x, x + n):
            if a[i][j] != d:
                flag = 0
                break

    if flag == 1:
        if d == 0:
            white[0] += 1
            return 0
        else:
            blue[0] += 1
            return 0
    else:
        chk(a, n//2, y, x)
        chk(a, n//2, y + n//2, x)
        chk(a, n//2, y, x + n//2)
        chk(a, n//2, y + n//2, x + n//2)


N = int(input())
white = [0]
blue = [0]
chk([list(map(int, input().split())) for _ in range(N)], N, 0, 0)

print(white[0])
print(blue[0])