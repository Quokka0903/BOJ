n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    item, value = map(int, input().split())
    for j in range(1, k + 1):
        if item > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item] + value)
print(dp[n][k])