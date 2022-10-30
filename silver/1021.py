import collections
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
mlist = list(map(int, input().split()))
nlist = list(i for i in range(1, N + 1))

cnt = 0
for unit in mlist:
    if unit == nlist[0]:
        nlist = nlist[1:]

    else:
        l = len(nlist)
        for i in range(l):
            if nlist[i] == unit:
                break
        
        if i < l - i:
            cnt += i
        else:
            cnt += l - i
        
        nlist = nlist[i + 1:] + nlist[:i]

print(cnt)