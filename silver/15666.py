import sys
input = sys.stdin.readline

def com(idx, stack):
    if len(stack) == M:
        res.add(tuple(stack))
        return
    
    if idx >= N:
        return
    
    com(idx, stack + [hubo[idx]])
    com(idx + 1, stack + [hubo[idx]])
    com(idx + 1, stack)

N, M = map(int, input().split())
hubo = sorted(list(map(int, input().split())))

res = set()
com(0, [])

for unit in sorted(list(res)):
    print(*unit)