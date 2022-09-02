import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

case = ''
for _ in range(N):
    case += 'IO'
case += 'I'

cnt = 0
i = 2 * N + 1
while i < M:
    if S[i - 2*N - 1 : i] == case:
        cnt += 1
        while True:
            if S[i:i+2] == 'OI':
                cnt += 1
                i += 2
            else:
                break
        i += 2 * N
    i += 1

print(cnt)