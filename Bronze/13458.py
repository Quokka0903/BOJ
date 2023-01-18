N = int(input())
A = list(map(int,input().split()))
B, C = map(int, input().split())
cnt = 0
for unit in A:
    if unit > B:
        if (unit - B) % C:
            cnt += ((unit - B) // C) + 2
        else:
            cnt += ((unit - B) // C) + 1
    else:
        cnt += 1
print(cnt)