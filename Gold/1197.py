def find_set(x):
    while idx[x] != x:
        x = idx[x]
    return x

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
nodes = []
for _ in range(E):
    n1, n2, val = map(int, input().split())
    nodes.append([val, n1, n2])

nodes.sort()

idx = [i for i in range(V + 1)]

cnt = 0
total = 0
for val, n1, n2 in nodes:

    if find_set(n1) != find_set(n2):
        cnt += 1
        total += val
        idx[find_set(n2)] = find_set(n1)

        if cnt == V:
            break

print(total)