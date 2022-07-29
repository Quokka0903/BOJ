n = int(input())

f1, f2, f_f = 1, 1, 0
if n >= 3 :
    for i in range(3, n + 1) :
        f_f = f1 + f2
        f1 = f2
        f2 = f_f
    print(f_f)

elif n == 0 :
    print(0)
else :
    print(f1)


