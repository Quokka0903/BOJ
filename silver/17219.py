N, M = map(int, input().split())

pwd = {}

for _ in range(N):
    site, pws = input().split()
    pwd[site] = pws

for _ in range(M):
    print(pwd[input()])