N, M = map(int, input().split())
card = list(map(int, input().split()))

min = M
ans = 0
for i in range(N - 2) :
    for j in range(i + 1, N - 1) :
        for k in range(j + 1, N) :
            num = card[i] + card[j] + card[k]
            if (M - num) < min and (M - num) >= 0 :
                min = (M - num)
                ans = num
print(ans)