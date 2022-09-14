import sys

input = sys.stdin.readline

V = int(input())
nodes = [[] for _ in range(V + 1)]
par = [[] for _ in range(V + 1)]
for _ in range(V - 1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

root = 1

stack = [root]

while stack:
    s = stack.pop()
    for unit in nodes[s]:
        if not par[unit]:
            par[unit].append(s)
            stack.append(unit)

for i in range(2, V + 1):
    print(*par[i])