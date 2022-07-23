xy = [0] * 2
for i in range(2) :
    xy[i] = int(input())

if xy[0] > 0 :
    if xy[1] > 0 :
        print(1)
    else :
        print(4)
else :
    if xy[1] > 0 :
        print(2)
    else :
        print(3)