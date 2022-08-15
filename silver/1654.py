K, N = map(int, input().split())

list_seon = []
for _ in range(K):
    list_seon.append(int(input()))

print(list_seon)

front, back = 0, 2147483647

max = 0
while front != (front + back) // 2:

    sum_seon = 0
    mid = (front + back) // 2

    for i in list_seon:
        sum_seon += i // mid

    if sum_seon < N:
        back = mid
    else :
        if mid > max:
            max = mid
        front = mid

print(max)
