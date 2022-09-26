def com(idx, stack):
    if len(stack) == M:
        res.add(tuple(stack))
        return
    
    if idx >= N:
        return
    
    com(idx + 1, stack)
    com(idx + 1, stack + [nums[idx]])


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
res = set()

com(0 , [])

for unit in sorted(list(res)):
    print(*unit)