nums = [0] * 10
for unit in input():
    nums[int(unit)] += 1

if (nums[6] + nums[9]) % 2 :
    nums[6] = (nums[6] + nums[9]) // 2 + 1
else:
    nums[6] = (nums[6] + nums[9]) // 2

nums[9] = nums[6]

print(max(nums))