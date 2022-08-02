N, K = map(int, (input().split()))
list_num = [i for i in range(1, N + 1)]
idx = 0

print('<', end = '')
while len(list_num) > 1 :
    idx += K
    if idx >= len(list_num) :
        idx = idx % len(list_num)
        if idx == 0:
            idx += len(list_num)
    idx -= 1
    print(str(list_num.pop(idx)), end = ', ')

print(str(list_num.pop()) +'>')