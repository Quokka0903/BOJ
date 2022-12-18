import sys
input = sys.stdin.readline

nums = []

for _ in range(9) :
    nums.extend(map(int, input().split()))

max_n = -1
max_i = -1
for i, unit in enumerate (nums) :
    if unit > max_n :
        max_n = unit
        max_i = i

print(max_n)
print((max_i // 9 + 1), (max_i % 9 + 1))