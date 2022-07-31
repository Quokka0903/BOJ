N, K = map(int, input().split())

ans1, ans2 = 1, 1

for i in range (N, N - K, -1) :
    ans1 *= i

for i in range (1, K + 1) :
    ans2 *= i

print(ans1 // ans2)