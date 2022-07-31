import sys

N = int(sys.stdin.readline())
nums = []
ans = [0 for _ in range(10000)]

for i in range(N):
    num = int(sys.stdin.readline())
    ans[num] += 1
    
for i in range(len(ans)):
    for j in range(ans[i]):
        print(i)