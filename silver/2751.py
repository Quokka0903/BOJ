import sys

T = int(input())
ans = []
for _ in range(T) :
    ans.append(int(sys.stdin.readline()))

ans.sort()

for i in ans :
    print (i)