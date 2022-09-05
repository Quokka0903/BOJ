from collections import deque
import sys

input = sys.stdin.readline

chk = input()

nums = []
idx = 0
cnt = 0
while idx < len(chk) - 1:
    stack = ''
    if chk[idx].isdigit():
        while chk[idx].isdigit():
            stack += chk[idx]
            idx += 1
        nums.append(int(stack))
        stack = ''
    
    else:
        nums.append(chk[idx])
        idx += 1
    cnt += 1

nums_1 = []
i = 0
while i < cnt:
    if nums[i] == '+':
        nums_1[-1] += nums[i + 1]
        i += 2
    else :
        nums_1.append(nums[i])
        i += 1

ans = 0
for i in range(len(nums_1)):
    if nums_1[i] == '-':
        nums_1[i + 1] *=  -1
    else :
        ans += nums_1[i]

print(ans)
