num = int(input())

nanum = 2
while num > 1 :
    if num % nanum == 0:
        print(nanum)
        num = num // nanum
        continue

    nanum += 1