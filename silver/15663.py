import sys
input = sys.stdin.readline

def suyeol(idx, temp):
    if len(temp) == M:
        res.add(tuple(temp))
        return
    
    if idx == N:
        return

    suyeol(idx + 1, temp)
    suyeol(idx + 1, temp + [desang[idx]])
    suyeol(idx + 1, [desang[idx]] + temp)

N, M = map(int, input().split())
desang = sorted(list(map(int, input().split())))
res = set()
suyeol(0, [])

for unit in sorted(list(res)):
    for text in list(unit):
        print(text, end=' ')
    print()