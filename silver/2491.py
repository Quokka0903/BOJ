T = int(input())
nums =list(map(int, input().split()))
cnt_a, cnt_b, max = 1, 1, 1
for i in range(1, T) :
    if nums[i] <= nums[i - 1] :
        cnt_a += 1
    else :
        cnt_a = 1
    if max < cnt_a :
        max = cnt_a

for i in range(1, T) :
    if nums[i] >= nums[i - 1] :
        cnt_b += 1
    else :
        cnt_b = 1
    if max < cnt_b :
        max = cnt_b

print (max)