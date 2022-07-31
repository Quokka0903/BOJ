T = int(input())
for t in range(1, T+1):
    k = int(input())
    n = int(input())


    floor = [[0] * n for _ in range(k + 1)]
    for i in range(k + 1):
        for j in range(n):
            if i == 0:
                floor[i][j] += j + 1
            else:
                floor[i][j] = floor[i-1][j]+floor[i][j-1]


    print(floor[k][n-1])