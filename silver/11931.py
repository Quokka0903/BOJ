n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse=True)
for num in nums:
    print(num)

