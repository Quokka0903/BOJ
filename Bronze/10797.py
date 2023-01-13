day = int(input())
nums = list(map(int, input().split()))

cnt = 0
for unit in nums:
    if unit == day:
        cnt += 1

print(cnt) 