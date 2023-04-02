while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    maps = []
    for i in range(h):
        maps.append(list(map(int, input().split())))

    sums = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                sums += 1
                stack = [[i, j]]
                while stack:
                    spot = stack.pop()
                    maps[spot[0]][spot[1]] += 1
                    for unit in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                        sx, sy = spot[0] + unit[0], spot[1] + unit[1]
                        if 0 <= sx < h and 0 <= sy < w and maps[sx][sy] == 1:
                            stack.append([sx, sy])

    print(sums)