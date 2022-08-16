def fac(a):
    res = a
    if a > 1 :
        return res * fac(a - 1)
    else :
        return res

num = int(input())

if num == 0:
    print(0)

else:

    res = str(fac(num))

    idx = -1
    cnt = 0
    while res[idx] == '0' :

        cnt += 1
        idx -= 1

    print(cnt)