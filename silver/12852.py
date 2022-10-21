import sys
input = sys.stdin.readline

def com(num, stack, cnt):
    if num < 1:
        return

    global min_cnt
    if cnt > min_cnt:
        return

    if num == 1:
        if cnt < min_cnt:
            min_cnt = cnt
            ans.append(stack + [1])

    if num % 3 == 0:
        com(num//3, stack + [num], cnt + 1)
    if num % 2 == 0:
        com(num//2, stack + [num], cnt + 1)
    if num > 1:
        com(num - 1, stack + [num], cnt + 1)


N = int(input())
ans = []
min_cnt = N
com(N, [], 0)

print(min_cnt)
print(*ans[-1])