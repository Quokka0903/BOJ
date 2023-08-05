import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

res = 0
left, right = 0, n - 1

while left < right:
    mid = nums[left] + nums[right]
    if mid == x:
        res += 1
        left += 1
    elif mid < x:
        left += 1
    else:
        right -= 1
print(res)