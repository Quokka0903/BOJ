for i in range(int(input())):
    dots = []
    dist = []
    for j in range(4):
        dots.append(list(map(int, input().split())))
    
    for j in range(4):
        for k in range(j + 1, 4):
            dist.append((dots[j][0] - dots[k][0])**2 + (dots[j][1] - dots[k][1])**2)
    
    dist.sort()

    if (dist[0] == dist[1] == dist[2] == dist[3]) and (dist[4] == dist[5]):
        print(1)
    else:
        print(0)
