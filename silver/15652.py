N, M = map(int, input().split())

def suyeol(numb, sy):
    if len(sy) == M:
        res.add(tuple(sy))
        return
    
    if numb > N:
        return
    
    suyeol(numb, sy + [numb])
    suyeol(numb + 1, sy)
    suyeol(numb + 1, sy + [numb])

res = set()
suyeol(1, [])
for unit in sorted(list(res)):
    print(*unit)