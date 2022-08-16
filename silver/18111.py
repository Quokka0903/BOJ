import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
mine = []
for _ in range(N):
    mine.extend(list(map(int, input().split())))

com_num = min(mine)

min_time = 2147483647
res_num = 0

while com_num <= 256:
    temp_B = B
    time_mine = 0
    
    for i in range(N * M):
        if mine[i] < com_num:
            temp_B -= (com_num - mine[i])
            time_mine += (com_num - mine[i])

        elif mine[i] > com_num:
            temp_B += (mine[i] - com_num)
            time_mine += 2 * (mine[i] - com_num)

        else :
            continue

    if temp_B >= 0:
        if min_time >= time_mine:
            min_time = time_mine
            res_num = com_num

    com_num += 1

print(min_time, res_num)