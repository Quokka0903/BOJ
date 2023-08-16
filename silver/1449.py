N, L = map(int,input().split())
taping = 0
cnt = 0

for i in sorted(list(map(int, input().split()))):
    if i > taping:
        cnt += 1
        taping = i + L - 1

print(cnt)