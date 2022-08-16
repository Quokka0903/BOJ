import sys

input = sys.stdin.readline

T = int(input())

wait_m = sorted(list(map(int, (input().split()))))

res = 0
for i in range(T) :
    res += wait_m[i] * (T - i)

print(res)