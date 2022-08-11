N, M = map(int, input().split())
chs_map = []
for _ in range(N):
    chs_map.append(list(input()))

min_time = 64
for i in range (N - 7) :
    for j in range (M - 7) :
        w_cnt, b_cnt = 0, 0
        for y in range(i, i + 8) :
            for x in range(j, j + 8) :
                if (x+y) % 2 == 0:
                    if chs_map[y][x] != 'W':
                        w_cnt += 1
                    if chs_map[y][x] != 'B':
                        b_cnt += 1
                else:
                    if chs_map[y][x] != 'B':
                        w_cnt += 1
                    if chs_map[y][x] != 'W':
                        b_cnt += 1
        res = (w_cnt if w_cnt < b_cnt else b_cnt)
        if res < min_time :
            min_time = res

print(min_time)