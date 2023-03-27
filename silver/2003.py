# N, M = map(int, input().split())

# def cal (num):
#     idx = 0
#     sums = 0
#     while O[idx] > 0:
#         sums += O[idx]
#         idx += 1
#     O[idx] = int(num)
#     return sums + int(num)

# O = [0] * N
# L = list(map(cal, input().split()))

# # print(*O)
# # print(*L)

# left = 0
# right = 1
# cnt = 0

# while left <= right and right < N:
#     if L[right] - L[left] < M:
#         right += 1
    
#     elif L[right] - L[left] > M:
#         left += 1
    
#     else :
#         cnt += 1
#         right += 1

# print(cnt)

N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right<=N and left<=right:

    sum_nums = nums[left:right]
    total = sum(sum_nums)

    if total == M:
        cnt += 1

        right += 1

    elif total < M:
        right += 1

    else:
        left += 1

print(cnt)