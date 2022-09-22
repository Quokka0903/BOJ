text = input()

nums = []
for unit in text:
    nums.append(unit)

print(''.join(sorted(nums, reverse = 1)))