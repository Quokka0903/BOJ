def com(stack, johab):
    if len(stack) == M:
        res.add(tuple(stack))
        return
    
    for i in range(len(johab)):
        com(stack + [johab[i]], johab[:])

N, M = map(int, input().split())

res = set()
nums = sorted(list(map(int, input().split())))
com([], nums)

for unit in sorted(res):
    print(*unit)