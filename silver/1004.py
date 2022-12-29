for t in range(int(input())):

    start_x, start_y, end_x, end_y = map(int, input().split())
    
    cnt = 0
    for n in range(int(input())):

        circle_x, circle_y, circle_r = map(int, input().split())

        d1 = (((start_x - circle_x) ** 2) + ((start_y - circle_y) ** 2)) ** 0.5
        d2 = (((end_x - circle_x) ** 2) + ((end_y - circle_y) ** 2)) ** 0.5
        
        if (d1 < circle_r and d2 > circle_r) or (d1 > circle_r and d2 < circle_r):
            cnt += 1
    print(cnt)