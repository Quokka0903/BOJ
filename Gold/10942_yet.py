import sys
input = sys.stdin.readline

N = int(input())
nlist = ('').join(input().split())

#print(nlist)
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    if S >= 2:
        #print(nlist[S - 1 : E])
        #print(nlist[E - 1 : S - 2 : -1])
        print(1 if nlist[S - 1 : E] == nlist[E - 1 : S - 2 : -1] else 0)
    else:
        #print(nlist[S - 1 : E])
        #print(nlist[E - 1 :  : -1])
        print(1 if nlist[S - 1 : E] == nlist[E - 1 :  : -1] else 0)