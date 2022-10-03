import sys
input = sys.stdin.readline

N = int(input())
gap = [list(map(int, input().split())) for _ in range(N)] + ([[0] * 3])

for i in range(1, N + 1):
    gap[i][0] = min(gap[i - 1][1], gap[i - 1][2]) + gap[i][0]
    gap[i][1] = min(gap[i - 1][0], gap[i - 1][2]) + gap[i][1]
    gap[i][2] = min(gap[i - 1][0], gap[i - 1][1]) + gap[i][2]

print(min(gap[i]))