while True :
    chk_list = []
    flag = 0
    num = int(input())

    if num == 0 :
        break

    while num > 0 :
        chk_list.append(num % 10)
        num = num // 10
    for i in range(len(chk_list)) :
        if chk_list[i] != chk_list[len(chk_list) - i -1] :
            flag = 1
            break
    if flag == 0 :
        print('yes')
    else :
        print('no')