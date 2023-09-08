def bin_search(nums, a):
    left, right = 0, len(nums) - 1
    res = -1
    while left <= right:
        m = (left + right) // 2
        if nums[m] < a:
            res = m
            left = m + 1
        else:
            right = m - 1
    return res
    
    
for _ in range(int(input())):
    cnt = 0
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    for unit in A:
        cnt += (bin_search(B, unit) + 1)
    print(cnt)