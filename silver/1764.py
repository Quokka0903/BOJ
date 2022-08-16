N, M = map(int, input().split())

dud = set()
bo = set()

for _ in range(N):
    dud.add(input())
for _ in range(M):
    bo.add(input())

dudbo = sorted(list(dud & bo))

print (len(dudbo))
for ans in dudbo:
    print(ans)