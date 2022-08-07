import sys
input = sys.stdin.readline()

T = int(input())
ans = set()
for _ in range(T) :
    ans.add(int(input()))

for i in ans :
    print (i)