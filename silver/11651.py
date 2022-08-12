import sys

input = sys.stdin.readline

T = int(input())

list_dot = []
for t in range(T):
    list_dot.append(list(map(int, input().split())))

ans = sorted(list_dot, key = lambda x: (x[1], x[0]))

for i in ans :
    print(*i)