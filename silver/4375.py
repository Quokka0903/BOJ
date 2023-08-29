while 1:
    try:
        n = int(input())
    
    except:
        break
    
    num = 0
    i = 1

    while 1:
        num = num * 10 + 1
        num %= n
        if not num:
            print(i)
            break
        i += 1