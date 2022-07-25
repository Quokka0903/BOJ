H, M = map(int, input().split())
T = int(input())

M += T
while M > 59 :
    H += 1
    M -= 60
if H > 23 :
    H -= 24

print(f'{H} {M}')