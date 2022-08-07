X, Y = map(int, input().split())
K = int(input())

a, b, cnt, stk = X, Y, 0, 0
ans_x, ans_y, temp, = 0, 0, 0

if X * Y < K :
    print(0)
else :
    if K <= 2 * (a + b) - 4 :
        pass
    else :
        while a >= 1 and b >= 1 :
            
            if a == 1 and b == 1 :
                temp = 1
            elif a == 1:
                temp = b
            elif b == 1:
                temp = a
            else :
                temp = 2 * (a + b) - 4
            if K <= stk + temp :
                break
            stk += temp
            a -= 2
            b -= 2
            cnt += 1

    if temp == 1:
        ans_x, ans_y = cnt + 1, cnt + 1

    else :
        if (K - stk) < b:
            ans_x = cnt + 1
            ans_y = cnt + (K - stk)

        elif (K - stk) <= a + b - 2 and (K - stk) >= b:
            ans_x = cnt + (K - stk) - b + 1
            ans_y = cnt + b

        elif (K - stk) > a + b - 2 and (K - stk) <= a + 2 * b - 3:
            ans_x = cnt + a
            ans_y = cnt + b - ((K - stk) - (a + b -2)) + 1

        elif (K - stk) > a + 2 * b - 3:
            ans_x = cnt + a - ((K - stk) - (a + 2 * b - 3)) + 1
            ans_y = cnt + 1


    print(ans_x, ans_y)