from re import X
import sys
input = sys.stdin.readline

for t in range(int(input())):
    M, N, x, y = map(int, input().split())
    
    flag = 0
    while M * N >= x:
        if (x - y) % N == 0:
            flag = 1
            break
        x += M

    if flag:
        print(x)
    else:
        print(-1)