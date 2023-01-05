import sys
input = sys.stdin.readline

N = int(input())
snow = sorted(list(map(int, input().split())), reverse=True)

if snow[0] > 1440:
    print(-1)

else :
    flag = 0
    time = 0
    while N > 1:
        while not snow[-1]:
            snow.pop()
            N -= 1
        if N <= 1:
            break

        time += 1
        snow[0] -= 1
        snow[1] -= 1
        
        if time > 1440:
            flag = 1
            break

        if not snow[1]:
            snow = sorted([snow[0]] + snow[2:], reverse=True)
            N -= 1
        else:
            snow.sort(reverse=True)

    if flag:
        print(-1)
    else:
        print(time + sum(snow))