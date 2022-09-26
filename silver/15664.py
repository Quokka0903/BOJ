def nm10(idx, stack):
    if len(stack) == M:
        res.add(tuple(stack))
    
    if idx >= N:
        return
    
    nm10(idx + 1, stack)
    nm10(idx + 1, stack + [nums[idx]])



N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

res = set()
nm10(0, [])

for unit in sorted(list(res)):
    print(*unit)