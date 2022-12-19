N = int(input())

sort_n = []
for _ in range(N):
    sort_n.append(int(input()))

for unit in sorted(sort_n):
    print(unit)