def com(stack, johab):
    if len(stack) == M:
        res.add(tuple(stack))
        return
    
    for i in range(len(johab)):
        com(stack + [johab[i]], johab[:])

N, M = map(int, input().split())

res = set()
nums = []
for i in range(1, N + 1):
    nums.append(i)
com([], nums)

for unit in sorted(res):
    print(*unit)