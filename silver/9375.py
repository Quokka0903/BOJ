from re import A


T = int(input())

for t in range(T):
    N = int(input())
    wear = [[] for _ in range(N)]
    type = []
    for _ in range(N):
        a, b = input().split()
        if b not in type:
            type.append(b)
        wear[type.index(b)].append(a)
        
    res = 1
    for i in range(N):
        res = res * (len(wear[i]) + 1)

    print(res - 1)