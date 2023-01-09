# X, Y = map(int, input().split())
# Z = (Y // X) * 100

# if Z >= 99:
#     print(-1)

# else:
#     left = 1
#     right = 1000000000
#     res = 0
#     while left <= right:
#         mid = (left + right)//2
#         # print(left, mid, right)
#         if ((Y + mid) * 100 // (X + mid)) > Z:
#             res = mid
#             right = mid - 1
#         else:
#             left = mid + 1

#     print(res)


N , M = map(int,input().split())

Z = (M *100)//N
ans = 0
if Z >= 99:
    print(-1)
else:
    ans = 0
    start =1
    end = 1000000000
    while start <= end:
        mid = (start+end)//2
        if (M+mid)*100 // (N+mid) > Z:
            ans = mid
            end = mid -1
        else:
            start = mid+1
    print(ans)