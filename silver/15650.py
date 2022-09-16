N, M = map(int, input().split())

def suyeol(numb, sy):
    if len(sy) == M:
        res.append(sy)
        return
    
    if numb > N:
        return
    
    suyeol(numb + 1, sy)
    suyeol(numb + 1, sy + [numb])

res = []
suyeol(1, [])
for unit in sorted(res):
    print(*unit)