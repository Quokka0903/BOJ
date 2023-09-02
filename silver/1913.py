import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
field = [[0 for _ in range(n)] for _ in range(n)]

garo = [0, 1, 0, -1]
sero = [1, 0, -1, 0]

r = n//2
c = n//2
num = 1
len = 0

field[r][c] = num

while True:
    for i in range(4):
        for _ in range(len):
            r += garo[i]
            c += sero[i]
            num+=1
            field[r][c]=num
            if num==m:
                ans = [r+1, c+1]

    if r==c==0:
        break
    r -= 1
    c -= 1
    len += 2

for i in range(n):
    print(*field[i])

print(*ans)