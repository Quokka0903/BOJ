import sys
input = sys.stdin.readline

N = int(input())
chingu = [input() for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if j == k :
                continue
            if chingu[j][k] == 'Y' or (chingu[j][i] == 'Y' and chingu[i][k] == 'Y'):
                visited[j][k] = 1

res = 0
for i in visited:
    res = max(res, sum(i))
print(res)