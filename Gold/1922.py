import sys
input = sys.stdin.readline

def find_set(x):
    while idx[x] != x:
        x = idx[x]
    return x

N = int(input())
M = int(input())

nodes = []
for _ in range(M):
    a, b, c = map(int, input().split())
    nodes.append([c, a, b])

nodes.sort()
idx = [i for i in range(N + 1)]

#print(nodes)
cnt = 0
total = 0
for val, n1, n2 in nodes:
    if find_set(n1) != find_set(n2):
        idx[find_set(n2)] = find_set(n1)
        cnt += 1
        total += val
        if cnt == N:
            break

print(total)
