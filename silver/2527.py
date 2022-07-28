for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    x_a, x_b, y_a, y_b = max(x1, x2), min(p1, p2), max(y1, y2), min(q1, q2)

    x_cha, y_cha = (x_b - x_a), (y_b - y_a)
    
    if x_cha > 0 and y_cha > 0:
        print('a')
    elif x_cha < 0 or y_cha < 0:
        print('d')
    elif x_cha == 0 and y_cha == 0:
        print('c')
    else:
        print('b')