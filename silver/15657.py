import sys
input = sys.stdin.readline


def NandM(unit, stack):
    if len(stack) == M:
        res.add(tuple(stack))
        return
    
    if unit >= N:
        return
    
    NandM(unit, stack + [nums[unit]])
    NandM(unit + 1, stack)
    NandM(unit + 1, stack + [nums[unit]])


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
res = set()
NandM(0, [])
for ans in sorted(res):
    print (*ans)