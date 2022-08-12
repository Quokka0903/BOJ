N = int(input()) # 미완

sugar_5 = N // 5
rest_5 = N % 5
sugar_3 = (rest_5) // 3
rest = (N % 5) % 3

bongzi = sugar_5 + sugar_3 + rest
min_bongzi = N

while True:
    bongzi = sugar_5 + sugar_3 + rest
    if rest == 0:
        if min_bongzi > bongzi:
            min_bongzi = bongzi
    else :
        if sugar_5 == 0:
            break
        sugar_5 -= 1
        rest_5 += 5
        sugar_3 = (rest_5) // 3
        rest = (N % 5) % 3
        
print(min_bongzi)