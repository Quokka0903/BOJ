import sys
input = sys.stdin.readline


N, M = map(int, input().split())
list_num = list(map(int, input().split()))
sum_num = [0]
sum_num.append(list_num[0])

for i in range(2, N + 1):
    sum_num.append(list_num[i - 1] + sum_num[i - 1])

for _ in range(M):
    a, b = map(int, input().split())
    print(sum_num[b] - sum_num[a - 1])