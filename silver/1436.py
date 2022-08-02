N = int(input())
i, cnt = 100, 0
while cnt != N :
    if str(i).count('666'):
        cnt += 1
    i += 1
print(i - 1)