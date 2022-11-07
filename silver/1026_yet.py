import sys
input = sys.stdin.readline

N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

hubo = set()
def makecombi(stack, rest):
    if len(stack) == 5:
        hubo.add(stack)
        return
    
    for unit in rest:
        rest.remove(unit)
        makecombi(stack + [unit], rest[:])
        rest.append(unit)

print(hubo)
