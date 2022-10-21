chess = [1, 1, 2, 2, 2, 8]
bigyo = list(map(int, input().split()))

ans = []
for i in range(6):
    ans.append(chess[i] - bigyo[i])

print(*ans)
