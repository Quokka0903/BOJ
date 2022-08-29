for t in range(int(input())): 
    man = list(map(int, input().split()))
    sum = 0
    for i in range(1, man[0] + 1):
        sum += man[i]
    
    ave = sum / man[0]

    cnt = 0
    for j in range(1, man[0] + 1):
        if man[j] > ave:
            cnt += 1
    
    print(f'{cnt/man[0] * 100:.3f}%')