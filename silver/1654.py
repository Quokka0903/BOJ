K, N = map(int, input().split())

list_seon = []
for _ in range(K):
    list_seon.append(int(input()))

front, back = 1, max(list_seon)

while front <= back:

    sum_seon = 0
    mid = (front + back) // 2

    for i in list_seon:
        sum_seon += i // mid

    if sum_seon >= N:
        front = mid + 1
    else :
        back = mid - 1

print(back)