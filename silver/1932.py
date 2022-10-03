import sys
input = sys.stdin.readline

N = int(input())

stack = [0] * N
for i in range(N):
    sam = list(map(int, input().split()))
    res = [0] * N
    for j in range(i + 1):
        if j > 0:
            res[j] = max(stack[j - 1], stack[j]) + sam[j]
        else:
            res[j] = stack[j] + sam[j]

    res, stack = stack, res
print(max(stack))