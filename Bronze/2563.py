arr = [[0]*100 for _ in range(100)]

for T in range(int(input())):
    m, n = map(int, input().split())
    for i in range(m, m + 10):
        for j in range(n, n + 10):
            arr[i][j] = 1
print(arr)
ans = 0
for i in arr:
    ans += i.count(1)
print(ans)