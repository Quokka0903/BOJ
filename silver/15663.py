import sys
input = sys.stdin.readline

def suyeol(temp, list_num):
    if len(temp) == M:
        res.add(tuple(temp))
        return
    
    for idx in range(len(list_num)):
        suyeol(temp + [list_num[idx]], list_num[:idx] + list_num[idx + 1:])

N, M = map(int, input().split())
desang = sorted(list(map(int, input().split())))
res = set()
suyeol([], desang)

for unit in sorted(list(res)):
    for text in list(unit):
        print(text, end=' ')
    print()