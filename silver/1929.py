m, n = map(int, input().split())
    
for check in range(m, n + 1):
    flag = 1
        
    for j in range(2, int(check**0.5) + 1): 
        if check % j == 0 :
            flag = 0
            break
        
    if flag and check != 1 :
        print(check)