N = 1000 - int(input())

cnt = 0
for unit in [500, 100, 50, 10, 5, 1]:
    cnt += N // unit
    N %= unit

print(cnt)