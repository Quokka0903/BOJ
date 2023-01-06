import sys
input = sys.stdin.readline

N = int(input())
snow = sorted(list(map(int, input().split())), reverse=True)

time = 0
while snow:
    if len(snow) <= 1:
        time += snow[0]
        break
    snow[0] -= 1
    snow[1] -= 1
    time += 1

    snow.sort(reverse=True)
    while snow and snow[-1] == 0:
        snow.pop()

print(time if time <= 1440 else -1)