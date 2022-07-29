import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))
temp_temp, max = 0, 0
ans = []

for i in range(K) :
    temp_temp += temp[i]
max = temp_temp

for i in range(N - K) :
    temp_temp -= temp[i]
    temp_temp += temp[i + K]
    if temp_temp > max :
        max = temp_temp

print(max)