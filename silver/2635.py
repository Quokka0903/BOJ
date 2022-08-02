def manymany(N, i, list) :
    if N - i < 0 :
        return list
    list.append(N - i)
    return manymany(i, N - i, list)

N = int(input())

max = 0
ans = []
for i in range(1, N) :
    temp = manymany(N, i, [N, i])
    if max < len(temp) :
        ans, max = temp, len(temp)

if N == 1 :
    ans = [1, 1, 0, 1]
    max = len(ans)

print(max)
for i in ans :
    print((i), end= ' ')