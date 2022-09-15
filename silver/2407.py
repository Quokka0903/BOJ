n, m = map(int, input().split())

M = m
res = 1
for _ in range(m):
    res *= n
    n -= 1

for _ in range(m):
    res //= M
    M -= 1

print(res)