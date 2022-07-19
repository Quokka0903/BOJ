while True :
    T = list(map(int, input().split()))
    if sum(T) == 0:
        break
    m = max(T)
    T.remove(m)
    if T[0]**2 + T[1]**2 == m**2:
        print('right')
    else:
        print('wrong')